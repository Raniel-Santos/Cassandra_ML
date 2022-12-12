#Listagem geral de Vendedores:
def buscar_vendedores(session):
    vendedores = session.execute('select * from vendedores')

    if vendedores:
        print('Vendedores ...\n')

        for vend in vendedores:
            print('|')
            print(f'| id: {vend.id}')
            print(f'| nome: {vend.nome}')
            print(f'| email: {vend.email}')
            print(f'| cnpj: {vend.cnpj}')
            print(f'| telefone: {vend.telefone}')
            print('|')

    else:
        print("Vendedor não encontrado / não existe...")

##Listagem de Vendedores por ID:
def buscar_vendedor_id(session):
    lista_vendedores = session.execute('select * from vendedores')

    if lista_vendedores:

        for vendedor in lista_vendedores:

            print("\nTodos os Vendedores Cadastrados...")
            print(f'| id: {vendedor.id}')
            print(f'| nome: {vendedor.nome}')
            print(f'| email: {vendedor.email}')

        print('\n')
        id_vendedor = input(str("Digite o id do vendedor: "))
        vendedor = session.execute(f"select * from vendedores where id = '{id_vendedor}'")

        if vendedor:

            for vend in vendedor:
                print('\n')
                print(f'| id: {vend.id}')
                print(f'| nome: {vend.nome}')
                print(f'| email: {vend.email}')
                print(f'| cnpj: {vend.cnpj}')
                print(f'| telefone: {vend.telefone}')
                print('\n')

        else:
            print("Vendedor encontrado...")

    else:
        print("Vendedor não encontrado / não existe...")