
#Feature importance from Random Forest
importances = pd.Series(rf.feature_importances_, index=x.columns)
importances = importances.sort_values(ascending=False)

plt.figure(figsize=(10,6))
importances.head(10).plot(kind='barh',color='steelblue')
plt.title("top 10 FeatureImportances")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

#confusion matrix heatmap
cm = confusion_matrix(y_test,rf_pred)
sns.heatmap(cm,annot=True,fmt='d',cmap='Blues',
            xticklabels=['Not Survived', 'Survived'],
            yticklabels=['Not Survived', 'Survived'])
plt.title("Confusion Matrix")
plt.show()

#survival rate by top features
df_orig = pd.read_csv("C:\\Users\\Yogeendra\\Downloads\\Titanic-Dataset.csv")
print(df_orig.groupby('Sex')['Survived'].mean())
print(df_orig.groupby('Pclass')['Survived'].mean())