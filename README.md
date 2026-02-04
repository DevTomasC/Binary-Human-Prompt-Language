# BHPL v2 — Binary-Human Prompt Language

**Autor:** Tomas Fernandes Correa  
**Data de criação:** Maio de 2025  
**Licença:** MIT  
**Status:** Em desenvolvimento  

---

## Visão Geral

**BHPL v2 (Binary-Human Prompt Language)** é uma meta-linguagem determinística para **estruturação de prompts complexos**, projetada para atuar como uma **DSL de comando** entre humanos e inteligências artificiais.

Seu foco é transformar linguagem natural em **instruções executáveis**, reduzindo ambiguidade, custo cognitivo e consumo de tokens, enquanto aumenta previsibilidade, reutilização e precisão operacional.

BHPL v2 não é conversacional.  
É **orientada à execução**.

---

## Propósito

A missão da BHPL v2 é **reduzir a complexidade semântica** na interação humano-IA por meio de:

- Sintaxe curta e padronizada  
- Separação explícita entre contexto, regras, ações e saída  
- Execução linear e previsível  
- Falha rápida e controlada  

O padrão é especialmente eficaz em domínios técnicos onde **intenção, regra e ação precisam estar claramente separadas**, como:

- Engenharia de Software  
- Análise e Arquitetura de Sistemas  
- Automação de Fluxos (RPA / n8n / CLI)  
- Análise e Correlação de Dados  
- Suporte Técnico e Infraestrutura  

---

## Conceito Central

BHPL v2 trata prompts como **programas declarativos**.

Cada prompt é composto por:
- **Contexto explícito** (`@ct`, `@ct+`)
- **Blocos semânticos organizacionais** (`#`)
- **Constraints e decisões** (`$`)
- **Ações executáveis** (`;`, `>>`)
- **Diretivas formais de saída** (`@res`, `@uml`, etc.)

O resultado é um pseudo-código humano-legível, porém **facilmente parseável por máquinas**.

---

## Princípios da Linguagem

BHPL v2 é conceitualmente inspirada por:

- **Estruturas Algorítmicas Clássicas**  
  Fluxo sequencial, condicionais, pipelines.

- **Lógica Binária**  
  Relação clara entre comando → execução → saída.

- **Programação Orientada a Objetos**  
  Encapsulamento de contexto, herança incremental (`@ct+`).

- **Linguagens Declarativas e de Script**  
  Shell, YAML, Python, XML, DSLs.

---

## Objetivos de Design (v2)

- Determinismo acima de criatividade  
- Execução acima de explicação  
- Baixo consumo de tokens  
- Sintaxe ortogonal (1 símbolo = 1 função)  
- Fácil integração com agentes, automações e parsers  

---

## Evolução para v2

A versão 2 introduz:
- Diretivas explícitas (`@ct`, `@mode`, `@res`)
- Separação clara entre ação (`;`) e pipeline (`>>`)
- Parametrização nativa (`@res:3`)
- Sintaxe reduzida e mais legível
- Melhor compatibilidade com fine-tuning e agentes IA

---

## Filosofia de Uso

BHPL v2 assume que:

- A IA é um **executor**, não um interlocutor
- Ambiguidade é erro
- Silêncio é melhor que resposta errada
- Estrutura vence linguagem natural

---

## Estado Atual

- Sintaxe v2 definida
- Documentação em expansão
- Uso experimental em automação, suporte técnico e agentes IA
- Parser e ferramentas ainda não oficiais

---

## Licença

MIT — uso livre, modificação permitida, atribuição recomendada.
