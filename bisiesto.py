"""
Determinar si un año es bisiesto.
"""

# Entradas
anho = int(input("Introduzca un año: "))

# Proceso
if anho % 400 == 0 or anho % 4 == 0 and anho % 100 != 0:
    bisiesto = "sí"
else:
    bisiesto = "no"

# Salidas
print(anho, bisiesto, "es un año bisiesto")
