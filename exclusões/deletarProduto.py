from buscas.buscaProdutos import busca_produtos


def excluir_produto(session):
    busca_produtos(session)

    id_prod = input(str('Insira o ID do Produto: '))

    session.execute(f"delete from produtos where id = '{id_prod}'")
    print('Produto deletado')