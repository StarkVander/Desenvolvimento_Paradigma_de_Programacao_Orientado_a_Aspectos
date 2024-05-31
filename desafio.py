# Definição da classe Conta
class Conta:
    def __init__(self, tipo_conta, tipo_cliente, data_abertura, saldo):
        self.tipo_conta = tipo_conta
        self.tipo_cliente = tipo_cliente
        self.data_abertura = data_abertura
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado com sucesso.")

    def calcular_tarifa_manutencao(self):
        # Lógica para calcular a tarifa de manutenção genérica
        print("Tarifa de manutenção calculada.")


# Definição da classe ContaPoupança, que herda da classe Conta
class ContaPoupanca(Conta):
    def calcular_tarifa_manutencao(self):
        # Lógica para calcular a tarifa de manutenção específica para conta poupança
        print("Tarifa de manutenção para conta poupança calculada.")


# Definição da classe ContaInvestimento, que herda da classe Conta
class ContaInvestimento(Conta):
    def calcular_tarifa_manutencao(self):
        # Lógica para calcular a tarifa de manutenção específica para conta de investimento
        print("Tarifa de manutenção para conta de investimento calculada.")


# Exemplo de uso das classes
conta1 = Conta("Corrente", "Pessoa Física", "01/01/2022", 1000)
conta1.sacar(500)
conta1.depositar(200)
conta1.calcular_tarifa_manutencao()

conta_poupanca = ContaPoupanca("Poupança", "Pessoa Física", "01/01/2022", 5000)
conta_poupanca.calcular_tarifa_manutencao()

conta_investimento = ContaInvestimento("Investimento", "Pessoa Jurídica", "01/01/2022", 10000)
conta_investimento.calcular_tarifa_manutencao()
