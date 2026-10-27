from modelo import Cuenta

class InterfazUsuario:
    @staticmethod
    def mostrar_menu():
        print("\n--- SISTEMA DE GESTIÓN DE CUENTAS BANCARIAS ---")
        print("1. Crear y agregar nueva cuenta")
        print("2. Listar y mostrar todas las cuentas (Recorrido de lista)")
        print("3. Realizar depósito en una cuenta")
        print("4. Realizar retiro de una cuenta")
        print("5. Salir")

    @staticmethod
    def solicitar_datos_cuenta():
        print("\n--- Registro de Nueva Cuenta ---")
        

        while True:
            try:
                num_cuenta = int(input("Ingrese el número de cuenta (entero largo): "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido. Intente de nuevo.")


        while True:
            try:
                documento = int(input("Ingrese el documento de identidad: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número de documento válido. Intente de nuevo.")


        while True:
            nombre = input("Ingrese el nombre del cliente: ").strip()
            if nombre:
                break
            print("Error: El nombre no puede estar vacío. Intente de nuevo.")


        while True:
            try:
                saldo_inicial = float(input("Ingrese el saldo inicial: "))
                break
            except ValueError:
                print("Error: Debe ingresar un valor numérico válido para el saldo. Intente de nuevo.")

        return Cuenta(num_cuenta, documento, nombre, saldo_inicial)

    @staticmethod
    def mostrar_lista_cuentas(cuenta_clientes: list):
        print("\n--- LISTADO GENERAL DE CLIENTES Y CUENTAS ---")
        if not cuenta_clientes:
            print("No hay cuentas registradas en el sistema.")
            return
        
        for indice, cuenta in enumerate(cuenta_clientes):
            print(f"[{indice}] {cuenta}")
