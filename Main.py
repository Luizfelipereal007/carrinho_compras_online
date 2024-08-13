from Views import*
from Classes import* 
while True:
       menu_principal()
       op=int(input("Opções")) 
       if 1==op:
           realizar_cadastro
       if 2==op:
           realizar_login
       if 3==op:
           listar_produtos
       if 4==op:
           sair