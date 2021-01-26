# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:37:49 2019

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def perceptronAgi(personelAd,maasGirdisi,kotaGirdisi):
    x1=1 # 1.örnegim ile verimsiz oldugunu aga gösterdim
    x2=0 
    x3=0 # 2.ornegim ile verimli oldugunu aga gosterdim.
    x4=1
    w1=1 
    w2=2;
    learnLambda=0.5
    esikDegeri=-1
    net1=0 
    net2=0
    gercekDeger1=0 
    gercekDeger2=0
    beklenenDeger1=1 
    beklenenDeger2=0
    iterasyon=0
    yeniGirdi1=-1
    yeniGirdi2=-1
    
    if(kotaGirdisi>=maasGirdisi):
        beklenenDeger1=1
        x1=1
        x2=0
        yeniGirdi1=1
        yeniGirdi2=0
    else:
        x3=0
        x4=1
        beklenenDeger2=0
        yeniGirdi1=0
        yeniGirdi2=1
  
    while True:
        iterasyon=iterasyon+1
        net1=x1*w1+x2*w2
        if net1>=esikDegeri:
            gercekDeger1=1
            #if beklenenDeger1==gercekDeger1:
                
            if beklenenDeger1>gercekDeger1:
                w1=w1-(learnLambda*x1)
                w2=w2-(learnLambda*x2)
        elif net1<=esikDegeri:
            iterasyon=iterasyon+1
            gercekDeger1=0
            #if beklenenDeger1==gercekDeger1:
                
            if beklenenDeger1>gercekDeger1:
                w1=w1+(learnLambda*x1)
                w2=w2+(learnLambda*x2)
            if beklenenDeger1<gercekDeger1:
                w1=w1-(learnLambda*x1)
                w2=w2-(learnLambda*x2)
        #2.ornek için
        net2=x3*w1+x4*w2
        if net2>esikDegeri:
            iterasyon=iterasyon+1
            gercekDeger2=1
           # if beklenenDeger2:gercekDeger2:
            
            if beklenenDeger2<gercekDeger2:
                w1=w1-(learnLambda*x3)
                w2=w2-(learnLambda*x4)
            if beklenenDeger2>gercekDeger2:
                w1=w1+(learnLambda*x3)
                w2=w2+(learnLambda*x4)
        if net2<=esikDegeri:
            iterasyon=iterasyon+1
            gercekDeger2=0
            #if beklenenDeger2==gercekDeger2:
            
            if beklenenDeger2<gercekDeger2:
                w1=w1-(learnLambda*x3)
                w2=w2-(learnLambda*x4)
            if beklenenDeger2>gercekDeger2:
                w1=w1+(learnLambda*x3)
                w2=w2+(learnLambda*x4)
                
        if(beklenenDeger1==gercekDeger1 and beklenenDeger2==gercekDeger2):
            break
    #print("Agirlik1: ",w1)
    #print("Agirlik2: ",w2)
    sonuc=w1*yeniGirdi1+w2*yeniGirdi2;
    if(sonuc==1):
           print("Ad soyad ve Sonuc: ",personelAd,"Verimlidir")
    else:
        print("Ad soyad ve Sonuc: ",personelAd,"Verimsizdir")
  
     
        

#csv dosyasındaki tabloyu veriSeti adli degiskene atadım ve utf-8 için ayarladım
veriSeti=pd.read_csv("YazilimciFirmasi.csv",sep=';',encoding='iso-8859-1') 
#verim_orani alanını floata çevirebilmek için virgül kısmını nokta ile değiştirdim
veriSeti["Verim_orani"]=veriSeti["Verim_orani"].apply(lambda x:x.replace(',','.'))


#ilgili alanlari floata donusturdum
veriSeti['Verim_orani']=veriSeti['Verim_orani'].astype(float)
veriSeti['Maas']=veriSeti['Maas'].astype(float)
veriSeti['Aylik_Satis']=veriSeti['Aylik_Satis'].astype(float)

#veri setim hakkinda genel bilgileri aldım.
veriSeti.info()

#maas ve aylik_satis degerlerim cok büyük oldugundan her alani 1000e bölüyorum
veriSeti["Maas"]=veriSeti["Maas"]/1000;
veriSeti["Aylik_Satis"]=veriSeti["Aylik_Satis"]/1000;
veriSeti.head() #verinin degistigini goruyoruz

personelAd=pd.Series(veriSeti["Personel Adi"])
maasDizi=pd.Series(veriSeti["Maas"])
kotaDizi=pd.Series(veriSeti["Aylik_Satis"])
for i in range(0,len(maasDizi+1)):
    perceptronAgi(personelAd[i],maasDizi[i],kotaDizi[i])


#veri gorsellestirme kısmi
plt.figure(figsize=(24,12))



adlar = veriSeti['Personel Adi']
incomes = veriSeti['Verim_orani']
y_post = np.arange(len(adlar))
plt.bar(y_post, incomes,align='center',alpha=0.5)
plt.xticks(y_post,adlar)

plt.ylabel('Verim Oranı')
plt.axhline(y=0,color='red')

plt.xlabel('Personel İsim ve Soyisimler')
plt.title('Personellere Göre Verimlilik Oran Tablosu')



      
        
                
#https://dev.to/shamdasani/build-a-flexible-neural-network-with-backpropagation-in-python bak..