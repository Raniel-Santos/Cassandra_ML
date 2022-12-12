import uuid
from datetime import date

from buscas.buscaCliente import buscar_clientes
from buscas.buscaProdutos import busca_produtos

def inserir_compra(session):
    dataAtual = date.today()
    execucao = True

    buscar_clientes(session)
    id_cliente = input(str('Insira o ID do Cliente: '))
    busca = session.execute("select * from clientes where id ='{id_cliente}'".format(id_cliente = id_cliente))

    if busca:
        while execucao:

            busca_produtos(session)
            id_prod = input(str('Insira o ID do Produto: '))
            busca_prod = session.execute("select * from produtos where id = '{id_prod}'".format(id_prod = id_prod))
            data_compra = dataAtual.strftime('%d/%m/%Y')

            if busca_prod:
                for cliente in busca:
                    info_cliente = {'id':cliente.id, 'nome':cliente.nome, 'cpf':cliente.cpf, 'email':cliente.email}

                for produto in busca_prod:
                    info_prod = {'id':produto.id, 'nome':produto.nome, 'preco':produto.preco}
                    info_vend = produto.vendedor
                session.execute("""
                        insert into compras
                            (id, data_compra, total, cliente, produto, vendedor)
                        values
                            (%s,%s,%s,%s,%s,%s)
                """,
                (str(uuid.uuid1()),data_compra, info_prod['preco'], str(info_cliente), str(info_prod), info_vend))

                opcao = input(str("Deseja comprar outro produto ? [s/n] "))

                if opcao.lower() != "s":
                    execucao = False

            else:
                print("Produto não encontrado")

    else:

        print("Cliente não encontrado...")
