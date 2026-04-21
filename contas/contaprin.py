from operacoes.historico import Historico

class Conta:
    def __init__(self, num, cli):
        self.__num = num
        self.__cli = cli
        self.__sald = 0.0
        self.__hist = Historico()

    def get_num(self):
        return self.__num

    def get_cli(self):
        return self.__cli

    def get_sald(self):
        return self.__sald

    def set_sald(self, val):
        self.__sald = val

    def get_hist(self):
        return self.__hist

    def dep(self, val):
        if val > 0:
            self.__sald += val
            self.__hist.add(f"Deposito: R$ {val:.2f}")
            print("Deposito feito")
            return True
        print("Valor invalido")
        return False

    def sac(self, val):
        pass