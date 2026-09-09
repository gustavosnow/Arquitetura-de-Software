from interfaces import INotificador, IVendaRepository


class VendaService:
    def __init__(self, repositorio: IVendaRepository, notificador: INotificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def processar(self, cliente: str, valor: float, contato: str) -> None:
        if valor <= 0:
            raise ValueError("O valor da venda deve ser maior que zero.")

        valor_final = valor * 0.9 if valor > 100 else valor

        self.repositorio.salvar(cliente, valor_final)

        mensagem = f"Venda de R$ {valor_final:.2f} confirmada!"
        self.notificador.enviar(contato, mensagem)
