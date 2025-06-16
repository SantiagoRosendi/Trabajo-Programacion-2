def calcular_IMC(peso: float, altura: float) -> float:
    return peso / (altura ** 2)

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    imc = calcular_IMC(peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    return 10 * peso + 6.25 * (altura * 100) - 5 * edad + valor_genero

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: int, valor_actividad: float) -> float:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: int) -> str:
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = round(tmb * 0.80)
    rango_superior = round(tmb * 0.85)
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior} y {rango_superior} calorías al día."