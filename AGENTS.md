# AGENTES

**Localização:** este arquivo foi movido para a pasta geral dos trabalhos do usuário. As diretrizes aqui descrevem o comportamento esperado de agentes (humanos ou automáticos) ao trabalhar em atividades que residem nesta pasta ou que usam seus artefatos.

Visão geral

- **Objetivo:** orientar contribuições, exploração e intervenções automatizadas em repositórios de atividades de arquitetura, especialmente quando o workspace estiver incompleto ou for um exercício acadêmico.
- **Escopo:** recomendações aplicam-se a projetos pequenos e em evolução; não substituem um README ou documentação específica do projeto.

Convenções de trabalho

- **Pequenas mudanças:** prefira alterações mínimas e explícitas que atendam à intenção do usuário.
- **Conformidade:** siga as convenções e organização já presentes no repositório antes de introduzir novos padrões.
- **Separação de camadas:** mantenha apresentação, lógica de negócio, persistência e infraestrutura separadas quando possível.
- **Evitar suposições:** não imponha uma stack completa sem autorização—pergunte antes de criar dependências ou scaffolding.

Descoberta inicial (checklist)

1. Verifique a presença de `README.md`, arquivos de configuração (por exemplo, `package.json`, `pyproject.toml`, `tsconfig.json`) e exemplos existentes.
2. Identifique a linguagem/stack e o padrão arquitetural predominante.
3. Procure scripts de build/test em `package.json` ou equivalentes e execute apenas comandos seguros e documentados.
4. Se faltar documentação, documente brevemente as suposições antes de avançar.

Regras de segurança e comportamento para agentes de IA

- **Sem refatorações globais sem aprovação:** evite mudanças amplas (migrações de framework, reescritas) sem tarefa explícita ou revisão humana.
- **Não afirmar resultados não verificados:** só declare build/tests como bem-sucedidos se você executou e verificou os comandos relevantes.
- **Pedir esclarecimentos:** quando a implementação estiver ausente ou ambígua, peça instruções claras ao mantenedor antes de tomar decisões estruturais.
- **Privacidade e segredos:** não introduza, registre ou expanda arquivos que contenham segredos; sinalize se encontrar credenciais em texto claro.

Fluxo de contribuição sugerido

1. Abra uma issue descrevendo a intenção (se aplicável).
2. Faça alterações pequenas em branch separado e crie um pull request com descrição clara.
3. Inclua testes ou exemplos mínimos quando relevante.
4. Peça revisão explícita para mudanças arquiteturais.

Atualização de referências e localização

- Se este arquivo for copiado ou referenciado por repositórios individuais, prefira apontar para a versão central na pasta geral.
- Ao mover este arquivo novamente, atualize o cabeçalho `Localização` com o novo caminho e registre no changelog abaixo.

Manutenção e contato

- **Mantido por:** proprietário da pasta geral dos trabalhos (geralmente o usuário que organizou a pasta).
- **Como reportar problemas:** abra uma issue no repositório correspondente ou contacte o mantenedor descrito no `README.md` do workspace.

Registro de alterações

- 2026-09-09: Conteúdo revisado para refletir que o arquivo está na pasta geral dos trabalhos; diretrizes clarificadas.

Notas finais

Este documento busca equilibrar segurança e agilidade em ambientes de aprendizado ou exercício. Se quiser, posso:

- atualizar referências em outros arquivos para apontarem para este `AGENTS.md` central;
- gerar um README mínimo para o workspace;
- criar um checklist de verificação automatizável (script) para início rápido.

Escolha uma ação e eu executo.
