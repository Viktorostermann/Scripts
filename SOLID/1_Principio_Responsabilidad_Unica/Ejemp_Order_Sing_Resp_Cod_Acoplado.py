# Ordenamiento de CLases con SOLID aplicacndo el pincipio de Responsabilidad Unica con Acoplamiento de Clases.
# EL uso de clases acopladas va en contra del principio de responsabilidad unica, 
# ya que una clase asume multiples responsabilidades y depende de otras clases para cumplir con su funcion.
# Por lo tanto, se recomienda evitar el acoplamiento excesivo entre clases.
# Debido a que una clase debe tener una, y solo una, razón para cambiar.
# Entonces el acoplamiento se refiere a la dependencia entre clases de manera directa.  

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
	
	def total_price(self):
		total = 0
		for quantity, price in zip(self.quantities, self.prices):
			total += quantity * price
		return total
	
	def pay(self, payment_type: str, security_code: str):
		if payment_type == "debit":
			print("Processing debit payment type")
			print(f"Verifying security code: {security_code}")
		elif payment_type == "credit":
			print("Processing credit payment type")
			print(f"Verifying security code: {security_code}")
		else:
			raise Exception(f"Unknown payment type: {payment_type}")
		self.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print("El precio total de la orden es: ", order.total_price())
order.pay("debit", "0372846")
print(order.status)