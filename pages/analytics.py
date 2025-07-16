import seaborn as sns
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

fig.update_layout(
    coloraxis_colorbar=dict(
        x=.97,         
        xanchor="left",
        len=0.75,       
        thickness=15    
    ),
    margin=dict(l=0, r=80, t=50, b=20)  
)

st.plotly_chart(fig, use_container_width=True)


st.header('Feature Cloud')
word_cloud_df = pd.read_csv("datasets/word_cloud_df.csv")
sector = st.selectbox('Sector', sorted(word_cloud_df['sector'].unique()))
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
property_type = st.selectbox('property_type', ['flat', 'house'])
df = pd.read_csv('datasets/gurgaon_properties_missing_value_imputed.csv')
viz_df = df[df['property_type'] == property_type]
fig = px.scatter(viz_df, x="builtUpArea", y='price', color='bedRoom', height=500)
st.plotly_chart(fig)


st.header("BHK percentage per sector")
sector = st.selectbox('Sector', ['Overall'] + sorted(df['sector'].unique()), key="sector_1_selector")
if sector == "Overall":
    fig = px.pie(df, names='bedRoom')
else:
    pie_df = df[df['sector'] == sector]
    fig = px.pie(pie_df, names='bedRoom')

st.plotly_chart(fig, use_container_width=True)


st.header("Price variation per BHK")
sector = st.selectbox('Sector', ['Overall'] + sorted(df['sector'].unique(), key="sector_2_selector"))
if sector == "Overall":
    temp_df = df[df['bedRoom'] <= 4]
else:
    sector_specific_df = df[df['sector'] == sector]
    temp_df = sector_specific_df[sector_specific_df['bedRoom'] <= 4]
fig = px.box(temp_df, x='bedRoom', y='price')
st.plotly_chart(fig, use_container_width=True)



st.header("Price Distribution")
fig = plt.figure(figsize=(6, 4))
sns.histplot(data=df[df['property_type'] == 'house'], x='price', color='blue', label='House', kde=True, stat='density', alpha=0.5)
sns.histplot(data=df[df['property_type'] == 'flat'], x='price', color='orange', label='Flat', kde=True, stat='density', alpha=0.5)
plt.legend()
st.pyplot(fig)