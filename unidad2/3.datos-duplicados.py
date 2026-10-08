import pandas as pd

# COMO MANEJAR DATOS DUPLICADOS?

# En este ejemplo, vamos a ver cómo manejar datos duplicados en un DataFrame de pandas. Los datos duplicados pueden surgir por diversas razones, como errores de entrada de datos o combinaciones de múltiples fuentes de datos. Es importante identificar y manejar estos duplicados para asegurar la calidad de los datos.

# Primero, vamos a crear un DataFrame de ejemplo con algunos datos duplicados:

df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Laura', 'Ana', 'Juan'],
    'Edad': [25, 31, 29, 28, 25, 31],
    'Salario': [80000, 90000, 95000, 72000, 80000, 90000]
})

datosDuplicados = df[df.duplicated()] # Esto nos muestra las filas duplicadas en el DF. 

print(datosDuplicados)

# Y despues dropeamos los duplicados con drop_duplicates().

df_sin_duplicados = df.drop_duplicates() # Esto elimina las filas duplicadas del DataFrame.

print(df_sin_duplicados)

# Pero OJO, que haya dos datos iguales no significa que sean duplicados, ya que pueden ser registros diferentes de dos personas con el mismo nombre y salario. Por eso es importante analizar el contexto de los datos antes de decidir eliminar duplicados.


# ------------------------------------------------------------

# ERRORES DE CODIFICACION E INCONSISTENCIA CATEGORICAS

# Estos problemas pueden aparecer cuando los datos provienen de diferentes fuentes o cuando se ingresan manualmente. Por ejemplo: 

# [Buenos Aires, buenos aires, Buenos aires, buenos Aires] ----> Esto es un problema de inconsistencia en la codificación de la variable categórica "Ciudad".

df = pd.DataFrame({
    'Ciudad': ['Buenos Aires', 'buenos aires', 'Buenos aires', 'buenos Aires', 'Córdoba', 'cordoba'],
    'Poblacion': [3000000, 3000000, 3000000, 3000000, 1500000, 1500000]
})

categorias = df['Ciudad'].unique() # Esto nos muestra los valores unicos de la columna, lo que nos permite revisar categorias existentes. 

print(categorias)

# Entonces hacemos la normalizacion de los datos.

df['Ciudad'] = (
    df['Ciudad']
    .str.strip() # Elimina espacios al inicio y final
    .str.lower() # Estandariza a minusculas
)

ciudades = df['Ciudad'].unique()
print(ciudades)

# Para corregir errores manualmente se hace de la siguiente manera:

df['Ciudad'] = df['Ciudad'].replace({
    'córdoba' : 'cordoba'
})

ciudades2 = df['Ciudad'].unique()
print(ciudades2)