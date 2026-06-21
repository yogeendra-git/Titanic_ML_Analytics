
from sklearn.preprocessing import LabelEncoder,StandardScaler

#Label encoding
le = LabelEncoder()
df['sex_enc'] = le.fit_transform(df['Sex'])
print(df['sex_enc'])

#one-hot encoding for multi-categorical variables
df = pd.get_dummies(df,columns=['Embarked','Title'], drop_first=True)
print(df.head())

#droping columns that are not needed for model training
df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Sex',
                  'AgeGroup', 'FareGroup'], inplace=True)

#scale the numerical features
scaler = StandardScaler()
df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])

print(df.head())
print("final shape:", df.shape)