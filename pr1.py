import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")   # Ensure file is in same folder

# Last 5 rows
df.tail()

df.info()

df.describe()

categorical_cols = df.select_dtypes(include='object').columns
numerical_cols = df.select_dtypes(include=['int64','float64']).columns

categorical_cols, numerical_cols

for col in categorical_cols:
    print(f"\n{col} unique values:")
    print(df[col].unique())

df.isnull().sum()

target = "Survived"
features = df.drop(columns=[target]).columns

target, features

df.shape

df['Survived'].value_counts()

df['Survived'].value_counts(normalize=True)
