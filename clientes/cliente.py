class Cliente:
    def __init__(self, nom, cpf):
        self.__nom = nom
        self.__cpf = cpf

    def get_nom(self):
        return self.__nom

    def get_cpf(self):
        return self.__cpf