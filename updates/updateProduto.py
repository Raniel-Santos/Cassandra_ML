from buscas.buscaProdutos import busca_produtos

def update_produto(session):
    busca_produtos(session)
    id_produto = input(str('Insira o ID do Produto a ser editado: '))
    busca = session.execute(f"select * from produtos where id = '{id_produto}'")

    if busca:
        execucao = True

        while execucao:
            print('''
                [1] Nome
                [2] Descricao
                [3] Preço
                [4] Quantidade
                [0] Sair
            ''')
            opcao = input(str('Escolha uma opção acima: '))

            match int(opcao):
                        case 1:
                            nome = input(str("Insira o novo nome do produto: "))
                            session.execute(f"update produtos set nome='{nome}' where id='{id_produto}'")
                        case 2:
                            descricao = input(str("Insira a nova descricao do produto: "))
                            session.execute(f"update produtos set descricao='{descricao}' where id='{id_produto}'")
                        case 3:
                            preco = input(str("Insira o novo preço do produto: "))
                            session.execute(f"update produtos set preco='{preco}' where id='{id_produto}'")
                        case 4:
                            quantidade = input(str("Insira a nova quantidade de produtos em estoque: "))
                            session.execute(f"update produtos set quantidade='{quantidade}' where id='{id_produto}'")
                        case 0:
                            print("\nEdição Salva...\n")
                            execucao = False
                            return
                        case _:
                            print("Operação não entendida...")

        else:
            print("\nProduto não encontrado...\n")
            return      