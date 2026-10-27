from ui import InterfazUsuario

def main():

    cuentaClientes = []

    while True:
        InterfazUsuario.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nueva_cuenta = InterfazUsuario.solicitar_datos_cuenta()
            cuentaClientes.append(nueva_cuenta)
            print("¡Cuenta agregada exitosamente a la lista!")

        elif opcion == "2":
            InterfazUsuario.mostrar_lista_cuentas(cuentaClientes)

        elif opcion == "3":
            if not cuentaClientes:
                print("No hay cuentas creadas aún.")
                continue
            
            InterfazUsuario.mostrar_lista_cuentas(cuentaClientes)
            idx = int(input("Seleccione el índice de la cuenta para depositar: "))
            if 0 <= idx < len(cuentaClientes):
                monto = float(input("Ingrese la cantidad a depositar: "))
                cuentaClientes[idx].depositar_dinero(monto)
            else:
                print("Índice de cuenta inválido.")

        elif opcion == "4":
            if not cuentaClientes:
                print("No hay cuentas creadas aún.")
                continue
            
            InterfazUsuario.mostrar_lista_cuentas(cuentaClientes)
            idx = int(input("Seleccione el índice de la cuenta para retirar: "))
            if 0 <= idx < len(cuentaClientes):
                monto = float(input("Ingrese la cantidad a retirar: "))
                cuentaClientes[idx].retirar_dinero(monto)
            else:
                print("Índice de cuenta inválido.")

        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()