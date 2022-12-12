import json

from buscas.buscaVendedor import buscar_vendedores


def update_vendedor(session):
    buscar_vendedores(session)

    id_vend = input(str('Insira o ID do vendedor a ser editado: '))
    busca = session.execute(f"select * from vendedores where id = '{id_vend}'")

    if busca:
        nome = input(str("Insira o novo nome do vendedor: "))
        email = input(str('Insira o novo endereço de email: '))
        cnpj = input(str("Insira o novo numero do cnpj: "))
        telefone = input(str('Insira o novo numero do telefone: '))
    
        prod_cadastrados = session.execute('select * from produtos')

        for produto in prod_cadastrados:
            
            vendedor = json.loads(produto.vendedor.replace("\'", "\""))
            if vendedor['id'] == id_vend:
                vendedor['nome'] = nome
                vendedor['email'] = email
                vendedor['cnpj'] = cnpj
                vendedor['telefone'] = telefone

                session.execute(f"delete from produtos where id='{produto.id}'")
                session.execute("""
                        insert into produtos
                            (id, nome, descricao, preco, quantidade, data_postagem, vendedor )
                        values
                            (%s,%s,%s,%s,%s,%s,%s)
                """,
                (produto.id,produto.nome, produto.descricao, produto.preco, produto.quantidade, produto.data_postagem, str(vendedor)))

        session.execute(f"update vendedores set nome='{nome}', email='{email}', cnpj='{cnpj}', telefone='{telefone}' where id = '{id_vend}'")

    else:
        print("\nVendedor não encontrado...\n")
        return