from datetime import date
import uuid

def insert_vendedor(session):
    dataAtual = date.today()
    execucao = True
    while execucao:

        nome = input(str("Insira o nome do vendedor: "))
        email = input(str('Insira o endereço de email: '))
        cnpj = input(str("Insira o cnpj: "))
        telefone = input(str('Insira o numero do telefone: '))
        data_cadastro_vendedor = dataAtual.strftime('%d/%m/%Y')

        session.execute("""
                        insert into vendedores
                            (id,nome,email,cnpj,telefone,data_cadastro_vendedor)
                        values
                            (%s,%s,%s,%s,%s,%s)
        """, 
        (str(uuid.uuid1()),nome, email, cnpj, telefone, data_cadastro_vendedor))

        opcao = input(str("Deseja cadastrar outro vendedor ? [s/n] "))

        if opcao.lower() != "s":
            execucao = False