from message_sender import MessageSender
# Klientská třída, která používá IMessageSender
class EmailSender:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, to: str, subject: str, body: str):
        print("[Client] Preparing to send message...")
        self.sender.send_message(to, subject, body)
