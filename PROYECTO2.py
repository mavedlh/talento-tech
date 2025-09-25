import random

# diccionario con productos y su disponibilidad
# (true = en stock , false = agotado)
inventario = {"Camisas": True, "Zapatos": False, "Pantalones": True, "Gorras": False, "Mochilas": True}
# listas con acciones que puede realizar el sistema de control


acciones = ["Verificar", "reabastece", "Omitir", "Detener"]

# Tupla con productos criticos (los más vendidos)
productos_criticos = ("Camisas", "Zapatos")

# --- uso de for --- #
print("\n Estado Inicial Del Inventario:")
for producto, disponible in inventario.items():
    print(f"{producto}:{"disponible" if disponible else "Agotado"}")

    # --- Uso de While con eventos aleatorios --- #
    print("\n Ejecutando control de inventario(con eventos aleatorios)...")
    indice = 0
    while indice < len(acciones):
        accion = acciones[indice]
        indice += 1

        # Evento aleatorio: si sale 6, simulamos un error de inventario y se detiene el sistema
        numero = random.randint(1, 10)
        if numero == 6:
            print("Error en el sistema de inventario (numero aleatorio = 6). Deteniendo operaciones")
            if accion == "Detener":
                print("Accon detener entrada.Se interrumpe el control.")
                break

            elif accion == "Omitir":
                print("Accion omitir: No se realiza ninguna operacion.")
