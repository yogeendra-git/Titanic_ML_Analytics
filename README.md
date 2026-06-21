# Titanic Survival Prediction using Machine Learning

## Project Overview

This project analyzes the famous Titanic dataset and builds machine learning models to predict passenger survival. The workflow follows a complete data science pipeline including Exploratory Data Analysis (EDA), Data Cleaning, Feature Engineering, Data Encoding, Model Training, Evaluation, and Feature Importance Analysis.

The objective is to identify the factors that influenced survival and develop predictive models capable of estimating whether a passenger would survive the disaster.

---

## Dataset

The dataset contains passenger information such as:

* Passenger ID
* Passenger Class (Pclass)
* Name
* Sex
* Age
* Number of Siblings/Spouses aboard (SibSp)
* Number of Parents/Children aboard (Parch)
* Ticket Number
* Fare
* Cabin
* Port of Embarkation
* Survival Status

Target Variable:

* Survived

  * 0 = Did Not Survive
  * 1 = Survived

---

## Project Structure

```text
Titanic-Survival-Prediction/
│
├── import.py
├── EDA.py
├── cleaning.py
├── feature_engineering.py
├── encoding.py
├── Train&evaluate_model.py
├── feature_imp%insights.py
├── Titanic-Dataset.csv
└── README.md
```

---

## Workflow

### 1. Data Import and Initial Exploration

The dataset is loaded using Pandas and initial exploration is performed using:

* head()
* info()
* describe()
* shape
* column inspection

This helps understand the dataset structure and identify missing values.

---

### 2. Exploratory Data Analysis (EDA)

Several analyses and visualizations are performed:

#### Statistical Analysis

* Data types inspection
* Unique values count
* Value counts of categorical features

#### Visualizations

1. Survival Distribution
2. Survival by Gender
3. Survival by Passenger Class
4. Age Distribution
5. Fare Distribution

These visualizations help identify patterns related to passenger survival.

---

### 3. Data Cleaning

Missing values are handled as follows:

#### Age

Missing values are replaced using the median age.

#### Embarked

Missing values are replaced using the most frequent port (mode).

#### Cabin

A new feature called HasCabin is created:

* 1 → Cabin information available
* 0 → Cabin information missing

The Cabin column is then removed.

---

### 4. Feature Engineering

Several new features are created to improve model performance.

#### FamilySize

```python
FamilySize = SibSp + Parch + 1
```

Represents the total family members traveling together.

#### IsAlone

```python
IsAlone = 1 if FamilySize == 1 else 0
```

Identifies passengers traveling alone.

#### AgeGroup

Passengers are categorized into:

* Child
* Teen
* Adult
* Middle-Aged
* Senior

#### FareGroup

Fare values are grouped into:

* Low
* Medium
* High
* Premium

#### Title Extraction

Titles are extracted from passenger names:

Examples:

* Mr
* Mrs
* Miss
* Master

Rare titles are grouped under a single category called Rare.

---

### 5. Data Encoding and Scaling

Machine learning models require numerical inputs.

#### Label Encoding

The Sex column is encoded:

* Male → 1
* Female → 0

#### One-Hot Encoding

Applied to:

* Embarked
* Title

#### Feature Scaling

StandardScaler is used on:

* Age
* Fare

This standardizes the numerical features.

#### Columns Removed

The following columns are dropped:

* PassengerId
* Name
* Ticket
* Sex
* AgeGroup
* FareGroup

---

### 6. Machine Learning Models

Two classification algorithms are implemented.

#### Logistic Regression

A linear classification algorithm used as a baseline model.

#### Random Forest Classifier

An ensemble learning algorithm based on multiple decision trees.

---

### 7. Model Evaluation

Models are evaluated using:

#### Accuracy Score

Measures overall prediction accuracy.

#### Classification Report

Provides:

* Precision
* Recall
* F1 Score

#### Confusion Matrix

Visualizes:

* True Positives
* True Negatives
* False Positives
* False Negatives

#### Cross Validation

5-Fold Cross Validation is performed to estimate model stability and generalization capability.

---

### 8. Feature Importance Analysis

Random Forest feature importance is used to identify the most influential predictors.

A horizontal bar chart displays the Top 10 Most Important Features.

This helps understand which passenger attributes contribute most to survival prediction.

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Key Insights

### Gender Impact

Female passengers had a significantly higher survival rate compared to males.

### Passenger Class Impact

Passengers traveling in First Class had a higher probability of survival than those in lower classes.

### Family Influence

Passengers traveling with family showed different survival patterns compared to those traveling alone.

### Age Influence

Children generally had better survival rates than older passengers.

---
## Machine Learning Pipeline

```text
Data Collection
       ↓
Data Exploration
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Encoding & Scaling
       ↓
Train-Test Split
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Feature Importance Analysis
```
## Conclusion

This project demonstrates a complete end-to-end machine learning workflow using the Titanic dataset. Through data preprocessing, feature engineering, model training, and evaluation, meaningful insights were extracted and predictive models were developed to estimate passenger survival. The project highlights the importance of data preparation and feature engineering in improving machine learning performance.

#RESULT

top Features(RF importance)
Sex
female    0.742038
male      0.188908
Name: Survived, dtype: float64
Pclass
1    0.629630
2    0.472826
3    0.242363
Name: Survived, dtype: float64

model_acuuracy:::/

Logistic Regression: 81.01 %
Random Forest:       80.45 %
              precision    recall  f1-score   support

           0       0.83      0.85      0.84       110
           1       0.76      0.72      0.74        69

    accuracy                           0.80       179
   macro avg       0.79      0.79      0.79       179
weighted avg       0.80      0.80      0.80       179

CV Accuracy: 80.02% ± 3.82%
