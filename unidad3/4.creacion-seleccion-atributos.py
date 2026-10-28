# CREACION Y SELECCION DE ATRIBUTOS

# ¿Qué es un atributo?
# Un atributo, también llamado feature o variable, es una característica que describe cada observación.

# En nuestro caso:

# Atributo	        Qué representa
# -------------    ----------------------
# model	            Modelo del iPhone
# price	            Precio de reventa
# battery_health	Salud de la batería
# storage	        Capacidad de almacenamiento
# condition	        Estado del teléfono
# lastUpdated	    Fecha de actualización

# Si queremos construir un modelo que estime el precio de un teléfono, podemos utilizar algunos de esos atributos para predecir price.

# Aquí aparece una distinción fundamental:

# - Atributos de entrada (X): las variables que utilizamos para realizar una predicción.
# - Variable objetivo (y): aquello que queremos predecir, en este ejemplo price.

# ¿Porque queremos crear atributos? FEATURING ENGINEERING
# La creación de atributos consiste en generar nuevas variables a partir de los datos disponibles. No estamos agregando necesariamente información externa: podemos obtener información útil mediante cálculos, combinaciones o transformaciones.

import pandas as pd

df = pd.DataFrame({
    "modelo": ["iPhone 13", "iPhone 14", "iPhone 15"],
    "anio_lanzamiento": [2021, 2022, 2023],
    "battery_health": [85, 96, 78],
    "price": [350, 520, 850]
})

anio_referencia = 2026

df["antiguedad"] = (
    anio_referencia - df["anio_lanzamiento"]
)

print(df)


# Seleccion de atributos

# cuáles de las variables existentes conviene utilizar.

# Imaginá que tenemos 40 columnas. Algunas ayudan a explicar el precio; otras repiten información, contienen identificadores sin valor predictivo o incluso podrían revelar indirectamente la respuesta.

# La selección de atributos busca conservar un conjunto útil de variables y descartar las que no aportan suficiente información.

# Atributo	        Decisión inicial	        Motivo

# battery_health	Conservar	        Puede relacionarse con el precio.

# storage	        Conservar	        La capacidad podría influir en el precio.

# condition	        Conservar	        El estado del teléfono podría ser relevante.

# listing_id	    Investigar	        Un identificador único suele aportar poco por sí solo.

# price	            Usar como objetivo	Es lo que queremos predecir, no una entrada.


df_seleccion = pd.DataFrame({
    "battery_health": [70, 75, 80, 85, 90, 95],
    "storage_gb": [64, 64, 128, 128, 256, 256],
    "antiguedad": [6, 5, 4, 3, 2, 1],
    "price": [180, 230, 320, 400, 620, 800]
})

correlaciones = df_seleccion.corr(numeric_only=True)

print("--------------------------------------------------")
print(correlaciones["price"].sort_values(ascending=False))