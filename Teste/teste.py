# -*- coding: utf-8 -*-


class Pessoa(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Estudante(Pessoa):
    def __init__(self, name, serie):
        super(Estudante, self).__init__(name)
        self.serie = serie

    def get_serie(self):
        return self.serie




pessoa = Estudante('Pedro', 8)

print(pessoa.get_name())
print(pessoa.get_serie())
