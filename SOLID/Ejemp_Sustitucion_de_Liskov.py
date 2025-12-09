# Principio de Sustitucion de Liskov (Liskov Substitution Principle - LSP) 
# El principio de sustitucion de Liskov es una regla que dice que las subclases 
# # deben ser capaces de reemplazar, sustituir instancias de sus superclases sin alterar el comportamiento de la aplicacion.
# Este principio es fundamental para garantizar que el codigo sea modular y escalable.
# Eete principio establece como crear una clase, cuando una clase debe heredar de otra clase 
# y como deben comportarse las subclases y sus metodos he instancias de estas clases. 

# Barbara Liskov, una cientifica de la computacion, introdujo este principio en 1987.
# El principio de sustitucion de Liskov se aplica a la programacion orientada a objetos.
# En la programacion orientada a objetos, las subclases deben ser capaces de reemplazar a sus superclases sin alterar el comportamiento de la aplicacion.

class MetodoPago:
    def procesar_pago(self, monto):
        pass
# ___________________________________________________________________________________________________

class PagoTarjeta(MetodoPago):
    def __init__ (self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto} con tarjeta {self.numero_tarjeta}")
        print("")
# ___________________________________________________________________________________________________

class PagoPayPal(MetodoPago):
    def __init__ (self, cuenta_paypal):
        self.cuenta_paypal = cuenta_paypal
    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto} usando cuenta de PayPal {self.cuenta_paypal}")
        print("")
# ___________________________________________________________________________________________________

class PagoBitcoin(MetodoPago):
    def __init__ (self, direccion_bitcoin):
        self.direccion_bitcoin = direccion_bitcoin
    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto} usando cuenta de Bitcoin {self.direccion_bitcoin}")
        print("")
# ___________________________________________________________________________________________________

class PagoCheque(MetodoPago):
    def __init__ (self, numero_cheque):
        self.numero_cheque = numero_cheque
    def procesar_pago(self, monto):
        raise NotImplementedError("El pago con cheque no es soportado de manera automatizada.")
    print("")
    def procesar_cheque(self, monto):
        print(f"Procesando cheque numero {self.numero_cheque} por un monto de {monto}")
        print("")
# ___________________________________________________________________________________________________

def realizar_pago(metodo_pago:MetodoPago, monto):
    metodo_pago.procesar_pago(monto)

#Instanciar las clases
pago_tarjeta = PagoTarjeta("1234 5678 9012 3456")
pago_payPal = PagoPayPal("cuenta_paypal")
pago_bitcoin = PagoBitcoin("direccion_bitcoin")
pago_cheque = PagoCheque("123456789")

realizar_pago(pago_tarjeta, 50)
realizar_pago(pago_payPal, 100)
realizar_pago(pago_bitcoin, 200)
#realizar_pago(pago_cheque, 300) # Esto lanzara una excepcion, violando el principio de Liskov, ya que PagoCheque no puede sustituir a MetodoPago de manera adecuada.

# Agregamos una excepcion para manejar el caso del cheque
try:
    realizar_pago(pago_cheque, 300)
except NotImplementedError as e:
    print(e)
    print("")

pago_cheque.procesar_cheque(300)  # Metodo especifico para procesar cheques
