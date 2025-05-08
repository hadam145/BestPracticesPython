# Třída, která podporuje tisk i skenování – skládá rozhraní
from printer import Printer
from scanner import Scanner

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document: str):
        print(f"[MFP] Printing: {document}")

    def scan_document(self, document: str):
        print(f"[MFP] Scanning: {document}")
