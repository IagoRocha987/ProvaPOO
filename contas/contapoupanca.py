from contas.contaprin import Conta

class ContaPoupanca(Conta):
    def sac(self, val):
        if val > 0 and val <= self.get_sald():
            self.set_sald(self.get_sald() - val)
            self.get_hist().add(f"Saque CP: R$ {val:.2f}")
            print("Saque feito")
            return True
        print("Saldo insuficiente")
        return False