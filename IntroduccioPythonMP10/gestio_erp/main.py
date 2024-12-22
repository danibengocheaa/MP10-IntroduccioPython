from gestio_erp.clients import Client
from gestio_erp.orders import Order
from gestio_erp.products import Product

# Crear clients
anna = Client(1, "Anna", "anna@example.com")
pere = Client(2, "Pere", "pere@example.com")
joan = Client(3, "Joan", "joan@example.com")

# Crear productes
bicicleta = Product("bicicleta")
casc = Product("casc")
guants = Product("guants")
maillot = Product("maillot")
roda = Product("roda")
pantalons = Product("pantalons")
patinet = Product("patinet")

# Crear comandes per a Anna
order1 = Order(101)
order1.add_product(bicicleta, 1)
order1.add_product(casc, 2)

order2 = Order(102)
order2.add_product(guants, 1)

anna.add_order(order1)
anna.add_order(order2)

# Crear comandes per a Pere
order3 = Order(103)
order3.add_product(maillot, 1)
order3.add_product(roda, 2)

order4 = Order(104)
order4.add_product(guants, 2)

pere.add_order(order3)
pere.add_order(order4)

# Resum inicial
print("COMANDES DELS CLIENTS")
print(f"Comandes del client Anna: {len(anna.list_orders())}")
for order in anna.list_orders():
    print(order.summary())

print(f"Comandes del client Pere: {len(pere.list_orders())}")
for order in pere.list_orders():
    print(order.summary())

print(f"El client Joan no té cap comanda.")

# Gestió d'errors
try:
    order1.add_product(bicicleta)
except ValueError as e:
    print(e)

try:
    order1.update_product_quantity(patinet, 1)
except ValueError as e:
    print(e)

# Actualització de comandes
order1.update_product_quantity(bicicleta, 1)
order1.update_product_quantity(casc, 2)
order1.add_product(pantalons, 1)
order1.update_status("Enviada")

# Resum final
print("COMANDES DELS CLIENTS")
print(f"Comandes del client Anna: {len(anna.list_orders())}")
for order in anna.list_orders():
    print(order.summary())
