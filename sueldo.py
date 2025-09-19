"""
Inserta el encabezado aquí y escribe tu código abajo
"""


# Declaraciones


# Entradas
horas = int(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

# Proceso
if horas <= 48:
    sueldo = horas * tarifa
    horas_extras = 0
    importe = 0
else:
    horas_extras = horas - 48
    importe = horas_extras * tarifa * 2
    sueldo = (48 * tarifa) + importe

# Salidas
print(f"Horas trabajadas: {horas}")
print(f"Tarifa por hora:{tarifa}" ) 

print(f"Horas extras: {horas_extras}")
print(f"Sueldo por horas extras: {importe}")
print(f"Sueldo total: {sueldo}")