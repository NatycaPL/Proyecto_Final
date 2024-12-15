import sys
from pathlib import Path
import streamlit as st
import plotly.express as px
import pandas as pd
import sqlite3

# Cargar datos desde archivo SQLite
root = Path(__file__).parent.parent
sys.path.append(str(root))
from utils.cargar_datos import *

# Conexión a la base de datos
path_northwind = mapear_datos('Northwind_small', '.sqlite')
dataframes = cargar_datos(path_northwind)

#st.set_page_config(page_title="Clientes", layout="wide")
st.title("Northwind: Ventas por Caregoría")

# Cargar tablas necesarias
order_table = dataframes['Order']
detail_table = dataframes['OrderDetail']
product_table = dataframes['Product']
categories_table = dataframes['Category']

# Convertir 'OrderDate' a formato datetime
order_table['OrderDate'] = pd.to_datetime(order_table['OrderDate'])

# Combinar las tablas necesarias
order_details = detail_table.merge(product_table, left_on='ProductId', right_on='Id',  suffixes=('_detail', '_product'), how='left')
order_details = order_details.merge(categories_table, left_on='CategoryId', right_on='Id', suffixes=('', '_category'), how='left')


# Crear una columna 'TotalVentas' (Quantity * UnitPrice * (1 - Discount))
order_details['TotalVentas'] = (order_details['Quantity'] * order_details['UnitPrice_detail']) * (1 - order_details['Discount'])


# Agrupar las ventas por categoría
ventas_por_categoria = order_details.groupby('CategoryName', as_index=False).agg({'TotalVentas': 'sum'})


# Ordenar el DataFrame por TotalVentas de mayor a menor
ventas_por_categoria = ventas_por_categoria.sort_values(by='TotalVentas', ascending=False)

# Crear el gráfico de barras 
fig_bar = px.bar(
    ventas_por_categoria,
    x='CategoryName',
    y='TotalVentas',
    title='Ventas Totales por Categoría (Ordenado de Mayor a Menor)',
    labels={
        'CategoryName': 'Categoría de Producto',
        'TotalVentas': 'Ventas Totales'
    },
    color='CategoryName', 
    color_discrete_sequence=px.colors.qualitative.Set3  
)


fig_bar.update_layout(
    width=900,
    height=500,
    xaxis_title='Categoría',
    yaxis_title='Ventas Totales'
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_bar)




