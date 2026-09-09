from abc import ABC, abstractmethod
from pathlib import Path


# =========================================================================
# 1. Crie as Abstrações (DIP)
# =========================================================================
class INotificador(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str) -> None:
        pass


class IVendaRepository(ABC):
    @abstractmethod
    def salvar(self, cliente: str, valor: float) -> None:
        pass


# =========================================================================
# 2. Crie as Implementações Concretas
# =========================================================================
class NotificadorEmail(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[E-MAIL] Enviando para {destinatario}: {mensagem}")


class NotificadorSMS(INotificador):
    def enviar(self, destinatario: str, mensagem: str) -> None:
        print(f"[SMS] Enviando para {destinatario}: {mensagem}")


class VendaArquivoRepository(IVendaRepository):
    def __init__(self, caminho_arquivo: str = "vendas.txt") -> None:
        pasta_atual = Path(__file__).resolve().parent
        self.caminho_arquivo = str(pasta_atual / caminho_arquivo)

    def salvar(self, cliente: str, valor: float) -> None:
        with open(self.caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(f"{cliente};{valor}\n")
        print(f"[ARQUIVO] Venda de {cliente} salva em '{self.caminho_arquivo}'.")


class VendaMemoriaRepository(IVendaRepository):
    def __init__(self) -> None:
        self.vendas: list[dict[str, float | str]] = []

    def salvar(self, cliente: str, valor: float) -> None:
        self.vendas.append({"cliente": cliente, "valor": valor})
        print(f"[MEMÓRIA] Venda de {cliente} adicionada à lista interna.")


# =========================================================================
# 3. Aplique o SRP na Camada de Negócio
# =========================================================================
class VendaService:
    def __init__(self, repositorio: IVendaRepository, notificador: INotificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def processar(self, cliente: str, valor: float, contato: str) -> None:
        # Validação
        if valor <= 0:
            raise ValueError("O valor da venda deve ser maior que zero.")

        # Regra de negócio: 10% de desconto para compras acima de R$ 100
        valor_final = valor * 0.9 if valor > 100 else valor

        # Orquestração do fluxo
        self.repositorio.salvar(cliente, valor_final)
        
        mensagem = f"Venda de R$ {valor_final:.2f} confirmada!"
        self.notificador.enviar(contato, mensagem)