# Ukázka porušení ISP – klient musí implementovat zbytečné metody
from old_printer import OldPrinter

if __name__ == "__main__":
    printer = OldPrinter()
    printer.print_document("Hello.pdf")
    printer.scan_document("X.pdf")  # způsobí výjimku
