from clientes.cliente import Cliente
from contas.contacorrente import ContaCorrente
from contas.contapoupanca import ContaPoupanca
from operacoes.banco import Banco

def main():
    banc = Banco()
    prox = 1 

    while True:
        print("\n--- Sistema de Caixa Eletrônico ---")
        print("1 - Criar Conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar Saldo")
        print("5 - Histórico de Operações")
        print("0 - Sair")
        
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nom = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            tipo = input("Tipo de conta (1-Corrente, 2-Poupança): ")
            
            cli = Cliente(nom, cpf)
            
            if tipo == "1":
                cta = ContaCorrente(prox, cli)
                banc.add(cta)
                print(f"Conta Corrente número {prox} criada com sucesso para {nom}!")
                prox += 1
            elif tipo == "2":
                cta = ContaPoupanca(prox, cli)
                banc.add(cta)
                print(f"Conta Poupança número {prox} criada com sucesso para {nom}!")
                prox += 1
            else:
                print("Opção de conta inválida. Tente novamente.")

        elif opc == "2":
            try:
                num = int(input("Informe o número da conta: "))
                val = float(input("Qual o valor do depósito? R$ "))
                cta = banc.get(num)
                if cta:
                    cta.dep(val)
                else:
                    print("Conta não encontrada")
            except ValueError:
                print("Erro: digite apenas números válidos")

        elif opc == "3":
            try:
                num = int(input("Informe o número da conta: "))
                val = float(input("Qual o valor do saque? R$ "))
                cta = banc.get(num)
                if cta:
                    cta.sac(val)
                else:
                    print("Conta não encontrada")
            except ValueError:
                print("Erro: digite apenas números válidos")

        elif opc == "4":
            try:
                num = int(input("Informe o número da conta: "))
                cta = banc.get(num)
                if cta:
                    print(f"Saldo atual da conta {num}: R$ {cta.get_sald():.2f}")
                else:
                    print("Conta não encontrada")
            except ValueError:
                print("Erro: digite apenas números válidos")

        elif opc == "5":
            try:
                num = int(input("Informe o número da conta: "))
                cta = banc.get(num)
                if cta:
                    print(f"\n--- Histórico da Conta {num} ---")
                    cta.get_hist().ver()
                else:
                    print("Conta não encontrada")
            except ValueError:
                print("Erro: digite apenas números válidos")

        elif opc == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Escolha um número do menu")

if __name__ == "__main__":
    main()