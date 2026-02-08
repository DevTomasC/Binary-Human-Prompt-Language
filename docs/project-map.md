```md
# Project Map — Binary Human Prompt Language (BHPL)

Mapa estrutural do repositório.

```

Binary-Human-Prompt-Language/
├── agents/
│   ├── compilers/
│   │   └── n8n-workflow-generator.MD
│   ├── diagnostics/
│   │   └── log-bug-fixer.md
│   ├── meta/
│   │   └── prompt-maker.MD
│   └── runtime/
│       ├── logic-shell.md
│       └── open-shell.md
│
├── docs/
│   ├── LICENSE
│   └── README.md
│
├── syntax/
│   ├── v1/
│   │   └── syntax.v1.md
│   └── v2/
│       └── syntax.v2.md
│
└── tests/
└── v1/
├── alg-binario/
│   ├── hello-output-ai.py
│   └── hello-user-input.txt
├── planilha/
│   ├── ai-out.py
│   └── user-promp.txt
└── uml-ascii/
├── email.txt
├── ia-answer.txt
└── user-asks-uml.txt

```

## Leitura Rápida

- **agents/**: agentes cognitivos, separados por responsabilidade
  - `runtime`: execução textual determinística
  - `meta`: geração de prompts & abstrações correlatas
  - `compilers`: compiladores de representação (ex: n8n)
  - `diagnostics`: análise e correção de erros
- **syntax/**: definição da DSL, versionada
- **tests/**: testes organizados por versão da sintaxe
- **docs/**: documentação institucional

Estado: consistente, modular, escalável.
```
