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

#Todas las columnas, excepto la última
X = dataset.iloc[:,:-1].values

#Ultima columna
y = dataset.iloc[:,3].values

#Tratamiento de los NAs
from sklearn.impute import SimpleImputer

#axis 0 tomará los valores de la columna, 1 de la fila
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean", verbose= 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])




