import pandas as pd
import streamlit as st

# Creacion de la UI
st.title("""
    Valencia Neighbourhood Airbnb scraping
""")

file_uploader = st.file_uploader("Choose a CSV file")
# Para mejorar la forma automatica
url_uploader = st.text_input("Upload via URL")

if file_uploader is not None or url_uploader:

    # 1. Cargar el DataFrame
    if file_uploader is not None:
        df = pd.read_csv(file_uploader)
    else:
        df = pd.read_csv(url_uploader)

    # 2. Limpiar y convertir la columna 'price' a número
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # 3. Agrupar y calcular la media
    promedios = df.groupby("neighbourhood")["price"].mean()
    promedios_ordenados = promedios.sort_values(ascending=False)

    st.write("Analyze all Airbnb data for the city of Valencia")
    st.bar_chart(promedios_ordenados)

else:
    st.write("Error: insert a valid file or URL")