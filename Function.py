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
    usuario = Usuario(id, nome, idade, cpf, telefone, email, senha)
    Loja.lista_usuario.append(usuario)

# Adicionar Produto
def criar_produto():
    nome = input("Digite o seu Nome: ")
    preco = input("Digite o Preço do produto: ")
    descricao = input("Digite a Descrição do produto: ")
    codigo = input("Digite o seu Código: ")
    id = id_generate()
    # Chamada de funcao Salto para cria o id
    produto = Produto(id, nome, preco, descricao, codigo)
    Loja.lista_produto.append(produto)

# Editar informacoes usuario
def editar_usuario():
    nome_escolhido = input('Digite o nome da pessoa desejada: ')
    for pessoa in Loja.lista_usuario:
        if len(Loja.lista_usuario) > 0:

            if pessoa.nome == nome_escolhido:
                sub_menu_usuario()
                opcao = input("Digite a opção do menu requisitada: ")

                if opcao.lower() == 'nome':
                    new_nome = input('Digite o novo Nome: ')
                    pessoa.nome = new_nome

                elif opcao.lower() == 'idade':
                    new_idade = input('Digite a nova Idade: ')
                    pessoa.idade = new_idade

                elif opcao.lower() == 'cpf':
                    new_cpf = input('Digite o novo CPF: ')
                    pessoa.cpf = new_cpf

                elif opcao.lower() == 'telefone':
                    new_telefone = input('Digite o novo Telefone: ')
                    pessoa.telefone = new_telefone

                elif opcao.lower() == 'email':
                    new_email = input('Digite o novo Email: ')
                    pessoa.email = new_email

                elif opcao.lower() == 'senha':
                    new_senha = input('Digite a nova Senha: ')
                    pessoa.senha = new_senha

                else:
                    return 'Erro!'
            else:
                return 'Erro!\nPessoa não encontrada.'
        else: 
            return 'Lista vazia!'
        
# Editar informacoes editar 
def editar_produto():
    nome_escolhido = input('Digite o nome do produto desejado: ')
    for produto in Loja.lista_produto:
        if len(Loja.lista_produto) > 0:
            if produto.nome == nome_escolhido:
                sub_menu_produto()
                opcao = input('Digite a opção do menu requisitada: ')

                if opcao.lower() == 'nome':
                    new_nome = input('Digite o novo Nome:')
                    produto.nome = new_nome
                    
                elif opcao.lower() == 'preco':
                    new_preco = input('Digite o novo Nome:')
                    produto.preco = new_preco

                elif opcao.lower() == 'descricao':
                    new_descricao = input('Digite o novo Nome:')
                    produto.descricao = new_descricao

                elif opcao.lower() == 'codigo':
                    new_codigo = input('Digite o novo Nome:')
                    produto.codigo = new_codigo

                else:
                    return 'Erro!'
            else:
                return 'Erro!\nProduto não encontrado.'
        else:
            return 'Lista vazia!'
        
def login():
    usuario = input('Digite seu nome de Usuário: ')
    senha = input('Digite sua senha: ')
    validar_usuario(usuario)
    validar_senha(senha)
    if usuario == 'ADM':
        return 'ADM'

def validar_usuario(username):
    for pessoa in Loja.lista_usuario:
        if pessoa.nome != username:
            return 'Erro!\nNome incorreto!'
        continue

def validar_senha(password):
    for pessoa in Loja.lista_usuario:
        if pessoa.senha != password:
            return "Erro!\nSenha incorreta!"
        continue
    
    
