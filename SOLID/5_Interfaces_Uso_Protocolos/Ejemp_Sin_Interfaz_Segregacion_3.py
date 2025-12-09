# using PROTOCOL
from typing import Protocol


class IOpoeracionFinanciera(Protocol):
    def depositar(self, monto: float) -> None: ... # Protocolo que define los métodos requeridos por las clases concretas
    def retirar(self, monto: float) -> None: ... # Protocolo que define los métodos requeridos por las clases concretas
    def transferir(self, monto: float, a_cuenta: str) -> None: ... # Protocolo que define los métodos requeridos por las clases concretas


class CuentaAhorros: # No implementa transferir porque no lo necesita, solo necesita depositar y retirar
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta de ahorros")
    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta de ahorros")

    # Raise una excepcion rompe ISP


class CuentaCorriente: # No implementa depositar porque no lo necesita, solo necesita retirar y transferir
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta corriente")
    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta corriente")
    def transferir(self, amount: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {amount} de cuenta corriente a cuenta { a_cuenta}")


cuentaAhorros = CuentaAhorros()
cuentaAhorros.depositar(100)
cuentaAhorros.retirar(50)

cuentaCorriente = CuentaCorriente()
cuentaCorriente.depositar(100)
cuentaCorriente.retirar(50)
cuentaCorriente.transferir(20, "ABCSK189148")