# Tiskárna, která umí pouze tisknout – není nucena implementovat scan
from printer import Printer

class BasicPrinter(Printer):
    def print_document(self, document: str):
        print(f"[BasicPrinter] Printing: {document}")
