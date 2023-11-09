from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente


class Test(CuentaAhorros, CuentaCorriente):
    def __init__(self, numero, nombrePropietario, saldo, interes, TieneChequera):
        CuentaAhorros.__init__(self, numero, nombrePropietario, saldo, interes)
        CuentaCorriente.__init__(self, numero, nombrePropietario, saldo, TieneChequera)

# Ejemplo
cuenta_pru = Test("95823", "James Cameron", 5368.45, 2.0, True)

# Acceder a propiedades y métodos de ambas clases base
print("Saldo de la cuenta de ahorros:")
print(cuenta_pru.saldo)
print("Tiene chequera en la cuenta corriente:")
print(cuenta_pru.TieneChequera)

# Realizar transacciones
cuenta_pru.credito(327.0)
cuenta_pru.debito(120.0)
cuenta_pru.pagar_cheque(200.0)

# Mostrar saldos después de las transacciones
print("Saldo después de las transacciones:")
print(cuenta_pru.saldo)