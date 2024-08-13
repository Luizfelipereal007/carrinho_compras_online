from Classes import*
from Views import*

import random 
import string 

def id_generate():
    id = ''.join([random.choice(string.ascii_letters 
    + string.digits) for n in range(32)]) 
    print(id)


# Excluir Produto
def exluir_produto():
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
    id = id_generate()
    # Chamada de funcao Salto para cria o id
    usuario = Usuario(nome, idade, cpf, telefone, email, senha, id)
    Loja.lista_usuario.append(usuario)

# Adicionar Produto
def criar_produto():
    nome = input("Digite o seu Nome: ")
    preco = input("Digite o Preço do produto: ")
    descricao = input("Digite a Descrição do produto: ")
    codigo = input("Digite o seu Código: ")
    id = id_generate()
    # Chamada de funcao Salto para cria o id
    produto = Produto(nome, preco, descricao, codigo, id)
    Loja.lista_produto.append(produto)
