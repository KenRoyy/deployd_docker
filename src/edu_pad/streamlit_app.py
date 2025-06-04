import streamlit as st
import pandas as pd
import altair as alt
import os
import plotly.express as px
import plotly.graph_objects as go





class Stramlit_app:
    def __init__(self):
        st.set_page_config(page_title="Dashboard Indicadores Financieros",page_icon="📈",initial_sidebar_state="expanded")
        st.title("📈 Dashboard Indicadores Financieros")
        self.ruta_datos="src/edu_pad/static/csv/data_extractor.csv"
        self.df = pd.read_csv(self.ruta_datos)
        self.PLOTLY_AVAILABLE = True

    def slider_bar(self):
        with st.sidebar:
            st.title('📈  Filtro por año')
            year_list = list(self.df.year.unique())[::-1]
            self.selected_year = st.selectbox('Select a year', year_list)
            st.title('📈  Filtro por indicador')
            ind_list = list(self.df.indicador.unique())[::-1]
            self.selected_ind = st.selectbox('Select a year', ind_list)
            #df_selected_year = self.df[self.df.year == selected_year]


    # Heatmap
    def make_world_map(self,input_df):
        """Crea un mapa mundial con los indicadores"""
        try:
            # Prepare data for world map
            map_data = input_df.groupby(['indicador', 'indicator_name', 'country', 'lat', 'lon'])['cerrar'].mean().reset_index()
            
            if self.PLOTLY_AVAILABLE:
                # Use Plotly if available
                fig = go.Figure()
                
                # Add points for each indicator
                for _, row in map_data.iterrows():
                    fig.add_trace(go.Scattergeo(
                        lon=[row['lon']],
                        lat=[row['lat']],
                        text=f"{row['indicator_name']}<br>País: {row['country']}<br>Valor: {row['cerrar']:.2f}",
                        mode='markers+text',
                        marker=dict(
                            size=15,
                            color=row['cerrar'],
                            colorscale='Viridis',
                            showscale=True,
                            colorbar=dict(title="Valor de Cierre"),
                            line=dict(width=1, color='white')
                        ),
                        name=row['indicator_name'],
                        textposition="top center"
                    ))
                
                fig.update_layout(
                    title={
                        'text': 'Ubicación Global de Indicadores Financieros',
                        'x': 0.5,
                        'xanchor': 'center'
                    },
                    geo=dict(
                        projection_type='natural earth',
                        showland=True,
                        landcolor='rgb(243, 243, 243)',
                        coastlinecolor='rgb(204, 204, 204)',
                        showocean=True,
                        oceancolor='rgb(230, 245, 255)',
                        showcountries=True,
                        countrycolor='rgb(204, 204, 204)'
                    ),
                    template='plotly_dark',
                    height=400,
                    showlegend=True
                )
                
                return fig
            else:
                # Use Altair as fallback
                world_chart = alt.Chart(map_data).mark_circle(size=200).encode(
                    longitude='lon:Q',
                    latitude='lat:Q',
                    color=alt.Color('cerrar:Q', 
                                scale=alt.Scale(scheme='viridis'),
                                legend=alt.Legend(title="Valor de Cierre")),
                    size=alt.Size('cerrar:Q', 
                                scale=alt.Scale(range=[100, 400]),
                                legend=alt.Legend(title="Valor")),
                    tooltip=['indicator_name:N', 'country:N', 'cerrar:Q']
                ).resolve_scale(
                    color='independent',
                    size='independent'
                ).properties(
                    width=700,
                    height=400,
                    title="Ubicación de Indicadores Financieros"
                ).project(
                    type='naturalEarth1'
                )
                
                return world_chart
        except Exception as e:
            st.error(f"Error creando mapa: {e}")
            # Simple fallback chart
            return alt.Chart(input_df).mark_circle(size=100).encode(
                x='lon:Q',
                y='lat:Q',
                color='cerrar:Q',
                tooltip=['indicator_name:N', 'cerrar:Q']
            ).properties(width=700, height=400, title="Ubicaciones de Indicadores")

#with col[1]:
    
    
    #choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
    #st.plotly_chart(choropleth, use_container_width=True)
    
    #heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population')
    #st.altair_chart(heatmap, use_container_width=True)


stramlit_app=Stramlit_app()
stramlit_app.slider_bar()
#df_filtrado = stramlit_app.df[stramlit_app.df.year == stramlit_app.selected_year]
#stramlit_app.make_heatmap(df_filtrado)