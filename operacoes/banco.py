class Banco:
    def __init__(self):
        self.__ctas = []

    def add(self, cta):
        self.__ctas.append(cta)

    def get(self, num):
        for conta in self.__ctas:
            if conta.get_num() == num:
                return conta
        return None