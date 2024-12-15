import sys
from pathlib import Path
import streamlit as st
import plotly.express as px

#Carga de Utils
root = Path(__file__).parent.parent 
sys.path.append(str(root))

from utils.cargar_datos import *

#Carga y procesamiento de los datos
path_northwind = mapear_datos('Northwind_small', '.sqlite')

#st.set_page_config(page_title="Clientes", layout="wide")
st.title("Northwind: Ventas por año")

dataframes = cargar_datos(path_northwind)

order_table = dataframes['Order']
detail_table = dataframes['OrderDetail']
product_table = dataframes['Product'][['Id', 'QuantityPerUnit', 'UnitPrice']]



lista_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

product_table = product_table.loc[product_table['Id'].isin(lista_items)]

#obtener el id de las ordenes
order_region = order_table[order_table['ShipRegion'] == 'North America'][['Id','ShipRegion','OrderDate']]

#Obtener la informacion de cada orden.
order_info = order_region.merge(detail_table, left_on= 'Id', right_on= 'OrderId')

#Obtener las columnas para el primer gráfico
order_info_2 = order_info[['OrderId', 'OrderDate','ShipRegion', 'UnitPrice', 'Quantity','Discount']]

#Crear una columna 'Total de ventas' (Quantity * UnitPrice - Discount)
order_info_2['TotalVentas'] = (order_info_2['Quantity'] * order_info_2['UnitPrice']) * (1 - order_info_2['Discount'])

#Agrupar el 'TotalVentas' por las columnas de fecha y orden 
order_info_agrupada = order_info_2.groupby(['OrderId', 'OrderDate'], as_index=False).agg({'TotalVentas':'sum'})

#Crear el gráfico de líneas
fig = px.line(
    order_info_agrupada,
    x='OrderDate',
    y='TotalVentas',
    markers=True,
    title='Ventas Totales en el tiempo',
    labels={
        'OrderDate':'Fecha de la orden',
        'TotalVentas': 'Ventas Totales'
    }
)

fig.update_traces(line_color='#48B5E0')

#Ajustar el tamaño del gráfico
fig.update_layout(
    width=900,
    height=500
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)