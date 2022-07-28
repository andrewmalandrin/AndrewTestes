# -*- coding: utf-8 -*-
from model.characters.char_data.char_data import CharData
from model.characters.classes.cop import Cop
import os

CLEAR = lambda: os.system('cls')

def new_char():

    try:
        check = False
        CLEAR()
        char_username = raw_input("Informe o nome de usuario do seu personagem\n\n")
        CLEAR()
        char_age = int(raw_input("Qual a idade do seu char?\n\n"))
        CLEAR()
        char_class_opt = input("Selecione uma das classes:\n\n1-Policial\n2-Guerreiro\n3-Elfo Noturno\n4-Elfo\n5-General\n6-Farmaceutico\n7-Politico\n8-Soldado\n9-Soldado Tecnologico\n\n")
        CLEAR()
        while not check:
            if char_class_opt not in [1,2,3,4,5,6,7,8,9,10]:
                CLEAR()
                print("Selecione uma das opcoes válidas.\n\n")
            else:
                if char_class_opt == 1:
                    char_class = 'cop'
                    check = True
                    return Cop(char_username, char_age)
                    
                if char_class_opt == 2:
                    char_class = 'knight'
                    check = True
                if char_class_opt == 3:
                    char_class = "night_elf"
                    check = True
                if char_class_opt == 4:
                    char_class = "elf"
                    check = True
                if char_class_opt == 5:
                    char_class = "general"
                    check = True
                if char_class_opt == 6:
                    char_class = "pharmaceutical"
                    check = True
                if char_class_opt == 7:
                    char_class = "politician"
                    check = True
                if char_class_opt == 8:
                    char_class = "soldier"
                    check = True
                if char_class_opt == 9:
                    char_class = "tech_soldier"
                    check = True
        
        return CharData(char_username, char_age, char_class)


    except TypeError as error:
        print("Tipo de dados incorreto: {}".format(error))
    except AttributeError as error:
        print("Tipo de dados incorreto: {}".format(error))
    except ValueError as error:
        print("Tipo de dados incorreto: {}".format(error))
    # except Exception as error:
    #     print(error)

#Criando o novo char

#char = char_data('delmiroslav', 33, 'soldier')
#charClassnameTranslated = char.get_classname_translated(char.classname, 'pt-br')





# print ('{}, seja bem vindo ao corpo de {}s'.format(char.username, char.get_classname_translated(char.classname, 'pt-br')))

# print('Confira seus dados na ficha abaixo')

# print("Nome: {}".format(char.username))
# print("Level: {}".format(char.level))
# print("Idade: {}".format(char.age))
# print("Classe: {}".format(charClassnameTranslated))

