import pandas as pd

# 1. Cargar el DataFrame
df = pd.read_csv("./listings.csv")

# 2. Limpiar y convertir la columna 'price' a número
df["price"] = df["price"].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

# 3. Agrupar y calcular la media
promedios = df.groupby("neighbourhood")["price"].mean()
promedios_ordenados = promedios.sort_values(ascending=False)


print(promedios_ordenados)