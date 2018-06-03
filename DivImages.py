#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:47:14 2018

@author: salvador
"""
from PIL import Image
try:
    imagen=Image.open("Images/Ejemplo.jpg")
  #  imagen.show()
except:
    print("No se ah podido cargar la imagen.")
    exit

Reducida=imagen.resize((800,600)) #Se cambiaran los valores luego.
#Reducida.show()
Reducida.save("Images/Reducida.jpg")
Aux=0
#Se empieza a recortar las imagenes.
for i in range(10):
    for j in range(10):    
        NewDir='Images/ImageRec'
        Box=list([80*j,60*i,80*(j+1),60*(i+1)])
        Box=tuple(Box)
        region=Reducida.crop(Box)
        NewDir+=str(Aux)
        NewDir+='.jpg'
        region.save(NewDir)
        Aux+=1