# Diretrizes de mensagens de commit (em português)

Este arquivo define um padrão de mensagens de commit a ser seguido neste acervo. As mensagens devem ser escritas em português e claras para facilitar histórico e revisões.

Formato recomendado

- Estrutura: `<tipo>(escopo): resumo curto`
- Resumo curto: em português, no imperativo, máximo ~50 caracteres.
- Corpo (opcional): explique o "por que" da mudança em mais detalhes.
- Footer (opcional): referências a issues ou breaking changes.

Tipos recomendados (conventional, use o que fizer sentido):

- `feat`: nova funcionalidade
- `fix`: correção de bug
- `docs`: documentação
- `style`: formatação, espaçamento, sem alteração de comportamento
- `refactor`: refatoração de código sem alteração de comportamento
- `perf`: melhoria de desempenho
- `test`: adição/ajuste de testes
- `chore`: tarefas de manutenção (build, config, scripts)

Observações importantes

- Use verbo no imperativo: por exemplo, `Adiciona`, `Corrige`, `Atualiza`.
- Escreva os commits em português; mantenha os tipos como acima (em inglês) se preferir compatibilidade com ferramentas, ou troque por equivalentes em português (ex.: `feat` → `nova`).
- Inclua o escopo quando for relevante: `feat(api): adiciona endpoint de autenticação`.
- Seja sucinto no resumo; use o corpo para detalhes técnicos, referências e justificativas.

Exemplos (em português)

- `feat(auth): adiciona endpoint de login com JWT`
- `fix(ui): corrige overflow no card de usuário`
- `docs: atualiza README com instruções de acervo`
- `refactor(servico): extrai interface para repositório de dados`
- `chore: adiciona .gitignore e regras básicas`

Ferramentas recomendadas

- Use ferramentas de lint de commits (ex.: commitlint) se desejar impor o padrão automaticamente.

Por que isso importa

Mensagens de commit claras e consistentes facilitam revisão de código, geração de changelogs e histórico de decisões. Manter tudo em português ajuda colaboradores que preferem esse idioma e preserva contexto local das tarefas.
