from Views import*
from Function import*
from Classes import*


close = True
while close:
    menu_principal()
    menu = input("Digite a opção do menu: ")

    if menu == '1':
        criar_usuario()

    elif menu == '2':
        login()

    elif menu == '3':
        criar_produto()

    elif menu == '4':
        editar_produto()

    elif menu == '5':
        exluir_produto()
        
    elif menu == '6':
        visualizar_prod()

    elif menu == '7':
        pass
    else:
        print('Erro!\nOpção não encontrada.')