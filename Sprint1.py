# CRM Social - Nuvem do Bem
# Simulação em Python para Sprint 1

# Listas para armazenar os dados
dentistas = []
patrocinadores = []
atendimentos = []

# Função para cadastrar dentista voluntário
def cadastrarDentista():
    print("\n--- Cadastro de Dentista Voluntário ---")
    nome = input("Nome completo: ")
    cidade = input("Cidade de atuação: ")
    especialidade = input("Especialidade: ")
    dentista = {"nome": nome, "cidade": cidade, "especialidade": especialidade}
    dentistas.append(dentista)
    print(f"\nDentista {nome} cadastrado com sucesso!\n")

# Função para cadastrar patrocinador
def cadastrarPatrocinador():
    print("\n--- Cadastro de Patrocinador ---")
    nome = input("Nome da empresa ou pessoa: ")
    tipo = input("Tipo de apoio (financeiro / material): ")
    valor = input("Descrição do apoio: ")
    patrocinador = {"nome": nome, "tipo": tipo, "valor": valor}
    patrocinadores.append(patrocinador)
    print(f"\nPatrocinador {nome} cadastrado com sucesso!\n")

# Função para registrar um atendimento
def registrarAtendimento():
    print("\n--- Registro de Atendimento ---")
    nome_dentista = input("Nome do dentista responsável: ")
    beneficiario = input("Nome do beneficiário atendido: ")
    procedimento = input("Procedimento realizado: ")
    data = input("Data do atendimento (DD/MM/AAAA): ")
    atendimento = {
        "dentista": nome_dentista,
        "beneficiario": beneficiario,
        "procedimento": procedimento,
        "data": data
    }
    atendimentos.append(atendimento)
    print(f"\nAtendimento de {beneficiario} registrado com sucesso!\n")

# Função para listar cadastros
def listarRegistros():
    print("\n--- Relatório de Registros ---")
    print(f"\nTotal de dentistas: {len(dentistas)}")
    print(f"Total de patrocinadores: {len(patrocinadores)}")
    print(f"Total de atendimentos: {len(atendimentos)}\n")

    if atendimentos:
        print("Últimos atendimentos:")
        for a in atendimentos[-3:]:  # mostra os 3 mais recentes
            print(f"- {a['beneficiario']} atendido por {a['dentista']} ({a['procedimento']} em {a['data']})")
    else:
        print("Nenhum atendimento registrado ainda.")
    print()

# Função principal (menu)
def menu():
    while True:
        print("========== CRM SOCIAL - TURMA DO BEM ==========")
        print("1 - Cadastrar Dentista Voluntário")
        print("2 - Cadastrar Patrocinador")
        print("3 - Registrar Atendimento")
        print("4 - Listar Registros")
        print("5 - Sair")
        print("===============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrarDentista()
        elif opcao == "2":
            cadastrarPatrocinador()
        elif opcao == "3":
            registrarAtendimento()
        elif opcao == "4":
            listarRegistros()
        elif opcao == "5":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

# Execução do programa
menu()
