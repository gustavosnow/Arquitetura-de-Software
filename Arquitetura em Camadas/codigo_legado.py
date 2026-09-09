class ProcessadorVenda:
    def processar(self, cliente: str, valor: float, email_cliente: str):
        #1. Regra de Negócio + Validação
        if valor <= 0:
            raise ValueError("Valor inválido")

        valor_com_desconto = valor * 0.9 if valor > 100 else valor

        #2. Persistência (Acesso a Dados)
        with open("vendas.txt", "a") as f:
            f.write(f"{cliente};{valor_com_desconto}\n")
            print(f"[BD] Venda salva no arquivo para {cliente}")

        #3. Comunicação (Serviço de Terceiros)