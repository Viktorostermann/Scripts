from typing import Protocol


# Contratos de deposito, retiro y transferencia
class IDepositar(Protocol):
    def depositar(self, monto: float) -> None: ...
class IRetirar(Protocol):
    def retirar(self, monto: float) -> None: ...
class ITransferir(Protocol):
    def transferir(self, monto: float) -> None: ...


class CuentaAhorros:
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta de ahorros ")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta de ahorros")


class CuentaCorriente:
    def depositar(self, monto: float) -> None:
        print(f"Depositando { monto} en cuenta corriente")

    def retirar(self, amount: float) -> None:
        print(f"Retirando {amount} de cuenta corriente")

    def transferir(self, amount: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {amount} de cuenta corriente a cuenta { a_cuenta}")


def realizar_pago(cuenta: ITransferir, monto: float) -> None:
    cuenta.transferir(monto)


cuentaCorriente = CuentaCorriente()

realizar_pago(cuentaCorriente, 20)

# cuentaAhorros.depositar(100, 20)
# cuentaAhorros.retirar(50)

# cuentaCorriente = CuentaCorriente()
# cuentaCorriente.depositar(100)
# cuentaCorriente.retirar(50)
# cuentaCorriente.transferir(20, "ABCSK189148")