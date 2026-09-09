from pathlib import Path


class ProcessadorVenda:
    def processar(self, cliente: str, valor: float, email_cliente: str):
        #1. Regra de Negócio + Validação
        if valor <= 0:
            raise ValueError("Valor inválido")

        valor_com_desconto = valor * 0.9 if valor > 100 else valor

        #2. Persistência (Acesso a Dados)
        caminho_arquivo = Path(__file__).resolve().parent / "vendas.txt"
        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(f"{cliente};{valor_com_desconto}\n")
            print(f"[BD] Venda salva no arquivo para {cliente}")

        #3. Comunicação (Serviço de Terceiros)
        print(f"[E-MAIL] Enviando e-mail para {email_cliente}: Venda de R$ {valor_com_desconto:.2f} confirmada!")