import numpy as np

ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])

ventas_con_aumento = ventas * 1.10
total = ventas_con_aumento.sum()

print("Ventas con aumento:", ventas_con_aumento)
print("Total de la semana:", total)