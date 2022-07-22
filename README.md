# [Personal Key Indicators of Heart Disease](https://heart-disease-diagnosis-app.herokuapp.com/)

## **Introduction**
In this project we will be making a full analysis on heart-disease dataset that contains 2020 anual [CDC](https://www.cdc.gov/heartdisease/risk_factors.htm) survey data of nearly 320k adults related to their health status.

**<ins>Aim</ins>:** Our goal is build A Predictive Machine Learning Model capable of diagnosing new Heart Disease cases and deploy it into a [WebApp](https://heart-disease-diagnosis-app.herokuapp.com/).

## **About Dataset**
Originally, the dataset is a major part of the Behavioral Risk Factor Surveillance System (BRFSS), which conducts annual telephone surveys to gather data on the health status of U.S. residents.
It consists of 319795 rows and 18 columns.

**Dataset Columns**:
This dataset contains 18 variables (9 booleans, 5 strings and 4 decimals).

<ins>Sample</ins>:
|Column Name     | Description                                                                                          |
|:--------------:|------------------------------------------------------------------------------------------------------|
|`**HeartDisease**`| Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI)|
|`**BMI**`| Body Mass Index (BMI)|
|`**Smoking**`| Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]|
|`**AlcoholDrinking**`| Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week|

## **Project Details**
This Project is devided into two parts:

**PART 1** contains the first steps of applying EDA and preparing the data for Machine Learning stage including the following steps:
- Data Wrangling
- Data Cleansing
- Exploratory Data Analysis (EDA)
- EDA Conclusions
- Data Preprossing


**PART 2** contains the steps of building different predictive machine learning models and evaluating them including the following steps:
- Base Models
- Handling Data Imbalance
- Feature Selection
- Hyperparameter Tuning & Cross Validation
- Models Evaluation
- Voting Classifier
- Saving Final Model


Based on this project, I constructed a Voting Classifier based on three models and embedded it in an application you might be inspired by and use it to diagnose yourself: https://heart-disease-diagnosis-app.herokuapp.com/.
<br>
Can you indicate which variables have a significant effect on the likelihood of heart disease?
