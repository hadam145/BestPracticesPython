# Ukázka ISP – každá třída implementuje jen to, co opravdu potřebuje
from basic_printer import BasicPrinter
from multi_function_printer import MultiFunctionPrinter

if __name__ == "__main__":
    printer = BasicPrinter()
    printer.print_document("Hello.pdf")

    mfp = MultiFunctionPrinter()
    mfp.print_document("Report.pdf")
    mfp.scan_document("Contract.pdf")
