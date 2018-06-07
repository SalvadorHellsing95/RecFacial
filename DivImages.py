#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:47:14 2018

@author: salvador
"""
from PIL import Image, ImageDraw
try:
    imagen=Image.open("Images/Ejemplo.jpg")
  #  imagen.show()
except:
    print("No se ah podido cargar la imagen.")
    exit

Reducida=imagen #Se cambiaran los valores luego.
#Reducida.show()
#Reducida.save("Images/Reducida.jpg")
Aux=0
#Se empieza a recortar las imagenes.
a=Reducida.size
Points=[]
jump=10
Size=50
for i in range(0,(a[0]),jump):
    for j in range(0,(a[1]),jump):
        if (i+Size)>a[0]:
            continue
        if (j+Size)>a[1]:
            continue
        NewDir='Images/ImageRec'
        Box=list([i,j,i+Size,j+Size])
        Points.append(Box);
        #Box=list([20*j,20*i,20*(j+1),20*(i+1)])
        Box=tuple(Box)
        region=Reducida.crop(Box)
        NewDir+=str(Aux)
        NewDir+='.jpg'
        #region.save(NewDir)
        Aux+=1
        
        
SaveDraw='Images/Final.jpg'
ImDraw=Image.open("Images/Ejemplo.jpg")
Dra=0
for Aux in Points:
    if(Dra%100==0):
    
        draw=ImageDraw.Draw(ImDraw)
        draw.line((Aux[0], Aux[1]) + (Aux[0],Aux[3]), fill=200)
        draw.line((Aux[0], Aux[1]) + (Aux[2],Aux[1]), fill=200)
        draw.line((Aux[0], Aux[3])+(Aux[2],Aux[3]), fill=200)
        draw.line((Aux[2],Aux[3])+(Aux[2],Aux[1]), fill=200)
        del draw
        ImDraw.save(SaveDraw)
    Dra+=1
