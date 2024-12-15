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

# Configuración de la página
st.set_page_config(page_title="Empleados", layout="wide")
st.title("Northwind: Ventas por Empleado")

# Cargar tablas necesarias
order_table = dataframes['Order']
details_table = dataframes['OrderDetail']
products_table = dataframes['Product']
category_table = dataframes['Category']
employee_table = dataframes['Employee']

# Convertir 'OrderDate' a formato datetime 
order_table['OrderDate'] = pd.to_datetime(order_table['OrderDate'])

# Crear columnas de años
order_table['Year'] = order_table['OrderDate'].dt.year


# Crear un filtro para los años disponibles
años_disponibles = sorted(order_table['Year'].unique())

# Widget para seleccionar un solo año
año_seleccionado = st.sidebar.selectbox(
    "Seleccione el año de interés",
    options=años_disponibles,
    index=0
)

# Crear segmentador por empleado
empleados_disponibles = employee_table['FirstName'].unique()


empleado_seleccionado = st.sidebar.multiselect(
    "Seleccione el o los empleados de interés",
    options=empleados_disponibles,
    default=empleados_disponibles
)

# Crear la máscara de filtrado
mascara = (
    (employee_table['FirstName'].isin(empleado_seleccionado)) &
    (order_table['Year'] == año_seleccionado)
)

empleados_filtrados = employee_table[mascara][['Id', 'FirstName']]

# Combinar con la tabla de detalles order 
info_empleados = empleados_filtrados.merge(order_table, left_on='Id', right_on='EmployeeId', suffixes=('_order', '_Id'), how='left')


# Unir con OrderDetail
info_empleados_details = info_empleados.merge(
    details_table,
    left_on='Id_Id',
    right_on='OrderId',
    how='inner'
)

# Seleccionar culumnas
result = info_empleados_details[['FirstName', 'UnitPrice', 'Quantity', 'Discount']]


# Calcular el precio final
info_empleados_details['Precio_Final'] = ((info_empleados_details['Quantity'] * info_empleados_details['UnitPrice'])) * (1 - info_empleados_details['Discount'])



# Agrupar por empleado y calcular la suma del precio final
info_empleados_agrupada = info_empleados_details.groupby(['FirstName'], as_index=False).agg({'Precio_Final': 'sum'})


# Ordenar el DataFrame de mayor a menor por Precio_Final
info_empleados_agrupada = info_empleados_agrupada.sort_values(by='Precio_Final', ascending=False)

# Crear el gráfico de barras 
fig_bar = px.bar(
    info_empleados_agrupada,
    x='FirstName',
    y='Precio_Final',
    color='FirstName',  
    title='Ventas totales por empleado',
    labels={
        'FirstName': 'Empleado', 
        'Precio_Final': 'Precio Final'
    },
    color_discrete_sequence=px.colors.qualitative.Set3 
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig_bar)



