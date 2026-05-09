import pandas as pd

class DataMain:
    def __init__(self):
        self.df = pd.read_csv("./data/2.csv")
        self.df = self.df.dropna()
        print("Columnas del CSV:", self.df.columns) 

    def felicidad_score(self):
        col = "happiness_score"
        country_col = "country" 

        if col not in self.df.columns:
            raise ValueError(f"La columna '{col}' no existe en el dataset")

        # Estadísticas
        media = float(self.df[col].mean())
        minimo = float(self.df[col].min())
        maximo = float(self.df[col].max())
        desviacion = float(self.df[col].std())

        # País con menor felicidad
        pais_min = self.df.loc[self.df[col].idxmin(), country_col]

        # País con mayor felicidad
        pais_max = self.df.loc[self.df[col].idxmax(), country_col]

        # España
        pais_spain = self.df[self.df["country"] == "Spain"]
        media_spain = float(pais_spain[col].mean())
        

        return {
            "media": media,
            "min": minimo,
            "max": maximo,
            "desviacion": desviacion,
            "Indice de menos felicidad": pais_min,
            "Indice de mas felicidad": pais_max,
            "Indice de España": media_spain
        }


if __name__ == "__main__":
    data = DataMain()
    print(data.df.head())              
    print(data.felicidad_score())
