
import pandas as pd
import plotly.graph_objects as go   # Importación de plotly.graph_objects como go
import streamlit as st
 
# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')
 
# Encabezado principal de la aplicación
st.header('Análisis de Anuncios de Venta de Coches')
 
st.write('Explora el conjunto de datos de vehículos en venta en EE. UU. '
         'Utiliza los botones para generar visualizaciones interactivas.')
 
# ── Botón 1: Histograma ──────────────────────────────────────────────────────
hist_button = st.button('Construir histograma')
 
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
 
    # Crear un histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
 
    # Añadir título al gráfico
    fig.update_layout(title_text='Distribución del Odómetro')
 
    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
 
# ── Botón 2: Gráfico de dispersión ──────────────────────────────────────────
scatter_button = st.button('Construir gráfico de dispersión')
 
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
 
    # Crear un scatter plot utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    )])
 
    # Añadir título al gráfico
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
 
    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)