# Třída vytvořená čistě kvůli odpovědnosti logování (není doménový objekt) – GRASP: Pure Fabrication
class Logger:
    @staticmethod
    def log(message: str):
        print(f"[Logger] {message}")
