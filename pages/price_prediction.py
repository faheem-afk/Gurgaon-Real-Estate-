import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title='Gurgaon Property Price Predictor', layout="centered")

# Session state for result
if 'result' not in st.session_state:
    st.session_state.result = ''

# Load data & model
df = pd.read_csv('df.csv')
pipeline = joblib.load('model.joblib')


# Title section
st.markdown("<h1 style='text-align: center; color: #2e8b57;'>🏙️ Gurgaon Property Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Enter property details to predict a real estate price range in ₹ Cr.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input layout using columns
col1, col2 = st.columns(2)

with col1:
    property_type = st.selectbox('🏠 Property Type', ['flat', 'house'])
    bedroom = float(st.selectbox('🛏️ Bedrooms', sorted(df['bedRoom'].astype('int').unique().tolist())))
    servant_room = st.selectbox('🧑‍🍳 Servant Room', ['Yes', 'No'])
    luxury_type = st.selectbox('💎 Luxury Category', ['Low', 'Medium', 'High'])

with col2:
    sector = st.selectbox('📍 Sector', sorted(df['sector'].unique().tolist()))
    bathroom = float(st.selectbox('🛁 Bathrooms', sorted(df['bathroom'].astype('int').unique().tolist())))
    study_room = st.selectbox('📚 Study Room', ['Yes', 'No'])
    area = float(st.number_input('📐 Built-Up Area (sqft)', min_value=0.0))

st.markdown("")

# Predict button
if st.button('🔮 Predict Price'):
    data = pd.DataFrame({
        'sector': [sector],
        'property_type': [property_type],
        'bedRoom': [bedroom],
        'bathroom': [bathroom],
        'builtUpArea': [area],
        'servant room': [servant_room],
        'study room': [study_room],
        'luxury_category': [luxury_type]
    })

    pred = pipeline.predict(data)
    pred = np.expm1(pred)[0]
    low = round(pred - 0.24, 2)
    high = round(pred + 0.24, 2)

    st.session_state.result = f"💰 The predicted price for the **{property_type}** is between **₹{low} Cr** and **₹{high} Cr**."

# Show result persistently
if st.session_state.result:
    st.success(st.session_state.result)