
#craeting new features
df['FamilySize'] = df['SibSp'] + df['Parch']+1

print(df['FamilySize'])

#solo-traveller flag
df['IsAlone'] = (df['FamilySize']==1).astype(int)

print(df['IsAlone'])

#age groups divides into undestandable categories
df['AgeGroup'] = pd.cut(df['Age'],bins=[0,12,18,35,60,100],
                        labels=['child','Teen','Adult','Middle-Aged','Senior'])
print(df['AgeGroup'].head(10))

#fare groups divides into understandable categories
df['FareGroup'] = pd.cut(
    df['Fare'],bins=[0,10,30,100,600],
    labels=['Low','Medium','High','Premium'])
print(df['FareGroup'].head(10))

#extracting title from name
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.')
df['Title'] = df['Title'].replace(
    ['Lady','Countess','Capt','Col','Don',
     'Dr','Major','Rev','Sir','Jonkheer','Dona'], 'Rare')
print(df[['Title','Name']].head(10))

print(df[['FamilySize','IsAlone','AgeGroup','FareGroup','Title']].head(10))

