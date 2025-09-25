import pandas as pd

# Cargar archivo
df = pd.read_csv(r"C:\ruta\a\tu\archivo\ventas_tienda.csv")

# Verificar columnas
print("Columnas en el archivo:", df.columns.tolist())

# 1. Calcular estadísticas de 'Precio_Unitario'
media_precio = df["Precio_Unitario"].mean()
mediana_precio = df["Precio_Unitario"].median()
moda_precio = df["Precio_Unitario"].mode().tolist()

print("\n--- Estadísticas de 'Precio_Unitario' ---")
print("Media:", media_precio)
print("Mediana:", mediana_precio)
print("Moda:", moda_precio)

# 2. Filtrar ventas de clientes recurrentes
recurrentes = df[df["Cliente_Recurrente"] == True]
print("\nNúmero de ventas de clientes recurrentes:", len(recurrentes))
print("Primeras 5 ventas recurrentes:")
print(recurrentes[["Producto", "Ciudad", "Precio_Unitario"]].head())

# 3. Categoría con mayores ingresos totales
df["Ingreso_Total"] = df["Precio_Unitario"] * df["Cantidad_Vendida"]
categoria_max_ingresos = df.groupby("Categoria")["Ingreso_Total"].sum().idxmax()
print("\nCategoría con mayores ingresos totales:", categoria_max_ingresos)

# 4. Crear columna con descuento aplicado (10% si no es recurrente)
df["Precio_Final"] = df.apply(
    lambda row: row["Precio_Unitario"] * 0.9 if not row["Cliente_Recurrente"] else row["Precio_Unitario"], axis=1
)

print("\nColumna 'Precio_Final' creada (primeras filas):")
print(df[["Producto", "Cliente_Recurrente", "Precio_Unitario", "Precio_Final"]].head())

# 5. Guardar subconjunto en nuevo archivo CSV
subconjunto = df[["Producto", "Categoria", "Precio_Unitario", "Cantidad_Vendida", "Ciudad", "Ingreso_Total"]]
subconjunto.to_csv("ventas_subconjunto.csv", index=False)
print("\nSubconjunto guardado en 'ventas_subconjunto.csv'")
