import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="Analytics page", layout='centered', )
st.header("Sector Price per Sqft Geomap")
group_df = pd.read_csv("datasets/group_df.csv")
fig = px.scatter_mapbox(group_df, lat='latitude', lon='longitude', color='price_per_sqft', size='builtUpArea', 
                color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                mapbox_style="open-street-map", width=1200, height=600, hover_name=group_df.index)
st.plotly_chart(fig, use_container_width=True)


st.header('Feature Cloud')
word_cloud_df = pd.read_csv("datasets/word_cloud_df.csv")
sector = st.selectbox('📍 Sector', sorted(word_cloud_df['sector'].unique().tolist()))
feature_text = []
for i in word_cloud_df[word_cloud_df['sector'] == sector]['features'].values:
    feature_text += map(lambda x: x.replace("\'", ""), i.replace("[", "",).replace("]", "").split(","))
feature_text = ' '.join(feature_text)
plt.rcParams["font.family"] = "Arial"
wordcloud = WordCloud(width = 800, height = 500,background_color='white',stopwords=set(['s']),min_font_size = 10).generate(feature_text)
fig = plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')                    
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)


st.header("Area Vs Price")
property_type = st.selectbox('🏠 property_type', ['flat', 'house'])
df = pd.read_csv('datasets/gurgaon_properties_missing_value_imputed.csv')
viz_df = df[df['property_type'] == property_type]
fig = px.scatter(viz_df, x="builtUpArea", y='price', color='bedRoom', height=500)
st.plotly_chart(fig)


st.header("BHK percentage per sector")
sector = st.selectbox('📍 Sector', ['Overall'] + sorted(df['sector'].unique()))
if sector == "Overall":
    fig = px.pie(df, names='bedRoom')
else:
    pie_df = df[df['sector'] == sector]
    fig = px.pie(pie_df, names='bedRoom')

st.plotly_chart(fig, use_container_width=True)
