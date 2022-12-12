## Listagem geral de Clientes:
def buscar_clientes(session):    
    clientes = session.execute('select * from clientes')

    if clientes:
        print('Listagem dos Clientes...\n')

        for cliente in clientes:
            print('|')
            print(f'| id: {cliente.id}')
            print(f'| nome: {cliente.nome}')
            print(f'| email: {cliente.email}')
            print(f'| cpf: {cliente.cpf}')
            print(f'| data de nascimento: {cliente.data_nascimento}')
            print(f'| telefone: {cliente.telefone}')
            print(f'| endereco: {cliente.endereco}')
            print('|')

    else:
        print("Cliente não encontrado / não existe...")

## Listagem de Cliente por ID:
def buscar_cliente_id(session):

    lista_clientes = session.execute('select * from clientes')

    if lista_clientes:

        for cliente in lista_clientes:

            print('\nListagem dos clientes cadastrados no sistema...\n')
            print(f'| id: {cliente.id}')
            print(f'| nome: {cliente.nome}')
            print(f'| email: {cliente.email}')

        print('\n')
        id_cliente = input(str("Digite o id do cliente: "))
        cliente = session.execute(f"select * from clientes where id = '{id_cliente}'")

        if cliente:

            for usuario in cliente:
                print('\n')
                print(f'| id: {usuario.id}')
                print(f'| nome: {usuario.nome}')
                print(f'| email: {usuario.email}')
                print(f'| cpf: {usuario.cpf}')
                print(f'| data de nascimento: {usuario.data_nascimento}')
                print(f'| telefone: {usuario.telefone}')
                print(f'| endereco: {usuario.endereco}')
                print('\n')
            
        else:
            print("Cliente encontrado...")

    else:
        print("Cliente não encontrado / não existe...")