import uuid

def inserir_cliente(session):

    print('Iniciando cadastro do usuario...\n')

    nome = input(str('Insira o nome do usuario: '))
    email = input(str('Insira o endereço de email: '))
    cpf = input(str('Insira o numero do cpf: '))    
    data_nascimento = input(str('Insira a data de nascimento: '))
    telefone = input(str('Insira o numero do telefone: '))
    endereco = input(str('Insira o endereço: '))
    
    session.execute("""
                    insert into clientes 
                        (id,nome,email,cpf,data_nascimento,telefone,endereco)
                    values
                        (%s,%s,%s,%s,%s,%s,%s)
                    """, (str(uuid.uuid1()),nome, email, cpf, data_nascimento, telefone, endereco)
                    )

    print('\nCliente cadastrado com sucesso! =)')