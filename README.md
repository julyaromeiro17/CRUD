# Sistema de Gerenciamento de Tarefas (CRUD)

## Descrição

Este projeto consiste no desenvolvimento de um sistema simples de gerenciamento de tarefas utilizando a linguagem **Python** e o banco de dados **SQLite**.

O sistema implementa as quatro operações básicas de um CRUD:

* **Create** – Criar uma nova tarefa
* **Read** – Listar tarefas cadastradas
* **Update** – Atualizar informações de uma tarefa
* **Delete** – Remover uma tarefa do sistema

A aplicação é executada no **terminal**, permitindo que o usuário interaja através de um menu de opções.

---

## Tecnologias Utilizadas

* **Python 3**
* **SQLite**
* **GitHub**
* **GitHub Codespaces**

---

## Estrutura do Projeto

```
projeto-crud-tarefas/
│
├── main.py        # Código principal do sistema
├── tarefas.db     # Banco de dados SQLite (gerado automaticamente)
└── README.md      # Documentação do projeto
```

---

## Banco de Dados

O sistema utiliza um banco de dados SQLite chamado **tarefas.db**.

Tabela criada:

**Tabela: tarefas**

| Campo     | Tipo    | Descrição                                |
| --------- | ------- | ---------------------------------------- |
| id        | INTEGER | Identificador único da tarefa            |
| titulo    | TEXT    | Título da tarefa                         |
| descricao | TEXT    | Descrição da tarefa                      |
| status    | TEXT    | Status da tarefa (pendente ou concluída) |

---

## Funcionalidades

O sistema possui as seguintes funcionalidades:

1. **Criar tarefa**

   * Permite cadastrar uma nova tarefa no banco de dados.

2. **Listar tarefas**

   * Mostra todas as tarefas cadastradas no sistema.

3. **Atualizar tarefa**

   * Permite modificar o título, descrição ou status de uma tarefa existente.

4. **Deletar tarefa**

   * Remove uma tarefa do banco de dados.

---

## Como Executar o Projeto

1. Abra o projeto no **GitHub Codespaces** ou em um ambiente com Python instalado.

2. Execute o arquivo principal:

```
python main.py
```

3. O sistema exibirá um menu com as opções disponíveis.

---

## Exemplo de Menu

```
===== SISTEMA DE TAREFAS =====

1 - Criar tarefa
2 - Listar tarefas
3 - Atualizar tarefa
4 - Deletar tarefa
5 - Sair
```

O usuário deve digitar o número da opção desejada.

---

## Objetivo do Projeto

O objetivo deste projeto é praticar:

* Programação em **Python**
* Manipulação de banco de dados com **SQLite**
* Operações **CRUD**
* Estruturação de um projeto simples
* Uso do **GitHub** para versionamento

---

## Autor

Julya Romeiro Viana
Sthephany Souza
Heitor Baltazar

Projeto desenvolvido para atividade acadêmica.
