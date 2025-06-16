import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ").strip().upper()
valor_genero = 5 if genero == 'M' else -161

print("Nivel de actividad física:")
print("1. Poco o ningún ejercicio")
print("2. Ejercicio ligero (1-3 días/semana)")
print("3. Ejercicio moderado (3-5 días/semana)")
print("4. Deportista (6-7 días/semana)")
print("5. Atleta (entrena 2 veces al día)")

actividad = int(input("Seleccione una opción (1-5): "))
valores_actividad = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.72, 5: 1.9}
valor_actividad = valores_actividad.get(actividad, 1.2)

calorias = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(f"Calorías quemadas con actividad física: {calorias:.2f} calorías/día")