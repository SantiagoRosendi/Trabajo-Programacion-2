import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ").strip().upper()
valor_genero = 5 if genero == 'M' else -161

tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(f"Tasa Metabólica Basal: {tmb:.2f} calorías/día")