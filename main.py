from pyscript import display, document

# Arithmetic Operators

def create_order(e):
    prod1 = document.getElementById("food1")
    prod2 = document.getElementById("food2")
    prod3 = document.getElementById("food3")
    prod4 = document.getElementById("food4")

    # Calculate the subtotal
    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked
    display(f'The subtotal is ₱{subtotal:.2f}', target="show")

    # Calculate the VAT
    VAT = subtotal * 0.12
    display(f'The VAT is ₱{VAT:.2f}', target="show")

    # Calculate the total
    total = subtotal + VAT
    display(f'The total amount is ₱{total:.2f}', target="show")
