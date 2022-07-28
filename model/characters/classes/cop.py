# -*- coding: utf-8 -*-
from model.characters.char_data.char_data import CharData

class Cop(CharData):
    def __init__(self, classname):
        super(Cop, self).__init__()
        self.classname = classname

    def get_classname(self):
        return self.classname

    def get_classname_translated(self, lang):
        if lang.upper() == 'PT-BR':
            return ('policia')
        else:
            raise Exception("Por favor informar uma linguagem valida dentre as opções(pt-br...)")
