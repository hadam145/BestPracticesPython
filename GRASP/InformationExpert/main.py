# Ukázka GRASP principu Information Expert – výpočet provádí ten, kdo má potřebná data
from invoice import Invoice
from item import Item

if __name__ == "__main__":
    invoice = Invoice()
    invoice.add_item(Item("Notebook", 25000, 1))
    invoice.add_item(Item("Myš", 800, 2))

    print(f"Celková cena: {invoice.calculate_total():.2f} Kč")
