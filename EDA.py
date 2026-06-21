
#Data type of each column
print(df.dtypes)
#statistical summary of the dataset
print(df.describe())
#count of unique values in each column
print(df.nunique())

#Check value counts for categorical variables
print(df['Sex'].value_counts())

print(df['Pclass'].value_counts())

print(df['Survived'].value_counts())

print(df['Embarked'].value_counts())

#survival distribution 
plt.figure(figsize=(6,4))
sns.countplot(x='Survived',data=df)
plt.title("Survival Distribution")
plt.show()

#Survival by gender
plt.figure(figsize=(6,4))
sns.countplot(x='Sex',hue='Survived',data=df)
plt.title("Survival by Gender")
plt.show()

# Survival by Passenger Class
plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()

#Age distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Age'],bins=30,kde=True)
plt.title('Age Distribution')
plt.show()

# Fare Distribution
plt.figure(figsize=(8,4))
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title("Fare Distribution")
plt.show()