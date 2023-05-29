# Задача 57 b 59 b 61

# Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

# 59:
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное значение median_house_value
# 2. Показать максимальное median_house_value, где median_income = 3.1250
# 3. Узнать какая максимальная population в зоне минимального значения median_house_value

import pandas as pd

df = pd.read_csv('california_housing_train.csv') # получили данные из файла и сохранили их в переменнную df

#print(df.head()) # читаем начальные строки

#print(df.shape) # посмотреть сколько строчек в файле
#print(df.dtypes)  смотрим типы данных в таблице
# print(df.isnull().sum())
#print(df[df['median_income'] < 2][['median_house_value']]) # Показать median_house_value где median_income < 2
#print(df.describe()) # описание столбцов
#print(df[['longitude', 'latitude']]) #вывести 2а первых столбца
# df.iloc[ : , 0:2] # вывести 2а первых столбца
# print(df[(df.housing_median_age < 20) & (df.median_house_value > 70000)]) #Выбрать данные где housing_median_age < 20 и median_house_value > 70000
# print(df.median_house_value.max(), df.median_house_value.min()) #пределить какое максимальное и минимальное значение median_house_value
# print(df.loc[(df.median_income == 3.125), ['median_income', 'median_house_value']].max()) #Показать максимальное median_house_value, где median_income = 3.1250

# Узнать какая максимальная population в зоне минимального значения median_house_value:
# df1 = df.loc[df.median_house_value < df.median_house_value.quantile( .15)]
# print(df1.population.max())
# print(df1)
