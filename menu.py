from departamento import *
def menu_departamento():
    while True:
        print("\n===============================")
        print("\nMenu Departamento:")
        print("1. Inserir Departamento")
        print("2. Listar Departamentos")
        print("3. Atualizar Departamento")
        print("4. Deletar Departamento")
        print("0. Voltar ao Menu Principal")
        print("\n===============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_departamento()
        elif opcao == "2":
            listar_departamentos()
        elif opcao == "3":
            atualizar_departamento()
        elif opcao == "4":
            deletar_departamento()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_departamento()