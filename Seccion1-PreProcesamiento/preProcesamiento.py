# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Plantilla de pre procesado de datos

#Importar librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importar el dataset
dataset = pd.read_csv('~/Documents/udemy/machine-learning/datasets/Part1-Data_Preprocessing/Data.csv');

#Reemplazar valores desconocidos

#Todas las columnas, excepto la última, primero son las filas, después las columnas
X = dataset.iloc[:,:-1].values

#Ultima columna
y = dataset.iloc[:,3].values

#Tratamiento de los NAs
from sklearn.impute import SimpleImputer

#axis 0 tomará los valores de la columna, 1 de la fila
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", verbose= 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Codificar datos categoricos (transformarlos a números)
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()     
X[:,0] = le_X.fit_transform(X[:,0]) 


#Variable ordinal tiene cierto orden, ejemplo un número es mayor que otro
#Variable Dummy o One hot encoding

#Transformación de X
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct_x = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)
X = np.array(ct_x.fit_transform(X), dtype=np.float)

#Transformación de y
le_y = preprocessing.LabelEncoder()     
y = le_y.fit_transform(y) 