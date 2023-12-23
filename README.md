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

The output is a binary prediction indicating whether a given wine is of high or low quality.

## Example Output

- Instance 1: Predicted Quality - 1 (High Quality)
- Instance 2: Predicted Quality - 0 (Low Quality)
- ...

## Methods Without ML

1. **Threshold-Based Rules:**
   - Establish threshold values for key features.

2. **Expert Knowledge Rules:**
   - Leverage expertise to define rules based on known relationships.

3. **Decision Trees or Rule-Based Systems:**
   - Construct decision trees or rule-based systems manually.

## System Architecture (Tech Stack)

- **Programming Language:** Python
- **Libraries:** pandas, scikit-learn
- **Model:** RandomForestClassifier
- **Documentation:** Jupyter Notebook
- **Version Control:** GitHub
