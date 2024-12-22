# Classe per gestionar les comandes
class Order:
    def __init__(self, order_id, status="Pendent"):
        # Identificador únic de la comanda
        self.order_id = order_id
        # Diccionari per guardar productes i quantitats
        self.products = {}
        # Estat inicial de la comanda
        self.status = status

    # Afegeix un producte a la comanda
    def add_product(self, product, quantity=1):
        if product.name in self.products:
            # Llança un error si el producte ja existeix
            raise ValueError(f"El producte {product.name} ja existeix a la comanda.")
        self.products[product.name] = quantity

    # Actualitza la quantitat d'un producte existent
    def update_product_quantity(self, product, quantity):
        if product.name not in self.products:
            # Llança un error si el producte no existeix
            raise ValueError(f"El producte {product.name} no existeix a la comanda.")
        self.products[product.name] += quantity

    # Canvia l'estat de la comanda
    def update_status(self, new_status):
        if new_status not in ["Pendent", "Enviada"]:
            # Llança un error si l'estat no és vàlid
            raise ValueError("L'estat no és vàlid.")
        self.status = new_status

    # Retorna un resum de la comanda
    def summary(self):
        products_summary = ", ".join(f"{name}: {quantity}" for name, quantity in self.products.items())
        return f"Comanda {self.order_id} [{self.status}]: {products_summary}"
