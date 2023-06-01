# Задача 40: 
# Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

# 42:
# Узнать какая максимальная households в зоне минимального значения population


#40
import pandas as pd

df = pd.read_csv('california_housing_train.csv')
# print(df.head())
df1 = df[(df.population > 0) & (df.population < 500)]
print(df1)
print(df1['median_house_value'].mean())
print()


#42
df2 = df.loc[df.population < df.population.quantile(.20)]
print(df2.households.max())
print(df2)