import pandas as pd

df = pd.DataFrame({
    "modelo": ["iPhone 13", "iPhone 14", "iPhone 12", "iPhone 15"],
    "estado": ["Bueno", "Excelente", "Bueno", "Excelente"],
    "bateria": [85, 96, None, 99],
    "precio": ["$350", "$520", "$280", "$850"],
    "fecha": ["2026-04-16", "2026-05-20", "2026-06-10", "2026-07-01"]
})

# print(df)

print('--------------NUMERO FILAS Y COLUMNAS ----------------')
print(df.shape) # Cuantas columnas y filas tiene el dataset
print('-----------------------TIPOS DE DATOS ----------------')
print(df.dtypes) # Tipos de datos de cada columna
print('--------------------VALORES FALTANTES ----------------')
print(df.isna().sum()) # Cuenta cuantos valores faltantes tiene cada columna.
print('------------------FIN --------------------------------')


# TRANSFORMACION DE DATOS - DE STR A NUMBER

df['precio'] = df["precio"].str.replace('$', '', regex=False)
df["precio"] = pd.to_numeric(df["precio"], errors='coerce')

print(df["precio"])
print(df["precio"].dtype)

# TRANSFORMACION DE DATOS - DE STR A TIMESTAMP

df['fecha'] = pd.to_datetime(df["fecha"], errors='coerce')

print(df["fecha"])
print(df["fecha"].dtype)

# CONVERTIMOS VALORES CATEGORICAS A CATEGORY

df['estado'] = df["estado"].astype('category')

print(df["estado"])
print(df["estado"].dtype)
print(df["estado"].cat.categories)