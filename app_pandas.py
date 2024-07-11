import pandas as pd

df=pd.read_csv('salaries.csv')
print(df)

print(df['Salary'])

print(df[['Salary', 'Age']])

print("Max Salary:: ",df['Salary'].max())

print(df['Age'] > 30)

print(df[df['Age']>30])

print(df['Age'].unique())

print(df['Age'].nunique())

print(df.columns)

print(df.info())

print(df.describe())

print(df.index)