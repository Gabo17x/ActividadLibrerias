import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

datos = {
    "edad": [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "ingreso": [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    "compro": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
}


df = pd.DataFrame(datos)


print("DATOS DE LOS CLIENTES")
print(df)


X = df[["edad", "ingreso"]]

y = df["compro"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LogisticRegression()

modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

precision = accuracy_score(y_test, predicciones)



print("\nRESULTADOS DEL MODELO")

print("Resultados reales:", y_test.tolist())
print("Predicciones:", predicciones.tolist())
print("Precisión:", precision)
print("Precisión en porcentaje:", precision * 100, "%")