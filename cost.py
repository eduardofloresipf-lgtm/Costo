import streamlit as st
import pandas as pd

st.image("cost.jpeg", caption="Predicción del costo según la actividad", use_column_width=True)

st.title("Predicción del costo ($)")
st.header("Descripción de la actividad")

b0 = -24.896049312395917
b = [9.14496336, 88.81719839, 36.34086094, 42.5256678]

tipo = st.number_input(
    "Tipo de actividad (1= alimentos/salud, 2= ahorro/inversión, 3= ejercicio, 4= ocio, 5= académico, 6= transporte)",
    min_value=1, max_value=6, step=1
)

personas = st.number_input(
    "Personas involucradas",
    min_value=1, max_value=50, step=1
)

tiempo = st.number_input(
    "Tiempo invertido (hrs)",
    min_value=0.0, max_value=24.0, step=0.5
)

momento = st.number_input(
    "Momento del día (1= mañana, 2= tarde, 3= noche)",
    min_value=1, max_value=3, step=1
)

if st.button("Calcular costo estimado"):
    pred = (
        b0
        + b[0] * tipo
        + b[1] * personas
        + b[2] * tiempo
        + b[3] * momento
    )

    st.subheader("Predicción del costo ($)")
    st.write(round(pred, 2))

