import calculadora_indices as calc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M/F): ").strip().upper()
valor_genero = 10.8 if genero == 'M' else 0

grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(f"Porcentaje de grasa corporal: {grasa:.2f}%")