import streamlit as st
import pandas as pd
import altair as alt
import os





class Stramlit_app:
    def __init__(self):
        st.set_page_config(page_title="Dashboard Indicadores Financieros",page_icon="📈",initial_sidebar_state="expanded")
        st.title("📈 Dashboard Indicadores Financieros")
        self.ruta_datos="src/edu_pad/static/csv/data_extractor.csv"
        self.df = pd.read_csv(self.ruta_datos)

    def slider_bar(self):
        with st.sidebar:
            st.title('📈  Filtro por año')
            year_list = list(self.df.year.unique())[::-1]
            selected_year = st.selectbox('Select a year', year_list)
            st.title('📈  Filtro por indicador')
            ind_list = list(self.df.indicador.unique())[::-1]
            selected_ind = st.selectbox('Select a year', ind_list)
            #df_selected_year = self.df[self.df.year == selected_year]



stramlit_app=Stramlit_app()
stramlit_app.slider_bar()