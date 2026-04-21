# Sistema de Caixa Eletrônico em Python

Sistema que simula um caixa eletrônico (ATM) desenvolvido em Python, utilizando os conceitos de Programação Orientada a Objetos.

---

# Estrutura do Projeto

```
banco/
├── clientes/
│   ├── __init__.py
│   └── cliente.py
├── contas/
│   ├── __init__.py
│   ├── contaprin.py
│   ├── contacorrente.py
│   └── contapoupanca.py
├── operacoes/
│   ├── __init__.py
│   ├── historico.py
│   └── banco.py
├── __init__.py
└── main.py
```

---

# Funcionalidades

- Criar conta (Corrente ou Poupança)
- Depositar dinheiro
- Sacar dinheiro
- Consultar saldo
- Visualizar histórico de operações

---

# Conceitos de POO utilizados

| Conceito | Onde foi aplicado |
|---|---|
| Classes e Objetos | `Conta`, `Cliente`, `Banco`, `Historico` |
| Herança | `ContaCorrente` e `ContaPoupanca` herdam de `Conta` |
| Polimorfismo | Método `sac()` com regras diferentes em cada subclasse |
| Encapsulamento | Atributos privados com `__` e métodos getters/setters |
| Agregação | `Banco` agrega várias contas que existem de forma independente |
| Composição | `Conta` possui um `Historico` que não existe sem ela |
| Pacotes | Código organizado em `clientes/`, `contas/` e `operacoes/` |

---

# Como executar

**Pré-requisito:** Python 3.8 ou superior instalado.

1. Clone o repositório:
```bash
git clone https://github.com/IagoRocha987/ProvaPOO.git
```

2. Entre na pasta do projeto:
```bash
cd banco
```

3. Execute o sistema:
```bash
python main.py
```

---

# Menu do sistema

```
--- Sistema de Caixa Eletrônico ---
1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Consultar Saldo
5 - Histórico de Operações
0 - Sair
```

---

# Observações

- Conta Corrente possui limite adicional de R$ 500,00 para saque
- Conta Poupança permite saque apenas dentro do saldo disponível
- Todas as operações ficam registradas no histórico da conta
