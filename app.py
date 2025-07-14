import streamlit as st
import pandas as pd
import pickle 
import numpy as np

st.set_page_config(page_title='viz Demo')

with open('df.pkl', 'rb') as f:
    df = pickle.load(f)

st.header('Gurgaon Real Estate Prediction')
property_type = st.selectbox('Property Type', ['flat', 'house'])
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedroom = float(st.selectbox('Bedrooms', sorted(df['bedRoom'].astype('int').unique().tolist())))
bathroom = float(st.selectbox('Bathrooms', sorted(df['bathroom'].astype('int').unique().tolist())))
area = float(st.selectbox('Area (sqft)', sorted(df['builtUpArea'].unique().tolist())))
servant_room = st.selectbox('Servant Room', ['Yes', 'No'])
study_room = st.selectbox('Study Room', ['Yes', 'No'])
luxury_type = st.selectbox('Luxury Type', ['Low', 'Medium', 'High'])

with open('model.pkl', 'rb') as f:
    pipeline = pickle.load(f)

if st.button('Predict'):
    
    data  = pd.DataFrame({
    'sector':[sector],
    'property_type':[property_type],
    'bedRoom':[bedroom],
    'bathroom':[bathroom],
    'builtUpArea':[area],
    'servant room':[servant_room],
    'study room':[study_room],
    'luxury_category':[luxury_type]
    })

    pred = pipeline.predict(data)

    pred = str(round(np.expm1(pred)[0], 2)) + 'cr'
    
    st.text(pred)

    
