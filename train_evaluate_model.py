from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LogisticRegression 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

#Define features (X) and target (y)
x=df.drop(columns=['Survived'])
y=df['Survived']

#Split the dataset into training and testing sets
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

#logistic regression model
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)
lr_pred = lr.predict(X_test)
print(lr_pred)

#Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100,random_state=42)
rf.fit(X_train,y_train)
rf_pred = rf.predict(X_test)
print(rf_pred)

#evaluation metrics
print("Logistic Regression:",round(accuracy_score(y_test,lr_pred)*100,2),"%")
print("Random Forest:",round(accuracy_score(y_test,rf_pred)*100,2),"%")
print(classification_report(y_test,lr_pred))

#cross-validation for Random Forest model
cv_scores = cross_val_score(rf, x, y, cv=5, scoring='accuracy')

print (f"cv accuracy scores: {cv_scores.mean()*100:.2f}% + {cv_scores.std()*100:.2f}%")