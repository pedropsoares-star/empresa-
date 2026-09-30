from banco import conectar

def inserir_departamento():
    nome = input("Digite o nome do departamento: ")
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO departamento (nome) VALUES (%s)"
    cursor.execute(sql, (nome,))
    conexao.commit()
    cursor.close()
    print("Departamento inserido com sucesso!")

def listar_departamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM departamento"
    cursor.execute(sql)
    departamentos = cursor.fetchall()

    print("\nDepartamentos:")
    for departamento in departamentos:
        print(f"ID: {departamento[0]}, Nome: {departamento[1]}")

    cursor.close()

def atualizar_departamento():
    listar_departamentos()
    id_departamento = input("Digite o ID do departamento que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do departamento: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE departamento SET nome = %s WHERE id = %s"
    cursor.execute(sql, (novo_nome, id_departamento))
    conexao.commit()
    cursor.close()
    print("Departamento atualizado com sucesso!")

def deletar_departamento():
    listar_departamentos()
    id_departamento = input("Digite o ID do departamento que deseja deletar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM departamento WHERE id = %s"
    cursor.execute(sql, (id_departamento,))
    conexao.commit()
    cursor.close()
    print("Departamento deletado com sucesso!")
