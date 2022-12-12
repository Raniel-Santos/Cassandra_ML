from buscas.buscaVendedor import buscar_vendedores


def excluir_vendedor(session):
    buscar_vendedores(session)

    id_vend = input(str('Insira o ID do vendedor: '))
    session.execute(f"delete from vendedores where id = '{id_vend}'")

    print('Vendedor excluido!')