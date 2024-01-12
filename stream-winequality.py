import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import MinMaxScaler
import pickle

# Load Dataset
dataset_path = "winequalityN.csv"
df = pd.read_csv(dataset_path)

# Exploratory Data Analysis (EDA)
st.title('Wine Quality App - EDA')

# Display first few rows of the dataset
st.subheader('First Few Rows of the Dataset')
st.dataframe(df.head())

# Display histogram
st.subheader('Histogram')
fig_hist = plt.figure(figsize=(10, 10))
df.hist(bins=25, figsize=(10, 10))
st.pyplot(fig_hist)

# Bar graph to check the influence of alcohol on quality
st.subheader('Bar Graph - Influence of Alcohol on Quality')
fig_bar = plt.figure(figsize=[10, 6])
plt.bar(df['quality'], df['alcohol'], color='red')
plt.xlabel('Quality')
plt.ylabel('Alcohol')
st.pyplot(fig_bar)

# Correlation heatmap
st.subheader('Correlation Heatmap')
fig_heatmap = plt.figure(figsize=[19, 10], facecolor='blue')
sns.heatmap(df.corr(), annot=True)
st.pyplot(fig_heatmap)

# Machine Learning Model
st.title('Wine Quality Prediction Model')

# Drop highly correlated feature
new_df = df.drop('total sulfur dioxide', axis=1)

# Handle null values
new_df.isnull().sum()
new_df.update(new_df.fillna(new_df.mean()))

# Handle categorical variables
next_df = pd.get_dummies(new_df, drop_first=True)

# Create binary classification for quality (1 if quality >= 7, else 0)
next_df['best_quality'] = [1 if x >= 7 else 0 for x in next_df.quality]

# Split dataset
X = next_df.drop(['quality', 'best_quality'], axis=1)
y = next_df['best_quality']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

# Normalize data
norm = MinMaxScaler()
norm_fit = norm.fit(x_train)
new_xtrain = norm_fit.transform(x_train)
new_xtest = norm_fit.transform(x_test)

# Train the model
rnd = RandomForestClassifier(random_state=40)
rnd.fit(new_xtrain, y_train)
y_predict = rnd.predict(new_xtest)

# Model Evaluation
st.title('Model Evaluation')

# Evaluate model
st.subheader('Model Accuracy')
rnd_score = accuracy_score(y_test, y_predict)
st.write(f"Accuracy: {rnd_score}")

st.subheader('Classification Report')
st.text(classification_report(y_test, y_predict))
