# Error si un client no es troba
class ClientNotFoundError(Exception):
    pass

# Error si un producte no existeix
class ProductNotFoundError(Exception):
    pass

# Error si un producte ja existeix en una comanda
class DuplicateProductError(Exception):
    pass
