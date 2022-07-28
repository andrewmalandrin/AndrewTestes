# -*- coding: utf-8 -*-
from view.menus.main_menu import main_menu
from view.menus.new_char import new_char
import os


CLEAR = lambda: os.system('cls')

CLEAR()
main_menu_state = input(main_menu.main_menu())
while main_menu_state not in [1,2,3]:
    CLEAR()
    main_menu_state = input(main_menu.main_menu())

if main_menu_state == 1:
    char = new_char.new_char()
    print(char.username)
    charClassnameTranslated = char.get_classname_translated(char.classname, 'pt-br')

    CLEAR()
    print ('{}, seja bem vindo ao corpo de {}s'.format(char.username, char.get_classname_translated(char.classname, 'pt-br')))

    print('Confira seus dados na ficha abaixo\n\n')

    print("Nome: {}".format(char.username).title())
    print("Level: {}".format(char.level))
    print("Idade: {}".format(char.age))
    print("Classe: {}".format(charClassnameTranslated).title())

    try:
        confirm = input("Confirmar?\n\n1-sim\n2-nao\n\n")
        CLEAR()
        while confirm not in [1,2]:
            confirm = input("Selecione uma das opcoes. Confirmar? \n\n1-sim\n2-nao\n\n")

        if confirm == 1:
            #save_char()
            print("Usuario criado com sucesso.")
        else:
            print("Cancelando a criacao do usuario")


    except Exception as error:
        print(error)

    
    


