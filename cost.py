import streamlit as st
import pandas as pd

st.title("Predicción de costos por actividad")
st.image("cost.jpeg", caption="Predicción de costos según actividades")

st.header("Descripción de la actividad")

def user_input_features():
    Actividad = st.number_input(
        "Tipo de actividad (1= alimentos/salud, 2= ahorro/inversión, 3= ejercicio, 4= ocio, 5= académico, 6= transporte)",
        min_value=1, max_value=6, step=1
    )

    Personas = st.number_input("Personas involucradas", min_value=1, max_value=100, step=1)

    Tiempo = st.number_input("Tiempo invertido (hrs)", min_value=1, max_value=1000, step=1)

    Momento = st.number_input(
        "Momento del día (1= mañana, 2= tarde, 3= noche)",
        min_value=1, max_value=3, step=1
    )

    user_data = {
        'Tipo de actividad': Actividad,
        'personas': Personas,
        'Tiempo invertido (hrs)': Tiempo,
        'Momento del día': Momento
    }

    features = pd.DataFrame(user_data, index=[0])
    return features

df_user = user_input_features()

df = pd.read_csv("mod.csv", encoding="latin-1")

df = df.dropna()

b0 = 0      
b  = [0, 0, 0, 0]   
pred = (
    b0 +
    b[0] * df_user['Tipo de actividad'][0] +
    b[1] * df_user['personas'][0] +
    b[2] * df_user['Tiempo invertido (hrs)'][0] +
    b[3] * df_user['Momento del día'][0]
)

st.subheader("Predicción del costo ($)")
st.write("El costo estimado es:", round(pred, 2))
