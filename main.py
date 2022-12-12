from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from buscas.buscaCliente import buscar_cliente_id, buscar_clientes
from buscas.buscaCompras import buscar_compra_id, buscar_compras
from buscas.buscaProdutos import busca_produtos, buscar_produto_id
from buscas.buscaVendedor import buscar_vendedor_id, buscar_vendedores
from exclusões.deletarCliente import excluir_cliente
from exclusões.deletarCompra import excluir_compra
from exclusões.deletarProduto import excluir_produto
from exclusões.deletarVendedor import excluir_vendedor

##Import de Componentes
from inserts.insertCliente import inserir_cliente
from inserts.insertCompra import inserir_compra
from inserts.insertProduto import inserir_produtos
from inserts.insertVendedor import insert_vendedor

cloud_config= {
        'secure_connect_bundle': 'secure-connect-cassandra.zip'
}
auth_provider = PlainTextAuthProvider('dPWjTtUAwrbQdoKqtljJvdSQ', 'YZQZE8zMMsmvhTSlnpleMPTNU,7Jzx.HhtqC.ZE4p1ezHM1zJ1ovssgLPq4dGGZsC+ex4xHXRA8BAcJ51EBakUFSa3p55+yRghOZQB+r-8KvUQz2aQv_kvXOD.59aJCZ')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')

row = session.execute("select release_version from system.local").one()
if row:
    print("Conexão com Cassandra realizada com sucesso!")
    execucao = True
    
    while execucao:
        
        print('''
                Bem-Vindo Usuário, selecione uma opção:
                [1] Cadastrar Clientes
                [2] Cadastrar Vendedor
                [3] Cadastrar Produtos
                [4] Cadastrar Compras
                [5] Buscar Clientes
                [6] Buscar Cliente por ID
                [7] Buscar Vendedor
                [8] Buscar Vendedor por ID
                [9] Buscar Produtos
                [10] Buscar Produtos por ID
                [11] Buscar Compras
                [12] Buscar Compras por ID
                [13] Excluir Cliente
                [14] Excluir Vendedor
                [15] Excluir Produto
                [16] Excluir Compra
            ''')
        
        opcao = input(str('Escolha uma das opções acima: '))
        match (int(opcao)):
            case 1:
                inserir_cliente(session)
            case 2:
                insert_vendedor(session)
            case 3:
                inserir_produtos(session)
            case 4:
                inserir_compra(session)           
            case 5:
                buscar_clientes(session)
            case 6:
                buscar_cliente_id(session)
            case 7:
                buscar_vendedores(session)
            case 8:
                buscar_vendedor_id(session)
            case 9:
                busca_produtos(session)
            case 10:
                buscar_produto_id(session)                  
            case 11:
                buscar_compras(session)  
            case 12:
                buscar_compra_id(session)
            case 13:
                excluir_cliente(session)
            case 14:
                excluir_vendedor(session)
            case 15:
                excluir_produto(session)
            case 16:
                excluir_compra(session)
            # case 0:
                print('Até a próxima =)')
                execucao = False
            case _:
                print("Operação não entendida...")

else:
    print("Erro! Contate um ADM para resolver!")
