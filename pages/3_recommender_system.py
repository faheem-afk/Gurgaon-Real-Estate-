import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid

if 'results' in st.session_state:
    pass
else:
    st.session_state['results'] = ''


st.set_page_config("Recommender Appartments")

location_df = pd.read_csv("datasets/location_df.csv")
df = pd.read_excel("datasets/real_estate_data.xlsx")

st.title("Select Landmark and Range")
landmark = st.selectbox('Landmark', sorted(location_df.columns.unique()))
radius = float(st.number_input('Range(Km)', min_value=0.1, max_value=54.0))

if st.button('Search'):
    if radius == 54:
        st.session_state['results'] = location_df[location_df[landmark] < radius][['PropertyName', landmark]].sort_values(by=landmark)
    else:   
        st.session_state['results'] = location_df[location_df[landmark] <= radius][['PropertyName', landmark]].sort_values(by=landmark)

li_property_names = df['PropertyName'].tolist()

final_sim = pd.read_csv('datasets/final_sim.csv').to_numpy()

def recommend_properties_with_finalSimValue(x:str):
    ind = li_property_names.index(x)
    sims = final_sim[ind].tolist()
    numbered_sims = list(enumerate(sims))
    closer = sorted(numbered_sims, key=lambda x: x[1], reverse=True)[1:6]
    indices = []
    for idx, _ in closer:
        indices.append(idx)
    return df[['PropertyName']].loc[indices]


if isinstance(st.session_state['results'], pd.DataFrame) and not st.session_state['results'].empty:
    gb = GridOptionsBuilder.from_dataframe(st.session_state['results'])
    gb.configure_selection('single')  # single row selection
    
    columns = st.session_state['results'].columns.tolist()
    
    gb.configure_column(columns[1], flex=300)
    
    grid_options = gb.build()

    row_height = 35
    
    n_rows = len(st.session_state['results'])
    
    grid_height = max(120, row_height * (n_rows + 1)) 
    grid_response = AgGrid(
        st.session_state['results'],
        gridOptions=grid_options,
        height=grid_height,
        width='100%',
        key="aggrid_1"
    )

    selected = grid_response['selected_rows']

    if selected is not None:    
        st.header("Recommendations")
        prop_name = selected['PropertyName'].values[0]
        similar_props = recommend_properties_with_finalSimValue(prop_name).reset_index(drop=True)
        st.write(similar_props)
        
    