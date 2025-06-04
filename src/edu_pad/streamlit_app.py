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


    # Heatmap
    def make_heatmap(self, input_y, input_x, input_color, input_color_theme):
        st.markdown('#### Ubicacion indicador')
        heatmap = alt.Chart(self.df).mark_rect().encode(
                y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
                x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
                #color=alt.Color(f'max({input_color}):Q',
                                #legend=None,
                                #scale=alt.Scale(scheme=input_color_theme)),
                stroke=alt.value('black'),
                strokeWidth=alt.value(0.25),
            ).properties(width=900
            ).configure_axis(
            labelFontSize=12,
            titleFontSize=12
            ) 
        # height=300
        return heatmap

#with col[1]:
    
    
    #choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
    #st.plotly_chart(choropleth, use_container_width=True)
    
    #heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population')
    #st.altair_chart(heatmap, use_container_width=True)


stramlit_app=Stramlit_app()
stramlit_app.slider_bar()
stramlit_app.make_heatmap('year', 'country')