from Views import *
from Classes import *
def Adicionar_produto():
    nome = input("Nome do produto: ")
    preço = int(input("Digite o preço do produto: "))
    quantidade = int(input("Digite o preço do produto: "))
    descricao = input("Insira a descrição do produto: ")
    id_produto = int(input("Digite o id do produto: "))
    produto = Produto(nome, preço, quantidade,descricao, id_produto)
    Loja.lista_produto.append(produto)
    

def Excluir_produto():
    codigo = input('Digite o codigo do produto: ')
    i=0
    for produto in listar_produtos:
        if codigo == produto.codigo:
            Loja.lista_produto.pop(i)
            print("O produto foi deletado")
        i+=1
    

