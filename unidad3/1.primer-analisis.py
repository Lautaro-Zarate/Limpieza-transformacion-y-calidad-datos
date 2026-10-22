import pandas as pd

df = pd.DataFrame({
    "modelo": ["iPhone 13", "iPhone 14", "iPhone 12", "iPhone 15"],
    "estado": ["Bueno", "Excelente", "Bueno", "Excelente"],
    "bateria": [85, 96, None, 99],
    "precio": ["$350", "$520", "$280", "$850"]
})

# print(df)

print('--------------NUMERO FILAS Y COLUMNAS ----------------')
print(df.shape) # Cuantas columnas y filas tiene el dataset
print('-----------------------TIPOS DE DATOS ----------------')
print(df.dtypes) # Tipos de datos de cada columna
print('--------------------VALORES FALTANTES ----------------')
print(df.isna().sum()) # Cuenta cuantos valores faltantes tiene cada columna.
print('------------------FIN --------------------------------')
