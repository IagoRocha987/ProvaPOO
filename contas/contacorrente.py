from contas.contaprin import Conta

class ContaCorrente(Conta):
    def __init__(self, num, cli, lim=500.0):
        super().__init__(num, cli)
        self.__lim = lim

    def sac(self, val):
        disp = self.get_sald() + self.__lim
        if val > 0 and val <= disp:
            self.set_sald(self.get_sald() - val)
            self.get_hist().add(f"Saque Conta Corrente: R$ {val:.2f}")
            print("Saque feito")
            return True
        print("Saldo e limite insuficientes")
        return False