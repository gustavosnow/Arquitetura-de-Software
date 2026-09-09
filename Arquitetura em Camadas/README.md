# Arquitetura em Camadas

Este diretório contém exemplos em Python que ilustram conceitos de arquitetura em camadas, incluindo versão legada e refatorada.

## Arquivos principais

- `main.py` — pequena aplicação de exemplo que demonstra uso dos repositórios e notificadores.
- `interfaces.py` — definições de interfaces/contratos (`INotificador`, `IVendaRepository`).
- `repositorios.py` — implementações de persistência (`VendaArquivoRepository`, `VendaMemoriaRepository`).
- `notificadores.py` — implementações de notificação (`NotificadorEmail`, `NotificadorSMS`).
- `servico.py` — lógica de negócio (`VendaService`).
- `codigo_legado.py`, `codigo_refatorado.py` — exemplos de código para estudo e comparação.
- `vendas.txt` — arquivo de saída gerado quando se usa `VendaArquivoRepository`.

## Pré-requisitos

- Python 3.10 ou superior (uso de anotações de tipo modernos).

## Como executar

1. Abra um terminal e vá para a pasta do projeto:

```bash
cd "Arquitetura em Camadas"
```

2. (Opcional) criar e ativar um ambiente virtual:

Windows (PowerShell/CMD):

```powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Execute o exemplo:

```bash
python main.py
```

## Observações

- O script `main.py` grava entradas em `vendas.txt` quando `VendaArquivoRepository` é usado. Se quiser executar múltiplas vezes sem acumular dados, remova/renomeie `vendas.txt` antes de rodar.
- Não há dependências externas; apenas Python 3.10+.

## Objetivo

Fornecer um conjunto de exemplos simples para estudo de separação de responsabilidades em camadas e para comparar implementações legadas e refatoradas.
