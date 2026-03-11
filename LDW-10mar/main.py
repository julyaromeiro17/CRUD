import sqlite3

# conexão com banco
conn = sqlite3.connect("tarefas.db")
cursor = conn.cursor()

# criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    status TEXT
)
""")

conn.commit()


# validação de status
def validar_status(status):
    status = status.lower()
    if status not in ["pendente", "concluida"]:
        print("Status inválido! Use 'pendente' ou 'concluida'.")
        return False
    return True


# CREATE
def criar_tarefa():
    print("\n--- Criar Nova Tarefa ---")

    titulo = input("Título: ").strip()

    if titulo == "":
        print("O título não pode ser vazio.")
        return

    descricao = input("Descrição: ")
    status = input("Status (pendente/concluida): ")

    if not validar_status(status):
        return

    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)",
        (titulo, descricao, status)
    )

    conn.commit()
    print("✅ Tarefa criada com sucesso!")


# READ
def listar_tarefas():
    print("\n--- Lista de Tarefas ---")

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for t in tarefas:
        print(f"""
ID: {t[0]}
Título: {t[1]}
Descrição: {t[2]}
Status: {t[3]}
-------------------------
""")


# BUSCA POR NOME
def buscar_tarefa():
    nome = input("Digite o nome da tarefa: ")

    cursor.execute(
        "SELECT * FROM tarefas WHERE titulo LIKE ?",
        (f"%{nome}%",)
    )

    tarefas = cursor.fetchall()

    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    for t in tarefas:
        print(f"""
ID: {t[0]}
Título: {t[1]}
Descrição: {t[2]}
Status: {t[3]}
-------------------------
""")


# UPDATE
def atualizar_tarefa():
    listar_tarefas()

    id_tarefa = input("ID da tarefa para atualizar: ")

    titulo = input("Novo título: ")
    descricao = input("Nova descrição: ")
    status = input("Novo status (pendente/concluida): ")

    if not validar_status(status):
        return

    cursor.execute(
        """
        UPDATE tarefas
        SET titulo=?, descricao=?, status=?
        WHERE id=?
        """,
        (titulo, descricao, status, id_tarefa)
    )

    conn.commit()
    print("✏️ Tarefa atualizada!")


# DELETE
def deletar_tarefa():
    listar_tarefas()

    id_tarefa = input("ID da tarefa para deletar: ")

    cursor.execute("DELETE FROM tarefas WHERE id=?", (id_tarefa,))
    conn.commit()

    print("🗑️ Tarefa removida!")


# MENU MELHORADO
def menu():
    while True:

        print("""
==============================
      GERENCIADOR DE TAREFAS
==============================

1 - Criar tarefa
2 - Listar tarefas
3 - Buscar tarefa
4 - Atualizar tarefa
5 - Deletar tarefa
6 - Sair

==============================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            buscar_tarefa()

        elif opcao == "4":
            atualizar_tarefa()

        elif opcao == "5":
            deletar_tarefa()

        elif opcao == "6":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


menu()

conn.close()