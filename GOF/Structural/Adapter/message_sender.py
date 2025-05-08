from abc import ABC, abstractmethod
# Rozhraní očekávané klientem - cílové rozhraní
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, to: str, subject: str, body: str):
        pass
