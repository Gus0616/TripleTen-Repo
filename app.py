import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header("Hola, bienvenido a mi proyecto!")
hist_checkbox = st.checkbox('Construir histograma') # crear un botón
scatter_checkbox = st.checkbox('Construir gráfico de dispersión')

if hist_checkbox: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:
    st.write('Creación de un gráfico de dispersión de odómetro vs precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
