# Arquitetura RPA Python

Projeto de arquitetura padrão para automações em Python.

## 📑 Sumário

- [Arquitetura RPA Python](#arquitetura-rpa-python)
  - [📑 Sumário](#-sumário)
  - [🗂️ Descrição dos Diretórios da Aplicação](#️-descrição-dos-diretórios-da-aplicação)
    - [App](#app)
    - [App - Auto](#app---auto)
    - [App - Core](#app---core)
    - [App - Database](#app---database)
    - [App - Errors](#app---errors)
    - [App - Interfaces](#app---interfaces)
    - [App - Middleware](#app---middleware)
    - [App - Schemas](#app---schemas)
    - [App - Scripts](#app---scripts)
    - [App - Services](#app---services)
  - [🚀 Ativação e Execução do Projeto](#-ativação-e-execução-do-projeto)
    - [Instalações Necessárias](#instalações-necessárias)
    - [Setup Inicial do Projeto](#setup-inicial-do-projeto)
    - [Execução de Scripts e Ferramentas](#execução-de-scripts-e-ferramentas)
    - [Gerenciamento de Dependências](#gerenciamento-de-dependências)
    - [Qualidade de Código e Segurança](#qualidade-de-código-e-segurança)
    - [Validação Completa (Pipeline de Qualidade)](#validação-completa-pipeline-de-qualidade)
  - [🧪 Cobertura de Testes](#-cobertura-de-testes)


## 🗂️ Descrição dos Diretórios da Aplicação

### App

Pacote principal que contém o núcleo do framework e os robôs.

### App - Auto

Scripts de automação e suporte técnico.

### App - Core

Centraliza toda a inteligência de parâmetros e variáveis de ambiente e configurações públicas.

### App - Database

Camada de infraestrutura para interações com as bases de dados.

### App - Errors

Centraliza as exceções customizadas do projeto.

### App - Interfaces

Armazena as interfaces de contrato (ABC) utilizados pelas classes dos módulos repositories e services.

### App - Middleware

Camada de interceptação que adiciona funcionalidades aos métodos.

### App - Schemas

Armazena os modelos de dados do Pydantic e DTOs utilizadas pelo projeto.

### App - Scripts

Entry points (pontos de entrada) para execução.

### App - Services

Contém a lógica de negócio pura, independente de interfaces ou bancos.


## 🚀 Ativação e Execução do Projeto

### Instalações Necessárias

Caso ainda não possua o uv instalado na máquina:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Setup Inicial do Projeto

O comando uv sync substitui a preparação manual.</br>
Ele cria o ambiente virtual, instala as dependências e configura o projeto em modo editável automaticamente.

```powershell
# Sincroniza o ambiente com o lockfile (Cria .venv e instala tudo)
uv sync

# Garante que o projeto está em modo editável para permitir imports de 'src'
uv pip install -e .
```

### Execução de Scripts e Ferramentas

Os comandos abaixo utilizam os entry points definidos no seu pyproject.toml.</br>
O uv run garante que o comando seja executado dentro do contexto do ambiente virtual.

- Rodar Script de Exemplo:
  
```cmd
uv run exemplo-script
```

- Rodar Orquestrador Mestre:
  
```cmd
uv run mestre-script
```

### Gerenciamento de Dependências

Com o uv, não manipulamos arquivos .txt manualmente para instalar pacotes.

- Adicionar nova biblioteca:

```powershell
uv add <nome_da_biblioteca>
```

- Remover biblioteca:

```powershell
uv remove <nome_da_biblioteca>
```

- Visualizar árvore de dependências:

```powershell
uv tree
```

- Gerar/Atualizar o Lockfile:

```powershell
uv lock
```

- Atualizar o UV:

```powershell
uv self update
```

- Empacota seu código em arquivos .whl (Wheel) ou .tar.gz para distribuição oficial:

```powershell
uv build
```

### Qualidade de Código e Segurança

Centralizamos as validações no Ruff (que substitui Black, Isort, Flake8 e Pylint) e no MyPy.</br>
Para validação de segurança utilizamos o Bandit.</br>
Para idenificar código morto e bibliotecas não utilizadas, utilizamos o Vulture e o Deptry.</br>

- Validações Individuais - Linting (Erros e Boas Práticas):

```powershell
uv run ruff check .
```

- Formatação Automática:

```powershell
uv run ruff format .
```

- Análise de Tipagem Estática (Strict Mode):

```powershell
uv run mypy .
```

- Análise de Segurança (Bandit):

```powershell
uv run bandit -c pyproject.toml -r src
```

- Checagem de Dependências Inúteis (Deptry):

```powershell
uv run deptry .
```

- Checagem de Código Morto:

```powershell
uv run vulture .
```

### Validação Completa (Pipeline de Qualidade)

Para rodar todas as travas de segurança e estilo de uma só vez (recomendado antes de tentar realizar qualquer commit):

```powershell
uv run pre-commit run --all-files
```

</details>

## 🧪 Cobertura de Testes

Utilizamos o Pytest como framework principal de testes devido à sua flexibilidade e suporte a fixtures avançadas.</br>
A cobertura de código é medida para garantir que a lógica do projeto esteja sempre validada.

- Executar todos os testes:

```powershell
uv run pytest
```

Executar um teste específico:

```powershell
uv run pytest tests/unit/test_exemplo_script.py
```

Para não perder tempo rodando toda a suíte após uma correção, use a flag `--lf` (last failed):

```powershell
uv run pytest --lf
```

Para a execução no primeiro erro encontrado.

```powershell
uv run pytest -x
```

Gerar relatório de cobertura em `HTML`:

```powershell
# Abra o arquivo htmlcov/index.html no seu navegador após a execução
uv run pytest --cov=src --cov-report=html
```

---
