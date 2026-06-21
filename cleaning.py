
#Finding all missing values in the dataset
print(df.isnull().sum())
print(df.isnull().sum() / len(df)*100)

#Fix Age — impute with median
df['Age'].fillna(df['Age'].median(), inplace=True)

#Fix Embarked — impute with mode (most frequent)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

#Cabin — 77% missing, create binary feature instead
df['HasCabin']=df['Cabin'].notna().astype(int)
df.drop(columns=['Cabin'], inplace=True)


print(df.isnull().sum())

#checking if any duplicates are present in the dataset
print(df.duplicated())