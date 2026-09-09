# Acervo - Atividade de Arquitetura de Software

Este repositório foi convertido em um acervo de trabalhos, exercícios e materiais relacionados à disciplina/atividade de Arquitetura de Software.

## Visão geral

- **Objetivo:** centralizar implementações, refatorações e anotações de estudo para consulta e contribuição.
- **Público-alvo:** estudantes, instrutores e mantenedores do acervo.

## Estrutura do repositório

- `AGENTS.md` — diretrizes e práticas para agentes e contribuintes.
- `Arquitetura em Camadas/` — exemplos e código legado (Python) relacionados a arquitetura em camadas.
- `Refatoração Arquitetural/` — atividade TypeScript com `package.json`, fontes e scripts.

## Começando

Clone o repositório:

```bash
git clone https://github.com/gustavosnow/Atividade-01-Arquitetura-de-Software.git
cd Atividade-01-Arquitetura-de-Software
```

## Arquitetura em Camadas — execução

- **Pré-requisitos:** Python >= 3.10
- **Como executar:**

```bash
cd "Arquitetura em Camadas"
# (opcional) criar e ativar virtualenv
python -m venv .venv
.venv\Scripts\activate  # Windows (PowerShell/CMD)
# macOS/Linux: source .venv/bin/activate
python main.py
```

- **Observações:**
	- O exemplo grava/append no arquivo `vendas.txt` dentro da pasta `Arquitetura em Camadas`.
	- Não há dependências externas além de Python 3.10+.
	- Arquivos relevantes: `codigo_legado.py`, `codigo_refatorado.py`, `interfaces.py`, `servico.py`, `repositorios.py`, `notificadores.py`, `main.py`.


Para a pasta TypeScript (se for necessário executar):

```bash
cd "Refatoração Arquitetural"
npm install
# Verifique os scripts disponíveis em package.json
npm run build
npm run dev
```

Observação: `node_modules/` está listado em `.gitignore`; não comite dependências.

## Como contribuir

1. Abra uma issue descrevendo a proposta.
2. Crie uma branch com prefixo `feature/` ou `fix/`.
3. Faça mudanças pequenas e documentadas; inclua exemplos ou testes mínimos quando aplicável.
4. Envie um pull request com referência à issue e descrição das mudanças.

Para alterações arquiteturais maiores, solicite revisão explícita antes de mesclar.

## Boas práticas

- Preserve separação de responsabilidades entre camadas.
- Documente suposições antes de introduzir dependências ou scaffolding.
- Não inclua segredos em texto claro; remova ou sinalize credenciais encontradas.

## Arquivo de diretrizes

Leia `AGENTS.md` antes de aplicar alterações significativas — ele contém convenções e regras de segurança para intervenções automatizadas e humanas.

## Manutenção

- **Mantido por:** proprietário da pasta geral dos trabalhos.
- **Changelog (seleção):**
	- 2026-09-09: Repositório convertido em acervo; adicionado `.gitignore` e `AGENTS.md` central.

## Validação de mensagens de commit

Este repositório valida mensagens de commit automaticamente via GitHub Actions usando `commitlint`.

Para ativar verificação local (opcional):

1. Instale dependências de desenvolvimento no root:

```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional
```

2. (Opcional) Instale e configure `husky` para hooks locais:

```bash
npm install --save-dev husky
npx husky install
npx husky add .husky/commit-msg 'npx --no-install commitlint --edit "$1"'
```

3. Alternativamente, defina hooks locais com `core.hooksPath` apontando para `.githooks/` e crie um script `commit-msg` que chame `npx commitlint --edit "$1"`.

A configuração do `commitlint` está em `commitlint.config.js` e as regras de boas práticas de commits estão em `COMMIT_GUIDELINES.md`.

## Contato

Abra uma issue para dúvidas, sugestões ou solicitações de organização do acervo.
