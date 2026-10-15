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