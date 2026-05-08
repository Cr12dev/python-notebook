# Analisis de datos de tiempo de uso de las redes sociales entre adolescentes
# Sacar que genero utiliza mas las redes sociales
import pandas as pd

df = pd.read_csv('./data/rrss_horas.csv')

df = df.sort_values(by="age", ascending=True)
df.isnull()
df = df.drop(columns=["platform_usage", "daily_social_media_hours", "sleep_hours", "screen_time_before_sleep", "academic_performance", "physical_activity", "social_interaction_level", "stress_level", "anxiety_level", "addiction_level", "depression_label"])

df['nuevo_genero'] = df["gender"]
df['nuevo_genero'] = 0


for i in range(len(df)):
    genero = str(df.loc[i, 'gender']).strip().lower()

    if genero == 'male':
        df.loc[i, 'nuevo_genero'] = 1
    else:
        df.loc[i, 'nuevo_genero'] = 2

def sacar_par(numero: int) -> str:
    if numero % 2 == 0:
        return "Mujeres"
    else:
        return "Hombres"
    
genero_promedio = df['nuevo_genero'].mean()
    

print(df)
print("Edad promedio que utilizan mas las redes sociales:", df['age'].mean())
print("Genero que mas usa", sacar_par(genero_promedio))
