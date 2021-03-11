#Plantilla para pre procesado de datos

#Importar librerias


#Importar dataset
dataset <- read.csv('datasets/Part1-Data_Preprocessing/Data.csv')

#Reemplazar valores desconocidos
dataset$Age <- ifelse(is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                      dataset$Age)

dataset$Salary <- ifelse(is.na(dataset$Salary),
                      ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                      dataset$Salary)
