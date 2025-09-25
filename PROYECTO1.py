# 1 calculaadora financiera usando varios tipos de datos
print("MI PRIMERA CALCULADORA FINANCIERA EN python")
# umbral de ahorro (en pesos COP)--- tupla
umbrales = (100000, 1000000, 5000000)

# Mensajes --- tuplas y cadenas (tuple , str)
mensajes = (
    "Debes enfocarte en crear un fondo de inversion de emergencia",
    "Vas por buen camino, aumenta tu ahorro antes de invertir",
    "Tienes un buen colchón, puedes explorar inversiones de bajo riesgo",
    "excelente ahorro, puedes diversificar en diferentes productos financieros ",
)
# ---- Recomendaciones (Diccionarios)---#
recomendaciones = {
    "bajo": {"Cuenta de ahorro"},
    "medio": {"CDT", "Fondo colectivo", "Cuenta de ahorro"},
    "moderado": {"CDT", "fondo colectivo", "fondos voluntarios", "Cuenta de ahorros"},
    "alto": {"acciones", "ETF", "Fondo voluntarios", "inmuebles"},
}
# ---Lista para guardar el historial---#
historial = []

# ---Entradas del usuario---#
ingresos = float(input("¿cuanto son tus ingresos mensuales?(COP): $ "))
gastos = float(input("ingresa tus gastos mensuales (COP0): $ "))
ahorro = float(input("cuanto dinero tienes ahorrado actualmente (COP): $ "))

# ---Balanc (booleanos)---#
balance = ingresos - gastos
ahorra = balance > 0  # true, si hay ahorro
historial.append(f"balance mensual calculado:${balance:,.2f} COP")

# --- determinar el nivel del ahorro (if, elif,else)---#
if ahorro < umbrales[0]:
    nivel = "medio"
elif ahorro < umbrales[1]:
    nivel = "medio"
elif ahorro < umbrales[2]:
    nivel = "moderado"
else:
    nivel = "alto"

# ---Mostrar resultados ---#
print("\n ---resumen--")
print(f"Balance mensual: $ {balance:,.2f} COP(¿Ahorra?):", ahorra)


if nivel == "bajo":
    print("Mensaje:", mensajes[0])
elif nivel == "medio":
    print("Mensaje:", mensajes[1])
elif nivel == "moderado":
    print("Mensaje:", mensajes[2])
else:
    print(
        "Mensaje:",
        mensajes[3],
        "Balance mensual:",
        balance,
        "COP (¿ahorra?):",
        ahorra,
    )

if nivel == "bajo":
    print("Mensaje:", mensajes[0])
elif nivel == "medio":
    print("Mensaje:", mensajes[1])
elif nivel == "moderado":
    print("Mensaje:", mensajes[2])
else:
    print("Mensaje:", mensajes[3])

# --- Conjunto de recomendaciones ---#
if ahorra:
    sugerencias = recomendaciones[nivel]
else:
    sugerencias = set()  # Conjunto vacio

print("Recomendaciones")
if len(sugerencias):
    print("Ninguna por ahora")
else:
    for opcion in sugerencias:
        print("    ", opcion)


##---  Guardar historial ---##
historial.append("Nivel: " + nivel)
if len(sugerencias) == 0:
    historial.append("Recomendaciones: ninguna por ahora")
else:
    historial.append("Recomendaciones: " + str(sugerencias))
# --- Mostrar el historias ---#
print("\n ---historial---")
numero = 1
for elemento in historial:
    print(str(numero) + ".", elemento)
numero = numero + 1  # aumentando el contador
