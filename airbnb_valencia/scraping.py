import pandas as pd
import streamlit as st

# Creacion de la UI
st.title("""
    Valencia Neighbourhood Airbnb scraping
""")

file_uploader = st.file_uploader("Choose a CSV file")

if file_uploader is not None:
    # 1. Cargar el DataFrame desde el archivo subido
    df = pd.read_csv(file_uploader)

    # 2. Limpiar y convertir la columna 'price' a número
    df["price"] = (
        df["price"]
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
        .astype(float)
    )

    # 3. Agrupar y calcular la media
    promedios = df.groupby("neighbourhood")["price"].mean()
    promedios_ordenados = promedios.sort_values(ascending=False)

    st.write("Analyze all Airbnb data for the city of Valencia")
    st.line_chart(promedios_ordenados)

else:
    st.write("Error: insert a valid file")