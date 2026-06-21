#importing the required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Load dataset
df=pd.read_csv("Titanic_dataset.csv")

#quick look at the dataset
print(df.head(10))

print(df.info())

print(df.describe())

print(df.shape)

print(df.columns.tolist())