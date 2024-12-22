# Classe per gestionar els clients
class Client:
    def __init__(self, client_id, name, email):
        # Identificador únic del client
        self.client_id = client_id
        # Nom del client
        self.name = name
        # Correu electrònic del client
        self.email = email
        # Llista de comandes associades al client
        self.orders = []

    # Afegeix una comanda a la llista del client
    def add_order(self, order):
        self.orders.append(order)

    # Retorna la llista de comandes del client
    def list_orders(self):
        return self.orders
