class ContaBancaria:
    def __init__ (self, saldo = 0):
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if valor >= self.saldo:
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor

    def exibir_saldo(self):
        print(f'{self.saldo}')

    
conta = ContaBancaria()
conta.depositar(100)
conta.sacar(50)
conta.exibir_saldo()
