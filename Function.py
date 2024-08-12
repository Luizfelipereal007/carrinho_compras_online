# Adicionar Produto
def Adicionar_produto():
    pass

# Excluir Produto
def Exluir_produto():
    posicao = 1
    escolha_produto = input('Digite o id do produto escolhido: ')
    for produto in Loja.lista_produto:
        if len(Loja.lista_produto) > 0:
            if escolha_produto == produto.nome:
                print(f"O Produto na posição {posicao}° é\nNome -->{produto.nome}\tId -->{produto.id}")
                select = input("Deseja excluir?\tsim\tnao")
                if select == 'sim':
                    del produto
                    return 'Foi deletado com sucesso!'
                
                if select == 'nao':
                    pass
                else:
                    return 'Erro!'
        else: 
            return "Lista está vazia.\nAdicione um item!"    
        posicao += 1
    
# Excluir Carrinho
def excluir_carrinho():
    posicao = 1
    for produto in Loja.lista_produto:
        if len(Loja.lista_produto) > 0:
            print(f"O Produto na posição {posicao}° é\nNome -->{produto.nome}\tId -->{produto.id}")
            select = input("Deseja excluir?\tsim\tnao")
            if select == 'sim':
                del produto
                return 'Foi deletado com sucesso!'
            
            if select == 'nao':
                pass
            else:
                return 'Erro!'
            posicao += 1

# Criar Usuario
def criar_usuario():
    nome = input("Digite o seu Nome: ")
    idade = input("Digite a sua Idade: ")
    cpf = input("Digite o seu CPF: ")
    telefone = input("Digite o seu Telefone: ")
    email = input("Digite o seu Email: ")
    senha = input("Digite sua senha: ")
    # Chamada de funcao Salto para cria o id
    Usuario = Usuario(nome,idade,cpf,)