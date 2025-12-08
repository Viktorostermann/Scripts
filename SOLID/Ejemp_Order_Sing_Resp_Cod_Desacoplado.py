# Ordenamiento de CLases con SOLID aplicacndo el pincipio de Responsabilidad Unica y Desacoplamiento.
# Este principio establece que una clase debe tener una, y solo una, razón para cambiar. 
# Y que las clases deben estar desacopladas entre si. 
# Quiere decir que una clase no debe depender de los detalles de otra clase para funcionar, sino de una abstracción
# es decir, una clase debe ser independiente de otras clases para su funcionamiento.
# Esto facilita el mantenimiento y la escalabilidad del código.

class Order:
	def __init__(self):
		self.items = []
		self.quantities = []
		self.prices = []
		self.status = "open"
	
	def add_item(self, name: str, quantity: int, price : float) -> None: 
		self.items.append(name)
		self.quantities.append(quantity)
		self.prices.append(price)
	
class PaymentProcessor:
	def pay(self, order: Order, payment_type: str, security_code: str):
		if payment_type == "debit":
			print("Processing debit payment type")
			print(f"Verifying security code: {security_code}")
			order.status = "paid"
		elif payment_type == "credit":
			print("Processing credit payment type")
			print(f"Verifying security code: {security_code}")
			order.status = "paid"
		else:
			raise Exception(f"Unknown payment type: {payment_type}")
		order.status = "paid"

class CalculatorProcessor:
	def total_price(self, order: Order):
		total = 0
		for quantity, price in zip(order.quantities, order.prices):
			total += quantity * price
		return total

order = Order()
print("Estado de la orden: ", order.status)
order.add_item("Keyboard", 1, 50)
#order.add_item("SSD", 1, 150)
#order.add_item("USB cable", 2, 5)

procesor = PaymentProcessor()
procesor.pay(order, "debit", "0372846") # Separa la responsabilidad de pago

total = CalculatorProcessor()
print("Total price:", total.total_price(order))  # ← aquí usamos la instancia