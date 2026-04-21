class Historico:
    def __init__(self):
        self.__opera = []

    def add(self, msg):
        self.__opera.append(msg)

    def ver(self):
        if not self.__opera:
            print("Nenhuma operação registrada neste histórico")
        else:
            for op in self.__opera:
                print(op)