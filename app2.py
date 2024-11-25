import numpy as np
import streamlit as st

# Título de la aplicación
st.title("Modelo de Inflación Basado en Conflicto para N Sectores")
st.write("Explora cómo el conflicto entre sectores genera inflación en una economía interconectada.")

# Parámetros iniciales ajustables
st.sidebar.header("Configuración de parámetros")
N = st.sidebar.slider("Número de sectores (N)", 2, 10, 5)  # Número de sectores
n_periodos = st.sidebar.slider("Número de períodos", 10, 200, 100)  # Períodos de simulación
elasticidad = st.sidebar.slider("Elasticidad de demanda", 1.1, 5.0, 1.5)  # Elasticidad
lambda_rate = st.sidebar.slider("Tasa de ajuste de precios (λ)", 0.1, 1.0, 0.5)  # Frecuencia de ajuste
conflicto_base = st.sidebar.slider("Aspiraciones base del conflicto", -1.0, 1.0, 0.2)

# Crear matriz de interdependencia (red insumo-producto)
st.sidebar.subheader("Matriz de interdependencia (M)")
M = np.random.rand(N, N)
for i in range(N):
    M[i] = M[i] / np.sum(M[i])  # Normalizar filas
st.write("Matriz de interdependencia (normalizada):")
st.write(M)

# Inicializar precios, aspiraciones y otros parámetros
precios = np.ones((n_periodos, N))  # Precios iniciales en todos los sectores
aspiraciones = np.full(N, conflicto_base)  # Aspiraciones de cada sector
inflacion_total = []

# Simulación
for t in range(1, n_periodos):
    precios_previos = precios[t - 1].copy()
    if t % 2 == 0:  # Sectores pares ajustan precios
        for i in range(0, N, 2):
            influencia = np.dot(M[i], precios_previos)  # Efecto de otros sectores
            precios[t, i] = precios_previos[i] + lambda_rate * (aspiraciones[i] - influencia)
        precios[t, 1::2] = precios_previos[1::2]  # Sectores impares permanecen iguales
    else:  # Sectores impares ajustan precios
        for i in range(1, N, 2):
            influencia = np.dot(M[i], precios_previos)
            precios[t, i] = precios_previos[i] + lambda_rate * (aspiraciones[i] - influencia)
        precios[t, 0::2] = precios_previos[0::2]  # Sectores pares permanecen iguales
    
    # Inflación promedio en este período
    inflacion_total.append(np.mean(np.diff(precios[:t+1], axis=0), axis=1))

# Gráficos
st.subheader("Evolución de Precios por Sector")
for i in range(N):
    st.line_chart(precios[:, i])

st.subheader("Inflación Total Promedio")
st.line_chart([np.mean(inf) for inf in inflacion_total])

# Conclusión
st.write("El modelo muestra cómo las interdependencias entre sectores y las aspiraciones incompatibles generan inflación sostenida.")
st.write("Puedes experimentar cambiando el tamaño de la matriz, la elasticidad y las tasas de ajuste para observar diferentes dinámicas.")
