# Realizar una calculadora de gastos personales
# NO es obligatorio usar for, ni crear contadores
# si el if, elif, else ; booleanos

# Calculadora de gastos personales Maria
print("calculadora de gastos mensuales")
ingresos = float(input("¿cual es mi ingreso mensual?: "))
gastos_comida = float(input("¿cuanto gasto en comida?: "))
gastos_transporte = float(input("¿cuanto en transporte?: "))
gastos_hormiga = float(input("¿cuanto son mis gastos hormiga reina?: "))
otros_gastos = float(input("¿cuanto gasto en otros cosas?: "))
meta_ahorro = float(input("¿cuanto deseo ahorrar?: "))

gastos_totales = gastos_comida + gastos_transporte + gastos_hormiga + otros_gastos
ahorros = ingresos - gastos_totales
# Variable booleana
esta_ahorrando = ahorros > 0
cumple_meta = ahorros > meta_ahorro

if cumple_meta:
    print("cumpliste la meta de ahorro eres la mejor del mundo")
elif esta_ahorrando:
    print("estas ahorrando pero no o suficiente esfuerzate mas")
else:
    print("ten menos gastos y empieza a ahorrar")
