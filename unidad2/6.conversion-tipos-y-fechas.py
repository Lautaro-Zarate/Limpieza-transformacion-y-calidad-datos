import pandas as pd

# Conversion de tipos de datos y fechas
# Primero creamos el DataFrame

df = pd.DataFrame({
    'id': [1,2,3,4,5],
    'fecha': ['2021-01-01', '2021-02-15', '2021-03-20', '2021-04-25', '2021-05-33'],
})

print(df.dtypes) # Mostramos los tipos de datos antes de convertir.

df['fecha'] = pd.to_datetime( # convierte los valores al tipo de dato de fecha y hora.
    df['fecha'],
    errors='coerce' # Si un valor no puede convertirse, lo transforma en NaT, que representa una fecha u hora faltante.
)

print(df)

# ------------------------------------------------------------

# CREACION DE VARIABLES DERIVADAS
# ¿Para que sirve? A veces, la información que necesitamos no está directamente en el dataset, pero podemos calcularla usando columnas existentes.

ventas = pd.DataFrame({
    'product': ['Lays', 'Pepito', 'Oreo', 'Diversión'],
    'unit_price': [5500, 2800, 3000, 4500],
    'transactions': [3, 2, 6, 10]
})

# print(ventas)

# Entonces lo que podemos hacer para crear una columna con el valor total usamos el precio del producto con la cantidad que se compro de cada una.

# Y sería con la siguiente formula:

ventas['total_price'] = ventas['transactions'] * ventas['unit_price'] # CREAMOS LA COLUMNA 'total_price'

print(ventas)

# ¿Por qué es útil?

# Porque ahora podemos responder preguntas que antes requerían cálculos adicionales:

# - ¿Cuánto dinero generó cada transacción?
# - ¿Cuál fue el importe total de las ventas?
# - ¿Qué registros tienen importes negativos o inválidos?