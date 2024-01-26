import pickle
import streamlit as st

# LOAD MODEL
wine_model = pickle.load(open('quality_wine.sav', 'rb'))

# WEB TITLE
st.title('Quality Wine Data Mining')
st.text('Enter values for each feature (Range 1 - 10)')

# COLUMN LAYOUT
col1, col2, col3 = st.columns(3)

# INPUT FIELDS
with col1:
    fixed_acidity = st.text_input('Fixed Acidity')
    volatile_acidity = st.text_input('Volatile Acidity')
    citric_acid = st.text_input('Citric Acid')
    residual_sugar = st.text_input('Residual Sugar')

with col2:
    chlorides = st.text_input('Chlorides')
    free_sulfur_dioxide = st.text_input('Free Sulfur Dioxide')
    total_sulfur_dioxide = st.text_input('Total Sulfur Dioxide')
    density = st.text_input('Density')

with col3:
    pH = st.text_input('pH')
    sulphates = st.text_input('Sulphates')
    alcohol = st.text_input('Alcohol')

# PREDICTION
wine_qty = ''

# PREDICTION BUTTON
if st.button('Predict Wine Quality'):
    wine_qty = wine_model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                                    chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                                    density, pH, sulphates, alcohol]])
    wine_qty = wine_qty[0]  # Extract the predicted value from the array

# DISPLAY PREDICTION
if wine_qty:
    st.success(f'Predicted Wine Quality: {wine_qty}')

# ADDITIONAL INFO AND STYLE
st.info("This app predicts the quality of wine based on input features. Enter values for each feature in the range of 1 to 10.")
st.sidebar.title("About")
st.sidebar.info(
    "This web app is a simple demonstration of predicting wine quality using a machine learning model."
    "The model is trained on a dataset, and you can input values for various features to get a predicted wine quality."
    "Feel free to adjust the input values and see the predictions!"
)

# FOOTER
st.markdown(
    """
    *Note: This is a basic example, and the predictions may not be accurate for real-world scenarios. 
    Always validate the results and consider using a more robust model for production use.*
    """
)








