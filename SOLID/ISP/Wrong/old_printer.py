# Starší tiskárna – je nucena implementovat i scan, který neumí
from machine import Machine

class OldPrinter(Machine):
    def print_document(self, document: str):
        print(f"[OldPrinter] Printing: {document}")

    def scan_document(self, document: str):
        raise NotImplementedError("OldPrinter does not support scanning")
