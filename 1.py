#Estructura de datos en python
#
# Operaciones de las listas: .append() -> Añadir elementos
#                            .pop() ->    Eliminar
#
# Tuplas -> Lo mismo que las listas pero NO son dinamicas
# Dict -> Almacena informacion en pares de clave-valor
# Set -> Colecciones no ordenadas de elementos unicos

# # Escenario: Una empresa de análisis de datos maneja 
# información de grandes corporaciones tecnológicas 
# (Apple, Samsung, Microsoft, etc.)
# # . Supongamos que debido a una nueva normativa en 
# Estados Unidos, todas las empresas tecnológicas con sede 
# en ese país deben aumentar su número de empleados en un 5%
# si es china un -2%.

import pandas as pd

#Resolucion para la logica del negocio
def actualizar_empleados(row):
    """
    Funcion que evalua la fila y aplica el aumento si cumple la condicion [7].
    """

    if row['Country'] == 'United States':
        return row['Employees'] * 1.05
    elif row['Country'] == 'China':
        return row['Employees'] * 0.2
    return row['Employees']

# Representación de los datos
data = {
    'Revenue': [394.3, 244.2, 282.8, 99.9, 211.9],  # valores de ejemplo (en miles de millones)
    'Employees': [164000, 267000, 190000, 207000, 221000],
    'Country': ['United States', 'South Korea', 'United States', 'China', 'United States']
}

# Creación del DataFrame
df = pd.DataFrame(data, index=['Apple', 'Samsung', 'Alphabet', 'Huawei', 'Microsoft'])

#Se aplica la funcion a todo el dataframe:
df['Employees'] = df.apply(actualizar_empleados, axis=1)

print("Datos originales:")
print(df)