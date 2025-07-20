import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid
from utils import recommend_properties_with_finalSimValue, get_hash

if 'results' in st.session_state:
    pass
else:
    st.session_state['results'] = ''

st.set_page_config("Recommender Appartments")

location_df = pd.read_csv("datasets/location_df.csv")

st.title("Select Landmark and Range")
landmark = st.selectbox('Landmark', sorted(location_df.columns.unique()))
radius = float(st.number_input('Range(Km)', min_value=0.1, max_value=54.0))


if st.button('Search'):
    if radius == 54:
        st.session_state['results'] = location_df[location_df[landmark] < radius][['PropertyName', landmark]].sort_values(by=landmark)
        if len(st.session_state['results']) > 0:
            st.session_state['trigger'] = True
            pass
        else:
            st.write("No such Property!")
    else:   
        st.session_state['results'] = location_df[location_df[landmark] <= radius][['PropertyName', landmark]].sort_values(by=landmark)
        if len(st.session_state['results']) > 0:
            st.session_state['trigger'] = True
            pass
        else:
            st.write("No such Property!")

if isinstance(st.session_state['results'], pd.DataFrame) \
    and not isinstance(st.session_state['results'], str):
    
    dynamic_key = f"aggrid_{get_hash(st.session_state['results'])}"

    gb = GridOptionsBuilder.from_dataframe(st.session_state['results'])
    gb.configure_selection('single')  
    
    columns = st.session_state['results'].columns.tolist()
    
    gb.configure_column(columns[1], flex=3)
    
    grid_options = gb.build()

    row_height = 35
    
    n_rows = len(st.session_state['results'])
    
    grid_height = max(120, row_height * (n_rows + 1)) 
    
    grid_response = AgGrid(
        st.session_state['results'],
        gridOptions=grid_options,
        height=grid_height,
        width='100%',
        key=dynamic_key
    )

    selected = grid_response['selected_rows']
    
    if selected is not None :    
        st.header("Recommendations")
        prop_name = selected['PropertyName'].values[0]
        similar_props = recommend_properties_with_finalSimValue(prop_name).reset_index(drop=True)
        st.write(similar_props)
        
            
        
        
        
        
        
        
        
        