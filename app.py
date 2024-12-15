import streamlit as st
import plotly.express as px
import time
import sqlite3
import os


# Estilo personalizado para fondo oscuro
st.markdown(
    """
    :lollipop:
    <style>
    .main {
        background-color: #17153B; /* Fondo negro */
    }
    .title {
        color: #FA7070;
        font-size: 4.6em;
        font-weight: bold;
        text-align: center;  
    }
    .subtitle {
        color: #0A97B0;
        font-size: 1.5em;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .description {
        font-size: 1.1em;
        line-height: 1.6;
        color: #ffffff;
        text-align: justify;
    }
    .info-box {
        background-color: #0A5EB0;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 4px 6px rgba(255, 255, 255, 0.1);
    }
    .info-box p, .info-box li {
        color: #ffffff;
    }
    .stButton>button {
        background-color: #3498db;
        color: #ffffff;
        font-size: 1.1em;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    </style>
    
    """,
    unsafe_allow_html=True
)

# Título del proyecto
st.markdown('<h1 class="title">Proyecto Final Natasha Pineda</h1>', unsafe_allow_html=True)

# Subtítulo con información general
st.markdown('<h2 class="subtitle">Base de datos: Northwind</h2>', unsafe_allow_html=True)

# Descripción principal
st.markdown(
    '''
    :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: 
    :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store: :convenience_store:   
    <div class="description">
        <p>Este proyecto utiliza la base de datos <b>Northwind</b>, la cual contiene información detallada sobre empleados, clientes, pedidos, productos, proveedores, envíos, territorios, y más.</p>
        <p>El objetivo principal es proporcionar una visualización clara y efectiva para entender patrones de ventas, comportamiento de clientes, desempeño de productos y eficiencia de la cadena de suministro.</p>
    </div> 
    ''',
    unsafe_allow_html=True
)


# Crear una caja de información adicional
st.markdown(
    '''
    :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom: :cherry_blossom: :cherry_blossom: :cherry_blossom:
    :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom:  :cherry_blossom: :cherry_blossom: :cherry_blossom: :cherry_blossom: :cherry_blossom:
    <div class="info-box">
        <p><b>¿Qué puedes esperar?</b></p>
        <ul>
            <li>Visualizaciones interactivas y dinámicas.</li>
            <li>Insights clave para la toma de decisiones.</li>
            <li>Un diseño enfocado en la claridad y la estética.</li>
        </ul>
    </div>
    ''',
    unsafe_allow_html=True
)

# Añadir un botón de navegación para que los usuarios continúen
if st.button("Explorar el Proyecto"):
    st.success("¡Vamos a descubrir los datos juntos!")

