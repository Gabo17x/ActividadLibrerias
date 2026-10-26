import numpy as np

calificaciones = np.array([
    [8.5, 7.0, 9.0, 8.0],  # Carlos
    [6.0, 7.5, 8.0, 7.0],  # Ana
    [9.0, 8.5, 9.5, 9.0],  # Luis
])

print("Promedio por estudiante:", calificaciones.mean(axis=1))
print("Promedio por materia:", calificaciones.mean(axis=0))