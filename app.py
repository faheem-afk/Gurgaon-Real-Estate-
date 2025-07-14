import streamlit as st
import pandas as pd
import pickle 
import numpy as np
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
# from xgboost import XGBRegressor 
# import category_encoders as ce
# from sklearn.compose import ColumnTransformer

st.set_page_config(page_title='viz Demo')

with open('df.pkl', 'rb') as f:
        df = pickle.load(f)
        
st.header('Gurgaon Real Estate Prediction')
property_type = st.selectbox('Property Type', ['flat', 'house'])
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedroom = float(st.selectbox('Bedrooms', sorted(df['bedRoom'].astype('int').unique().tolist())))
bathroom = float(st.selectbox('Bathrooms', sorted(df['bathroom'].astype('int').unique().tolist())))
area = float(st.number_input('Area (sqft)', min_value=0.0))
servant_room = st.selectbox('Servant Room', ['Yes', 'No'])
study_room = st.selectbox('Study Room', ['Yes', 'No'])
luxury_type = st.selectbox('Luxury Type', ['Low', 'Medium', 'High'])

with open('model.pkl', 'rb') as f:
        pipe = pickle.load(f)
        
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

    
    pred = pipe.predict(data)

    pred = np.expm1(pred)[0]
    
    low = round((pred - 0.24), 2)
    high = round((pred + 0.24), 2)
    
    st.text("The price of the {property_type} is between {low} Cr and {high} Cr".format(property_type=property_type, low=low, high=high))

    
