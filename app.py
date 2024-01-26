import pickle
import streamlit as st

#LOAD MODEL

wine_model = pickle.load(open('quality_wine.sav', 'rb'))


#JUDUL WEB

st.title('DATA MAINING QUALITY WINE')
st.text('Value Quality Wine Range 1 - 10')

#Membagi Kolom
col1, col2, col3 = st.columns(3)

with col1 :
    fixed_acidity = st.text_input ('Input Value Fixed Acidity')
    volatile_acidity = st.text_input ('Input Value Volatile Acidity')
    citric_acid = st.text_input ('Input Value Ciytic Acid')
    residual_sugar = st.text_input ('Input Value Residual Sugar')
with col2 :
    chlorides = st.text_input ('Input Value Chlorides')
    free_sulfur_dioxide = st.text_input ('Input Value Free Sulfur Dioxxide')
    total_sulfur_dioxide = st.text_input ('Input Value Total Sulfur Dioxxide')
    density = st.text_input ('Input Value Density')
with col3 :
    pH = st.text_input ('Input Value Ph')
    sulphates = st.text_input ('Input Value Sulphates')
    alcohol = st.text_input ('Input Value Alcohol')

#Kode Prediksi

wine_qty = ''

#Button Prediksi

if st.button('Test Quality Wine'):
    wine_qty = wine_model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])

st.success(wine_qty)







