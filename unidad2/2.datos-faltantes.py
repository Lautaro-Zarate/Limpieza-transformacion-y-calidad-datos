# Manejo de datos faltantes

# Para detectar faltantes en Pandas, se usa df.isnull().sum().

# Esto nos dice cuantos valores faltantes/nulos tenemos en cada columna del DataFrame.

#¿Por qué hacemos esto antes de decidir qué hacer? -----> Porque necesitamos conocer la magnitud del problema.


# --------------------------------------------------------------


# 1.Primera estrategia para tratar con datos faltantes: ELIMINAR filas o columnas con datos faltantes. 

# df.drop = df.dropna() ----> Elimina filas con datos faltantes.

# Antes 
# Ana     25    800000
# Juan    31    NaN
# Pedro   NaN   950000
# Laura   28    720000

# Después
# Ana     25    800000
# Laura   28    720000


# En este caso tenemos que entender que estamos perdiendo información importante, por eso dropna() puede ser una solucion sencilla pero no siempre deberíamos utilizarla automaticamente o como primera opción.


# 2. Segunda estrategia: IMPUTAR. Reemplazar valores faltantes con un valor calculado por un valor estimado.

# IMPUTACION SIMPLE: Reemplazar los valores faltantes con un valor constante, como la media, mediana o moda de la columna.

# df['unit_price'].fillna(
#     df['unit_price'].mean(),
#     inplace=True
# )

# Cuidado con reemplazar con la media o moda, ya que si tenemos muchos valores faltantes o valores atípicos, esto puede sesgar los resultados. Por eso es importante analizar la distribución de los datos antes de decidir qué estrategia de imputación utilizar.

# 3. Tercera estrategia: IMPUTACION MULTIPLE: Reemplazar los valores faltantes con un valor estimado basado en otras variables del dataset.

# Importando ""from sklearn.experimental import enable_iterative_imputer" y "from sklearn.impute import IterativeImputer"

# Esto nos permite usar el IterativeImputer, que es un método más avanzado para imputar valores faltantes. Este método utiliza un modelo de regresión para predecir los valores faltantes basándose en otras variables del dataset.


## ¿QUE TENER EN CUENTA ANTES DE APLICAR CUALQUIER ESTRATEGIA?


#                    Encontré valores faltantes
#                               ↓
#                          ¿Cuántos hay?
#                               ↓
#                       ¿En qué columnas?
#                               ↓
#                     ¿Qué tipo de variable es?
#                               ↓
#                     ¿Por qué podrían faltar?
#                               ↓
#                           ¿Eliminar?
#                           ¿Imputar?
#                       ¿Con qué estrategia?
#                               ↓
#                     ¿Puede mi decisión introducir sesgo?