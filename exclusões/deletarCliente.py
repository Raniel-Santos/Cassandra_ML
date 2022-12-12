from buscas.buscaCliente import buscar_clientes


def excluir_cliente(session):

    buscar_clientes(session)
    id_cliente = input(str('Insira ID do cliente:'))

    session.execute("delete from clientes where id = '{id_cliente}'".format(id_cliente = id_cliente))
    print('Cliente excluido com sucesso!')