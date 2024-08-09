def Adicionar_produto():
    nome = input("Nome do produto: ")
    preço = int(input("Digite o preço do produto: "))
    quantidade = int(input("Digite o preço do produto: "))
    descricao = input("Insira a descrição do produto: ")
    produto = Produto(nome, preço, quantidade, descricao)
    lista_produtos.append(produto)
    

def Excluir_produto():
    codigo = input('Digite o codigo do produto: ')
    i=0
    for produto in lista_produtos:
        if codigo == produto.codigo:
            lista_produtos.pop(i)
            print("O produto foi deletado")
        i+=1
    
