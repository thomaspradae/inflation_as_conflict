import numpy as np
import matplotlib.pyplot as plt
import streamlit as st  # Framework para crear la web app

# Configuración inicial
st.title("Modelo de Inflación Basado en Conflicto")
st.write("Explora cómo el conflicto entre agentes genera inflación en un modelo estilizado.")

# Parámetros iniciales
st.sidebar.header("Configuración de parámetros")
n_periodos = st.sidebar.slider("Número de períodos", 10, 200, 100)  # Número de períodos
precio_inicial = st.sidebar.slider("Precio inicial", 1.0, 5.0, 1.0)  # Precio inicial
elasticidad = st.sidebar.slider("Elasticidad de demanda", 1.1, 5.0, 1.5)  # Elasticidad de demanda

# Función de utilidad (básica para el modelo)
def utilidad(c, c_prima):
    return np.log(c) + np.log(c_prima)

# Función para fijar precios (agente A o B)
def fijar_precio(precio_opuesto, uc, uc_prima, elasticidad):
    # Precio relativo fijado por el agente
    return (1 / (1 - 1 / elasticidad)) * (uc / uc_prima) * precio_opuesto

# Simulación de los precios
precios = np.zeros(n_periodos)
precios[0] = precio_inicial

for t in range(1, n_periodos):
    if t % 2 == 0:  # Agente A fija el precio
        precios[t] = fijar_precio(precios[t - 1], 1, 1, elasticidad)
    else:  # Agente B fija el precio
        precios[t] = fijar_precio(precios[t - 1], 1, 1, elasticidad)

# Cálculo de la inflación
inflacion = np.diff(precios) / precios[:-1]

# Gráficos interactivos
st.subheader("Dinámica de los precios")
st.line_chart(precios, use_container_width=True)

st.subheader("Inflación a lo largo del tiempo")
st.line_chart(inflacion, use_container_width=True)

st.write("El modelo ilustra cómo la dinámica de precios escalonados genera inflación sostenida debido al conflicto.")
