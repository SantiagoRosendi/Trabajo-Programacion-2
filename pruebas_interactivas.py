
# Archivo: pruebas.py (versión interactiva para Windows)
# Pruebas manuales para los módulos de la calculadora de índices

import os

def separador(titulo):
    print(f"\n{'='*10} {titulo} {'='*10}")

def ejecutar(nombre_script):
    os.system(f"python {nombre_script}")

# Módulo 1 – IMC
separador("PRUEBAS IMC")
print("Probá con valores como: 70 y 1.75 (válido), 'setenta' y 1.75 (inválido), 70 y 0 (inválido)")
ejecutar("consola_calculo_imc.py")

# Módulo 2 – Porcentaje de Grasa Corporal
separador("PRUEBAS % GRASA CORPORAL")
print("Probá con: hombre, 25, 70, 80 (válido), género inválido o edad 0 (inválidos)")
ejecutar("consola_calculo_porcentaje_grasa.py")

# Módulo 3 – TMB
separador("PRUEBAS TMB (Calorías en reposo)")
print("Probá con: hombre, 25, 70, 175 (válido), edad negativa (inválido)")
ejecutar("consola_calculo_calorias_reposo.py")

# Módulo 4 – TMB según actividad
separador("PRUEBAS TMB SEGÚN ACTIVIDAD")
print("Probá con: 2000 y 1.55 (válido), o 'moderada' en lugar de número (inválido)")
ejecutar("consola_calculo_calorias_actividad.py")

# Módulo 5 – Calorías para adelgazar
separador("PRUEBAS CALORÍAS PARA ADELGAZAR")
print("Probá con: 2500 (válido) o -1500 (inválido)")
ejecutar("consola_calculo_calorias_adelgazar.py")
