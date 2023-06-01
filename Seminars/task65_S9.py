# Задача №65 & 67 & 69
# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы


#65
# penguins = sns.load_dataset("penguins")
# penguins.head()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('penguins.csv')
#print(df.head())
#print(df.columns)
# print(df.describe())

# sns.scatterplot(data=df, x='species', y='island')
# plt.show()

# sns.scatterplot(data=df, x='bill_length_mm', y='species')
# plt.show()

# sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='bill_length_mm', size='bill_length_mm', sizes=(2,100))
# plt.show()


# sns.scatterplot(data=df, x='sex', y='bill_length_mm', hue='bill_length_mm', size='bill_length_mm', sizes=(2,100))
# plt.show()

# Использовать PairGrid с типом графика на ваш выбор
#cols = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# plt.show()


#Изобразить Heatmap/ температурная карта
# sns.heatmap(data=df.corr())
# sns.heatmap(data=df.corr(numeric_only=True), annot= True)
# plt.show()

# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# sns.heatmap(data=df[cols], annot = True)
# plt.show()

# sns.heatmap(data=df.corr(numeric_only= True), annot=True, vmin = 1, vmax=1, center=0, cmap = 'crest')
# plt.show()

#67
# Задача №67. Общее обсуждение
# 1. Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

# df.loc[df['bill_length_mm'] <= 35, 'bill_len'] = 'low' # прописываем в колонку, где клювы <= 35 слово low
# df.loc[(df['bill_length_mm'] > 35) & (df['bill_length_mm'] <= 42), 'bill_len'] = 'middle' # прописываем в колонку, где клювы 35-42 слово middle
# df.loc[df['bill_length_mm'] > 42, 'bill_len'] = 'high' # прописываем в колонку, где клювы > 42 слово high

# print(df[['bill_length_mm', 'bill_len']]) #вывели колонки, которые хотим видеть, в тч новую колонку bill_len
# print(df.groupby('bill_len')['bill_length_mm'].mean()) #сгруппированные по размеру и взяты средние значения от длины клюва
# df.groupby('bill_len')['bill_length_mm'].mean().plot(kind='bar')
# plt.show()

#69
# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ
df.loc[df['flipper_length_mm'] <= 190, 'height_group'] = 'low'
df.loc[(df['flipper_length_mm'] > 190) & (df['flipper_length_mm'] <= 210), 'height_group'] = 'middle'
df.loc[df['flipper_length_mm'] > 210, 'height_group'] = 'high'

print(df[['flipper_length_mm', 'height_group']])
print(df.groupby('height_group')['flipper_length_mm'].mean())

sns.histplot(data=df, x='flipper_length_mm', hue= 'height_group')
plt.show()



