import pandas as pd

# 1. Carga de datos desde un archivo Excel
ruta_archivo = r"E:\LEARNING\CLASES IA\EJERCICIOS\transacciones_bancarias.xlsx"
df = pd.read_excel(ruta_archivo)

# --- Inspección Inicial de Datos ---
print("\n--- 1.1. Inspección Inicial: Primeras 3 filas ---")
print(df.head(3))

# --- Resumen de la estructura y valores nulos (df.info()) ---
print("\n--- 1.2. Resumen de la estructura y valores nulos ---")
print(df.info())

# Objetivo: Analizar transacciones realizadas vía canal 'online' con 'monto_usd' > 1000
# para detectar posibles fraudes y optimizar seguridad digital.
df_simple = df[["id_transaccion", "cliente_id", "monto_usd", "canal", "tipo_transaccion", "es_fraude"]]

# 2. Filtrado de datos con condiciones booleanas
# Se crea una condición lógica para seleccionar filas específicas.
condicion = (df["canal"] == "online") & (df["monto_usd"] > 1000) & (df["es_fraude"] == 1)

# Se aplica el filtro y se resetea el índice para tener una secuencia limpia.
df_filtrado = df[condicion].reset_index(drop=True)
print("\n--- 2. DataFrame filtrado: Transacciones 'online' con monto > $1000 y fraude detectado ---")
print(df_filtrado)

# 3. Selección de datos con el método .loc
# .loc permite seleccionar datos por etiquetas (índices y nombres de columnas).

# Selección de una fila completa por su etiqueta (en este caso, el índice 1).
fila_2 = df.loc[1]
# Selección de un valor específico en la fila 1 y la columna 'monto_usd'.
valor_columna = df.loc[1, "monto_usd"]
# Selección de un subconjunto: filas de la 0 a la 3 y columnas específicas.
subset = df.loc[0:3, ["id_transaccion", "canal", "monto_usd"]]

print("\n--- 3.1. Selección de una fila completa por etiqueta (índice 1) ---")
print(fila_2)
print(f"\n--- 3.2. Selección de un valor específico (fila 1, columna 'monto_usd') ---")
print(valor_columna)
print("\n--- 3.3. Selección de un subconjunto de filas y columnas ---")
print(subset)

# 4. Ordenamiento y manejo de valores faltantes (NaN)
# Ordenar el DataFrame por la columna 'monto_usd' en forma descendente.
df_ordenado = df.sort_values(by="monto_usd", ascending=False)
print("\n--- 4.1. DataFrame ordenado por 'monto_usd' (descendente) ---")
print(df_ordenado.head())

# Detectar y mostrar todas las filas que contienen al menos un valor NaN en las columnas especificadas.
filas_nulas = df[df["monto_usd"].isna() | df["tipo_transaccion"].isna()]
print("\n--- 4.2. Filas que contienen valores nulos en 'monto_usd' o 'tipo_transaccion' ---")
print(filas_nulas)

# Eliminar filas con NaN en una columna específica ('monto_usd').
df_sin_nulos = df.dropna(subset=["monto_usd"]).reset_index(drop=True)
print("\n--- 4.3. DataFrame después de eliminar filas con NaN en 'monto_usd' ---")
print(df_sin_nulos)

# Imputar (rellenar) valores faltantes con la mediana.
mediana = df["monto_usd"].median()
print(f"\n--- 4.4. Mediana calculada para 'monto_usd': {mediana} ---")

# Se crea una copia para no modificar el DataFrame original.
df_imputado = df.copy()
# Se reemplazan los valores NaN en 'monto_usd' con la mediana calculada.
df_imputado["monto_usd"] = df_imputado["monto_usd"].fillna(mediana)

# Imputar NaN de la columna 'es_fraude' con su mediana.
mediana_fraude = df["es_fraude"].median()
df_imputado["es_fraude"] = df_imputado["es_fraude"].fillna(mediana_fraude)

print("\n--- 4.5. Comparación antes y después de imputar 'monto_usd' (primeras 5 filas) ---")
print("Original con NaN:")
print(df[df["monto_usd"].isna()].head())
print("\nCopia con NaN reemplazados por la mediana:")
print(df_imputado.loc[df[df["monto_usd"].isna()].index].head())

# 5. Funciones de agregación en pandas (groupby, agg, pivot_table)
# Agrupar por 'canal' y calcular varias métricas agregadas.
df_agrupado = (
    df.groupby("canal")
    .agg(
        transacciones=("id_transaccion", "count"),  # Contar transacciones por canal
        monto_promedio=("monto_usd", "mean"),  # Promedio de monto_usd
        monto_total=("monto_usd", "sum"),  # Suma total de monto_usd
        fraude_total=("es_fraude", "sum"),  # Número total de fraudes detectados
    )
    .reset_index()
)

print("\n--- 5.1. Agregación de datos por 'canal' usando groupby y agg ---")
print(df_agrupado)

# Crear una tabla pivote para analizar el 'monto_usd' promedio
# cruzando 'canal' con 'tipo_transaccion'.
tabla_pivote = pd.pivot_table(
    df,
    values="monto_usd",
    index="canal",  # filas: canales
    columns="tipo_transaccion",  # columnas: tipo de transacción
    aggfunc="mean",  # promedio del monto
)

print("\n--- 5.2. Tabla pivote: 'monto_usd' promedio por canal y tipo de transacción ---")
print(tabla_pivote)
