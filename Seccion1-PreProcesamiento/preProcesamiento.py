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

#Todas las columnas, excepto la última
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values





