import pandas as pd

# Datos iniciales del inventario de la tienda
inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

# Creamos una tabla con Pandas
df = pd.DataFrame(inventario.csv)


# EJERCICIO 5: Explorar el inventario

# Mostramos las primeras filas
print("\n--- EJERCICIO 5: EXPLORAR INVENTARIO ---")
print(df.head())

# Mostramos la cantidad de filas y columnas
print("Forma de la tabla:", df.shape)

# Mostramos los nombres de las columnas
print("Columnas:", df.columns)

# Mostramos estadísticas de los datos numéricos
print(df.describe())


# EJERCICIO 6: Productos por reponer

# Filtramos los productos con stock menor a 10
print("\n--- EJERCICIO 6: PRODUCTOS POR REPONER ---")
productos_reponer = df[df["stock"] < 10]
print(productos_reponer)


# EJERCICIO 7: Valor del inventario

# Calculamos el valor total de cada producto en existencia
df["valor_inventario"] = df["precio"] * df["stock"]

# Indicamos si se debe reponer el producto
df["reponer"] = df["stock"] < 10

print("\n--- EJERCICIO 7: VALOR DEL INVENTARIO ---")
print(df)


# EJERCICIO 8: Ordenar y resumir

# Ordenamos del producto más caro al más barato
ordenado = df.sort_values(by="precio", ascending=False)

print("\n--- EJERCICIO 8: INVENTARIO ORDENADO ---")
print(ordenado)

# Calculamos el precio promedio de los productos
promedio = df["precio"].mean()
print("Precio promedio:", promedio)


# EJERCICIO 9: Guardar y leer un archivo CSV

# Guardamos la tabla en un archivo que Excel puede abrir
df.to_csv("inventario.csv", index=False, encoding="utf-8-sig")

# Leemos nuevamente el archivo CSV
df_leido = pd.read_csv("inventario.csv")

print("\n--- EJERCICIO 9: LEER ARCHIVO CSV ---")
print(df_leido)

# Verificamos que los datos sean iguales
print("¿Los datos son iguales?", df.equals(df_leido))