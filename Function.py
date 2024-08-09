def Adicionar_produto():
    pass
    

def Exluir_produto_carrinho():
    pass
    
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
                

            else:
                return 'Erro!'
            posicao += 1
