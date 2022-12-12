import json

def busca_produtos(session):
    produtos = session.execute("select * from produtos")

    if produtos:
        print("Todos os Produtos cadastrados:")
        for produto in produtos:
            vendedor = json.loads(produto.vendedor.replace("\'", "\""))
            print("|")
            print(f'| id: {produto.id}')
            print(f'| Nome: {produto.nome}')
            print(f'| Descricao: {produto.descricao}')
            print(f'| Preço: {produto.preco}')
            print(f'| Quantidade de produtos em estoque: {produto.quantidade}')
            print(f'| Data de postagem do produto: {produto.data_postagem}')
            print("| Informações do vendedor: {nome}".format(
                nome = vendedor['nome']
            ))

    else:
        print("Produto não encontrado / não existe...")


def buscar_produto_id(session):
    lista_prod = session.execute("select * from produtos")

    if lista_prod:
        for produto in lista_prod:
            print("\nProdutos cadastrados no sistema...\n")
            print(f'| id: {produto.id}')
            print(f'| Nome: {produto.nome}')
            print(f'| Preço: {produto.preco}')

        print('\n')
        id_produto = input(str("Insira o ID do produto: "))
        produto = session.execute(f"select * from produtos where id = '{id_produto}'")
    
        if produto:
    
            for prod in produto:
                vendedor = json.loads(prod.vendedor.replace("\'", "\""))
                print('\n')
                print(f'| id: {prod.id}')
                print(f'| Nome: {prod.nome}')
                print(f'| Descricao: {prod.descricao}')
                print(f'| Preço: {prod.preco}')
                print(f'| Quantidade de produtos em estoque: {prod.quantidade}')
                print(f'| Data de postagem do produto: {prod.data_postagem}')
                print("| Informações do vendedor: {nome}".format(
                    nome = vendedor['nome']
                ))
                print('\n')

            else:    
                print("Produto Encontrado")
        else:
            print("Nenhum produto encontrado...")