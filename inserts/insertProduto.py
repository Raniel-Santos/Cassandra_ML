from datetime import date
import uuid

from buscas.buscaVendedor import buscar_vendedores

def inserir_produtos(session):
    dataAtual = date.today()
    execucao = True

    buscar_vendedores(session)

    id_vend = input(str('Insira o ID do vendendor: '))
    busca = session.execute("select * from vendedores where id = '{id_vend}'".format(id_vend = id_vend))

    for vendedor in busca:
        print("Vendedor...")
        info = {'id': vendedor.id, 'nome': vendedor.nome}
    while execucao:
        nome = input(str("Insira o nome do produto: "))
        descricao = input(str("Insira a descrição: "))
        preco = input(str("Insira o preço: "))
        quantidade = input(str("Insira a quantidade em estoque: "))
        data_postagem = dataAtual.strftime('%d/%m/%Y')

        session.execute("""
                insert into produtos
                    (id, nome, descricao, preco, quantidade, data_postagem, vendedor )
                values
                    (%s,%s,%s,%s,%s,%s,%s)
        """,
        (str(uuid.uuid1()),nome, descricao, preco, quantidade, data_postagem, str(info)))

        opcao = input(str("Deseja cadastrar outro produto ? [s/n] "))

        if opcao.lower() != "s":
            execucao = False
