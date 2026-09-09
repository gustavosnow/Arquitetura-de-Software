from pathlib import Path

from interfaces import IVendaRepository


class VendaArquivoRepository(IVendaRepository):
    def __init__(self, caminho_arquivo: str = "vendas.txt") -> None:
        pasta_atual = Path(__file__).resolve().parent
        self.caminho_arquivo = str(pasta_atual / caminho_arquivo)

    def salvar(self, cliente: str, valor: float) -> None:
        with open(self.caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(f"{cliente}; {valor}\n")
        print(f"[ARQUIVO] Venda de {cliente} salva em '{self.caminho_arquivo}'.")


class VendaMemoriaRepository(IVendaRepository):
    def __init__(self) -> None:
        self.vendas: list[dict[str, float | str]] = []

    def salvar(self, cliente: str, valor: float) -> None:
        self.vendas.append({"cliente": cliente, "valor": valor})
        print(f"[MEMÓRIA] Venda de {cliente} adicionada à lista interna.")
