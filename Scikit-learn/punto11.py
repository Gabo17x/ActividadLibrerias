import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

datos = {
    "edad": [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "ingreso": [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    "compro": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
}

df = pd.DataFrame(datos)

X = df[["edad", "ingreso"]]
y = df["compro"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

clientes_nuevos = pd.DataFrame({
    "edad": [28, 52],
    "ingreso": [2.2, 4.8]
})

resultados = modelo.predict(clientes_nuevos)


for i, resultado in enumerate(resultados):
    
    if resultado == 1:
        print(f"Cliente {i + 1}: Sí compra")
    else:
        print(f"Cliente {i + 1}: No compra")