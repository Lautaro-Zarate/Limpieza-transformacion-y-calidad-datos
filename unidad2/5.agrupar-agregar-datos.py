import pandas as pd

# Para agregar y agregar datos en un DataFrame de pandas, podemos utilizar las funciones `groupby()` y `agg()`. A continuación, se muestra un ejemplo de cómo hacerlo:

# Supongamos que tenemos puestos de trabajos con sus sueldos correspondientes y queremos agruparlos por el nombre del puesto y calcular el salario promedio, máximo y mínimo para cada puesto.

df = pd.DataFrame({
    'Puesto': ['Ingeniero', 'Ingeniero', 'Abogado', 'Abogado', 'Gerente', 'Gerente', 'Administrativo'],
    'Salario': [50000, 60000, 40000, 55000, 80000, 100000, 48000] 
})

df_grouped = (df
    .groupby('Puesto')['Salario'] 
    .agg(['mean', 'max', 'count'])
    .reset_index()
)

print(df_grouped)

# Veamos qué hace cada parte:

# groupby('Puesto'): agrupa las filas según el nombre del puesto.

# ['Salario']: selecciona la columna sobre la que queremos calcular estadísticas.

# .agg(['mean', 'max', 'count']): calcula la media, el máximo y la cantidad de registros de cada grupo.

# .reset_index(): vuelve a convertir el nombre del puesto en una columna normal del DataFrame resultante.

# Una vez que tengamos el dataset con reemplazos, no valores nulos, no duplicados y sin inconsistencias. Podemos exportar el DataFrame resultante a un archivo CSV para su posterior análisis o uso. Esto se puede hacer utilizando el método `to_csv()` de pandas.

df_grouped.to_csv(
    'salarios_agrupados.csv',  # Nombre del archivo CSV de salida
    index = False # Evita que se escriba el índice del DataFrame en el archivo CSV
)
