from Cuenta import Cuenta


class CuentaAhorros(Cuenta):
    def __init__(self, numero, nombrePropietario, saldo, interes: float = None):
        super().__init__(numero, nombrePropietario, saldo)
        self._interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, nuevo_interes):
        self._interes = nuevo_interes

    def credito(self, cantidad):
        self.saldo += cantidad

    def debito(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta de ahorros {self.numero}: ${self.saldo}")

    def pagar_interes(self):
        interes_ganado = self.saldo * (self.interes / 100)
        self.saldo += interes_ganado

# Ejemplo
#cuenta_pru = CuentaAhorros("38503", "Pitof", 3747.00, 3.5)
#cuenta_pru.credito(376.00)
#cuenta_pru.debito(124.00)
#cuenta_pru.mostrar_saldo()
#cuenta_pru.pagar_interes()
#cuenta_pru_saldo()
