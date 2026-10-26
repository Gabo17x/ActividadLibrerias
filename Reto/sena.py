import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

estudiantes = {
    "horas_estudio": [2, 4, 5, 6, 8, 10, 3, 7, 9, 1],
    "asistencia": [60, 70, 75, 80, 90, 95, 65, 85, 92, 50],
    "aprobo": [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
}

# ---------- PANDAS ----------
# 1. Crear el DataFrame
df = pd.DataFrame(estudiantes)

# 2. Estadísticas
print("Estadísticas:")
print(df.describe())

# 3. Nueva columna: promedio semanal (horas / 7)
df["promedio_semanal"] = df["horas_estudio"] / 7
print("\nDataFrame con promedio_semanal:")
print(df)

# 4. Aprobados con menos de 6 horas de estudio
filtro = df[(df["aprobo"] == 1) & (df["horas_estudio"] < 6)]
print("\nAprobaron con menos de 6 horas:")
print(filtro)

# ---------- NUMPY ----------
asistencia = np.array(df["asistencia"])
print("\nPromedio de asistencia:", np.mean(asistencia))
print("Desviación estándar de asistencia:", np.std(asistencia))

# ---------- SCIKIT-LEARN ----------
# X = datos de entrada, y = lo que queremos predecir
X = df[["horas_estudio", "asistencia"]]
y = df["aprobo"]

# Separar datos de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Crear y entrenar el modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Evaluar la precisión
predicciones = modelo.predict(X_test)
precision = accuracy_score(y_test, predicciones)
print("\nPrecisión del modelo:", precision)

# Predecir un aprendiz nuevo: 5 horas y 78% de asistencia
nuevo = pd.DataFrame({"horas_estudio": [5], "asistencia": [78]})
resultado = modelo.predict(nuevo)

if resultado[0] == 1:
    print("El aprendiz probablemente APROBARÁ")
else:
    print("El aprendiz probablemente NO aprobará")