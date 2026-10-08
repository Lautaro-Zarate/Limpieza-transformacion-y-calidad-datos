import pandas as pd

# TRANSFORMACION DE DATOS

# En esta sección vamos a ver cómo transformar los datos para que sean más útiles para el análisis. La transformación de datos puede incluir la normalización, estandarización, creación de nuevas variables, entre otros.

df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Laura'],
    'Edad': [25, 31, 29, 28],
    'Salario': ['80000 USD', '90000 USD', '95000 USD', '72000 USD']
})

# En este caso no podemos trabajar con la columna "salario" porque el tipo de dato es un string y no un número. Por esa razon tenemos que transformarla. O crear una columna nueva con el tipo de dato correcto.

df['salario_numerico'] = (
    df['Salario']
    .replace('[^\d.]', '', regex=True) # Esto reemplaza todo lo que no sea un número o un punto por una cadena vacía, dejando solo los números y los puntos decimales.
    .str.extract('(\d+)')
    .astype(float)
)

salario = df['salario_numerico']
print(salario)
