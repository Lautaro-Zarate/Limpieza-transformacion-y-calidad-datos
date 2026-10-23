from sklearn.preprocessing import LabelEncoder
import pandas as pd

# CODIFICAION DE VARIABLES CATEGORICAS: Sirve para representar categorías mediante números para poder analizarlas o utilizarlas en modelos Machine Learning.

# LABEL ENCONDING

# Label enconding asigna un número entero para cada categoría
# ¿Cuándo conviene utilizarlo?

# Es útil cuando las etiquetas tienen un orden real y ese orden está correctamente representado, aunque para variables ordinales también existen codificadores específicos. Para categorías sin orden, como colores o ciudades, hay que tener cuidado: algunos modelos pueden interpretar los números como si existiera una jerarquía.

# Por ejemplo, codificar rojo = 0, azul = 1 y verde = 2 no significa que verde sea mayor que rojo.

# Modelo	    Código
# iPhone 12	    0
# iPhone 13	    1
# iPhone 14	    2
# iPhone 15	    3

df = pd.DataFrame({
    "model_family": ["iPhone 13", "iPhone 14", "iPhone 12","iPhone 15", "iPhone 13"
    ],
    "condition": ["Bueno", "Excelente", "Regular", "Bueno", "Regular"],
    "price": [500, 800, 300, 400, 280]
})

le_model = LabelEncoder()
if "model_family" in df:
    df["model_label"] = le_model.fit_transform(df["model_family"])

print("\n Ejemplo label encoding (model):")
print(dict(zip(le_model.classes_, le_model.transform(le_model.classes_))))
print(df)

# ¿Qué está pasando?
# - LabelEncoder() crea el codificador.
# - fit_transform() aprende las categorías y las convierte en números.
# - classes_ muestra las categorías que encontró.

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

# ONE HOT ENCODING

# Esta tecnica toma una columna categorica y crea una columna por categoría, con valores que indican si cada observacion pertenece a ella. Por ejemplo:

# Estado_Bueno	Estado_Excelente	Estado_Regular
# 1	            0	                0
# 0	            1                   0
# 0	            0	                1
# 1	            0	                0

# Cada fila tiene un 1 en la categoría correspondiente y 0 en las demás.

df_onehot = pd.get_dummies(
    df,
    columns=["condition"],
    prefix="cond"
)

print(df_onehot)

# Fijate en los parámetros:
# - columns=["condition"]: indica qué columna transformar.
# - prefix="cond": define el prefijo de las columnas creadas.

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------


# TARGET ENCODING

# Esta técnica es un poco más interesante porque utiliza información de otra columna: la variable objetivo que queremos analizar o predecir.

# En el práctico, la idea es utilizar 'condition' para calcular el precio promedio de los iPhone en cada estado.

target_encoding = df.groupby("condition")["price"].mean()

df['condition_target'] = df["condition"].map(target_encoding)

print(target_encoding)
print(df)

# Las operaciones principales son:

# - groupby("condition"): agrupa las filas según el estado.
# - ["price"].mean(): calcula el precio promedio de cada grupo.
# - .map(target_encoding): asigna a cada fila el promedio correspondiente a su categoría.