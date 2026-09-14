# Arithmetic Operators
from pyscript import display, document


def create_order(e):
    prod1 = document.getElementById("food1")
    prod2 = document.getElementById("food2")
    prod3 = document.getElementById("food3")
    prod4 = document.getElementById("food4")

    # Calculate subtotal by multiplying value by checked status (1 or 0)
    subtotal = float(prod1.value) * prod1.checked
    subtotal = float(prod2.value) * prod2.checked
    subtotal = float(prod3.value) * prod3.checked
    subtotal = float(prod4.value) * prod4.checked
    display(subtotal, target="show")

    # Calculate VAT by getting 12% of the subtotal
    VAT = subtotal * 0.12
    display(VAT, target="show")

    # Calculate total by adding both values
    total = subtotal + VAT
    display(total, target="show")
