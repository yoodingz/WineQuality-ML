# Wine Quality Prediction

This machine learning project, developed by Group Members:

- Tasya Indri Agustina Dano (210040009)
- Ni Putu Putri Apriliani (210040099)
- Ni Putu Nadya Pramudita (210040114)

## Project Overview

This project focuses on building a machine learning model to predict the quality of wine based on its chemical properties. The primary goal is to enhance the production process and quality control in the winemaking industry. The model, developed using Python and scikit-learn, acts as a tool to assist in assessing wine quality.

## Success Metrics

1. **Accuracy on Test Set:**
   - Overall accuracy of the model on the test set.

2. **High-Quality Wine Identification:**
   - Precision and recall for predicting high-quality wine.

## Failure Metrics

1. **Misclassification of Low-Quality Wine:**
   - Scenario: Model incorrectly classifies low-quality wines as high-quality.

2. **Failure to Identify High-Quality Wine:**
   - Scenario: Model consistently fails to identify high-quality wines.

3. **Model Bias:**
   - Scenario: Model exhibits bias, especially if it disproportionately misclassifies certain types of wines.

4. **Overfitting or Underfitting:**
   - Scenario: Signs of overfitting or underfitting are observed.

5. **Model Drift:**
   - Scenario: Concept drift over time.

## Output Definition

The output values for the wine quality prediction system typically represent the predicted quality of wine based on the input features by the user. in this context, the predicted wine quality is expected to fall within the range of 1 to 10. Each discrete value in this range is an indication of the system's assessment of the quality of the wine, with higher values generally representing better quality.

## Example Output

- Instance 1: Predicted Quality 1 to 3 (Poor Quality)
- Instance 2: Predicted Quality 4 to 6 (Moderate Quality)
- Instance 3: Predicted Quality 7 to 10 (High Quality)

## Methods Without ML

1. **Threshold-Based Rules:**
   - Establish threshold values for key features.

2. **Expert Knowledge Rules:**
   - Leverage expertise to define rules based on known relationships.

3. **Decision Trees or Rule-Based Systems:**
   - Construct decision trees or rule-based systems manually.

## System Architecture (Tech Stack)

- **Programing Language**
   - **Phyton** : the entire application is written in Phyton, as evident from the code syntax and structure.
- **Web Framework**
   - **Streamlit** the web framework used for building the user interface.
- **Model Loading**
   - **Pickle** the pickle module is employed for loading a pre-trained machine learning model. It allows the model stored in the 'quality_wine.sav' file to be loaded back into memory for making predictions.
- **Additional libraries**
   - **scikit-learn** this is a common library for machine learning tasks in Phyton used to train the machine learning model
## Usage Instructions for Wine Quality Data Mining:

1. **After successfully running the Python code in Streamlit, the Wine Quality Data Mining interface will appear.**
2. **Input the required numerical data such as:**
   - fixed acidity,
   - volatile acidity,
   - citric acid,
   - residual sugar,
   - chlorides,
   - free sulfur dioxide,
   - total sulfur dioxide,
   - density,
   - pH,
   - sulphates,
   - and alcohol quality.
3. **Once all the data is entered, click on the "Predict Wine Quality" button. Subsequently, the predicted quality of the inputted wine data will be displayed.**
