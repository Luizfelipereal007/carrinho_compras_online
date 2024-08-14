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
        if login():     
            sub_menu_cliente()
            if menu == '3':
                criar_produto()
            elif menu == '4':
                editar_produto()

    elif menu == '5':
        exluir_produto()
        
    elif menu == '6':
        editar_usuario()
        
    else:
        print('Erro!\nOpção não encontrada.')