# --- SIMULACIÓN DE BASE DE DATOS (Para validar cuentas y saldos) ---
# Cuenta del usuario actual: "123" (Saldo inicial: 5000)
# Cuenta destino de prueba: "456"
cuentas_banco = {
    "123": 5000.0,
    "456": 1500.0
}

id_usuario_actual = "123"

# --- VARIABLES DEL INTEGRANTE 3 (Registro, contadores y acumuladores) ---
historial_movimientos = []
contador_consultas = 0
contador_transferencias = 0
acumulado_transferido = 0.0


# 1. Diseñar la función de consulta de saldo
def consultar_saldo():
    global contador_consultas
    saldo_actual = cuentas_banco[id_usuario_actual]
    contador_consultas += 1
    
    # Registrar en el historial de la sesión
    historial_movimientos.append(f"Consulta de saldo: ${saldo_actual:.2f}")
    
    print("\n--- CONSULTA DE SALDO ---")
    print(f"Su saldo actual es: ${saldo_actual:.2f}")


# 2. Desarrollar el sistema de transferencias simples con validaciones
def realizar_transferencia():
    global contador_transferencias, acumulado_transferido
    print("\n--- REALIZAR TRANSFERENCIA ---")
    
    cuenta_destino = input("Ingrese el número de cuenta destino: ")
    
    # Validar que la cuenta destino exista
    if cuenta_destino not in cuentas_banco:
        print("Error: La cuenta destino no existe.")
        historial_movimientos.append(f"Intento fallido de transferencia a cuenta {cuenta_destino} (No existe)")
        return

    # Validar que no se transfiera a sí mismo (opcional pero buena práctica)
    if cuenta_destino == id_usuario_actual:
        print("Error: No puede transferirse a su propia cuenta.")
        return

    try:
        monto = float(input("Ingrese el monto a transferir: $"))
    except ValueError:
        print("Error: Monto inválido.")
        return

    if monto <= 0:
        print("Error: El monto debe ser mayor a 0.")
        return

    # Validar que haya saldo suficiente
    saldo_actual = cuentas_banco[id_usuario_actual]
    if monto > saldo_actual:
        print(f"Error: Saldo insuficiente. Su saldo es de ${saldo_actual:.2f}")
        historial_movimientos.append(f"Intento fallido de transferencia por saldo insuficiente (${monto:.2f})")
        return

    # Si pasa las validaciones, se ejecuta la transferencia
    cuentas_banco[id_usuario_actual] -= monto
    cuentas_banco[cuenta_destino] += monto
    
    # Actualizar contadores y acumuladores
    contador_transferencias += 1
    acumulado_transferido += monto
    
    # Registrar la operación con éxito
    historial_movimientos.append(f"Transferencia exitosa a cuenta {cuenta_destino}: -${monto:.2f}")
    
    print(f"¡Transferencia realizada con éxito de ${monto:.2f} a la cuenta {cuenta_destino}!")


# 3. Programar un registro básico de operaciones (Historial del usuario)
def mostrar_historial_sesion():
    print("\n--- HISTORIAL DE MOVIMIENTOS EN ESTA SESIÓN ---")
    if not historial_movimientos:
        print("No se han realizado operaciones en esta sesión.")
    else:
        for movimiento in historial_movimientos:
            print(f"- {movimiento}")
    
    # Mostrar estadísticas usando los contadores y acumuladores requeridos
    print("\n--- RESUMEN DE CONTROL ---")
    print(f"Consultas realizadas: {contador_consultas}")
    print(f"Transferencias exitosas realizadas: {contador_transferencias}")
    print(f"Total de dinero transferido: ${acumulado_transferido:.2f}")


# --- MENÚ DE PRUEBA (Ideal para conectar con el Integrante 4) ---
def menu_test():
    while True:
        print("\n==============================")
        print("       SISTEMA BANCARIO       ")
        print("==============================")
        print("1. Consultar Saldo")
        print("2. Transferir Dinero")
        print("3. Ver Historial y Registros")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            realizar_transferencia()
        elif opcion == "3":
            mostrar_historial_sesion()
        elif opcion == "4":
            print("Saliendo de la sesión del Integrante 3. ¡Adiós!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú de prueba
if __name__ == "__main__":
    menu_test()