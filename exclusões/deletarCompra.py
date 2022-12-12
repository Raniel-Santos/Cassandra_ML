from buscas.buscaCompras import buscar_compra_id


def excluir_compra(session):
    buscar_compra_id(session)

    id_compra = input(str('Insira o ID da compra: '))
    session.execute(f"delete from compras where id= '{id_compra}'")

    print('Compra Excluida')