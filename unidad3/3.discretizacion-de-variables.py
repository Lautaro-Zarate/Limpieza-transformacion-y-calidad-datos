import pandas as pd

# DISCRETIZACION DE VARIABLES NUMERICAS

# La discretización es una tecnica que consiste en transformar una variable numerica continua o con muchos valores en un conjunto de intervalos o categorías.

# ¿Para qué sirve?
# Imaginá que tenemos estos precios de reventa:

# Modelo	    Precio
# iPhone 11	    180
# iPhone 12	    280
# iPhone 13	    350
# iPhone 14	    520
# iPhone 15	    850
# iPhone 16	    1.100


# El precio es una variable numérica. Podemos transformarla en una variable categórica:

# Precio	    Categoría
# 180	        Económico
# 280	        Económico
# 350	        Intermedio
# 520	        Intermedio
# 850	        Premium
# 1.100	        Premium

# ¿Como definimos intervalos? Con pd.cut() establecemos los límites de los intervalos. Es decir, decidimos cómo dividir el rango de valores.


df = pd.DataFrame({
    "modelo":  ["iPhone 11", "iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15", "iPhone 16"],
    "precio": [180, 250, 350, 520, 850, 1100]
})

limites = [0, 400, 700, 1500]
etiquetas = ['Económico', 'Intermedio', 'Premium']

df['categoria_precio'] = pd.cut(
    df['precio'],
    bins = limites, # Establecemos los intervalos
    labels = etiquetas, # Los nombres para cada intervalo
    include_lowest = True # Incluye el valor mínimo del rango en el primer intervalo.
)

print(df)
print('------------------------------------------')
print('------------------------------------------')



# DIVIDIR SEGUN CUARTILES, con pd.qcut() los limites se calculan a partir de las distribuciones de los datos, intentando que cada grupo tenga una cantidad similar de observaciones.

df['grupo_precio'] = pd.qcut(
    df["precio"],
    q = 3,
    labels = ['Bajo', 'Medio', 'Alto']
)

print(df[['precio', 'grupo_precio']])