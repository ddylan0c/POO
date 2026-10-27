class Cuenta:
    def __init__(self, numero_cuenta: int, documento_identidad: int, nombre_cliente: str, saldo: float):
        self.__numero_cuenta = numero_cuenta
        self.__documento_identidad = documento_identidad
        self.__nombre_cliente = nombre_cliente
        self.__saldo = saldo


    def get_numero_cuenta(self) -> int:
        return self.__numero_cuenta

    def get_documento_identidad(self) -> int:
        return self.__documento_identidad

    def get_nombre_cliente(self) -> str:
        return self.__nombre_cliente

    def get_saldo(self) -> float:
        return self.__saldo


    def depositar_dinero(self, monto: float):
        if monto > 0:
            retencion = monto * 0.19
            monto_neto = monto - retencion
            self.__saldo += monto_neto
            print(f"[Modelo] Depósito de {monto} realizado. Retención (19%): {retencion:.2f}. Saldo actualizado: {self.__saldo:.2f}")
        else:
            print("[Modelo] El monto a depositar debe ser mayor a cero.")


    def retirar_dinero(self, monto: float) -> bool:
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"[Modelo] Retiro exitoso de {monto:.2f}. Saldo actual: {self.__saldo:.2f}")
            return True
        else:
            print("[Modelo] Fondos insuficientes o monto inválido para el retiro.")
            return False

  
    def __str__(self):
        return (f"Número de Cuenta: {self.__numero_cuenta} | "
                f"Documento: {self.__documento_identidad} | "
                f"Cliente: {self.__nombre_cliente} | "
                f"Saldo Actual: ${self.__saldo:,.2f}")

