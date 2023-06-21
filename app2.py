import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

APP_TITLE = 'Mapeamento de ocorrencias'
#APP_SUBTITLE = 'Source: Federal Trade Comission'

  

    
def display_map(df_ocorrencias):
    

    map = folium.Map(location=[-23.5205087,-46.1869589], zoom_start=10.5,scrollWheelZoom = False)
    
    choroplet = folium.Choropleth(
        geo_data='dados/abairramento.geojson',
         key_on='feature.properties.name',
        line_opacity=0.8,
        highlight=True
        )
    choroplet.geojson.add_to(map)
    choroplet.geojson.add_child(
        folium.GeoJsonTooltip(['NOME','DISTRITO'],labels=False)
    )
    #folium.Marker(location=[0,0],

     #             tooltip="Clique aqui",
     #             icon=folium.Icon(color="green")
     #             ).add_to(map)
    tipo = df_ocorrencias['RUBRICA']
    lat = df_ocorrencias['LATITUDE']
    ltg = df_ocorrencias['LONGITUDE']

    for t, la, lo in zip (tipo, lat, ltg):
        folium.Marker(
            [la,lo],
            tooltip=t,
            icon=folium.Icon(color="red",icon_color="white",icon='info-sign')    
            ).add_to(map)
             
    st_map = st_folium(map, width=800, height=600)



    
    

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    
        

#    """ #Carregando dados

    df_ocorrencias = pd.read_csv('dados/ocorrencias_mogi.csv')
    df_ocorrencias = df_ocorrencias.dropna(subset=['LATITUDE'])
    df_ocorrencias['LATITUDE'] = df_ocorrencias['LATITUDE'].str.replace(',', '.')
    df_ocorrencias['LONGITUDE'] = df_ocorrencias['LONGITUDE'].str.replace(',', '.')
    df_ocorrencias['COORDENADAS'] = df_ocorrencias['LATITUDE'].astype(str) + ', ' + df_ocorrencias['LONGITUDE'].astype(str)

  #  df_loss = pd.read_csv('data/AxS-Losses Box_Full Data_data.csv')
   # df_median = pd.read_csv('data/AxS-Median Box_Full Data_data.csv')
   # df_continental = pd.read_csv('data/AxS-Continental_Full Data_data.csv')

   # year = 2022
    #quarter = 1
    #state_name = ''
   # report_type = 'Fraud' """
    
    
    
    year_list = list(df_ocorrencias['ANO_BO'].unique())
    year = st.sidebar.selectbox('Ano', year_list)

    bairro_list = list(df_ocorrencias['BAIRRO'].unique())
    bairro = st.sidebar.selectbox('Bairro',bairro_list)

    display_map(df_ocorrencias)

    st.write(df_ocorrencias.shape)   
    st.write(df_ocorrencias)
    st.write(df_ocorrencias.columns)






if __name__ == "__main__":
    main()