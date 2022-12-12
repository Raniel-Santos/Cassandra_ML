from buscas.buscaCliente import buscar_clientes


def update_cliente(session):
    buscar_clientes(session)
    
    id_cliente = input(str('Insira o ID do Cliente a ser editado: '))
    busca = session.execute(f"select * from clientes where id = '{id_cliente}'")

    if busca:
        execucao = True

        while execucao:
            print('''
                [1] Nome
                [2] Email
                [3] CPF
                [4] Data de Nascimento
                [5] Telefone
                [6] Endereço
                [0] Sair
            ''')
            opcao = input(str('Escolha uma opção acima: '))

            match int(opcao):
                case 1:
                    nome = input(str("Insira o novo nome do cliente: "))
                    session.execute(f"update clientes set nome='{nome}' where id='{id_cliente}'")
                case 2:
                    email = input(str("Insira o novo email do cliente: "))
                    session.execute(f"update clientes set email='{email}' where id='{id_cliente}'")
                case 3:
                    cpf = input(str("Insira o novo cpf do cliente: "))
                    session.execute(f"update clientes set cpf='{cpf}' where id='{id_cliente}'")
                case 4:
                    data_nascimento = input(str("Insira a nova data de nascimento do cliente: "))
                    session.execute(f"update clientes set data_nascimento='{data_nascimento}' where id='{id_cliente}'")
                case 5:
                    telefone = input(str("Insira o novo telefone do cliente: "))
                    session.execute(f"update clientes set telefone='{telefone}' where id='{id_cliente}'")
                case 6:
                    endereco = input(str("Insira o novo endereço do cliente: "))
                    session.execute(f"update clientes set endereco='{endereco}' where id='{id_cliente}'")                   
                case 0:
                    print("\nEdição Salva...\n")
                    execucao = False
                    return
                case _:
                    print("Operação não entendida...")
        else:
            print("\nProduto não encontrado...\n")
            return                 