from interfaces import INotificador


class NotificadorEmail(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-MAIL] Enviando para {destinatario}: {mensagem}")


class NotificadorSMS(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[SMS] Enviando para {destinatario}: {mensagem}")
