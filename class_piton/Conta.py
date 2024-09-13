class Conta:
    def __init__(self, titular, num, saldo):
        self._titular = titular
        self._numero = num
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print("Saldo nao pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if(self._saldo >= valor):
            self._saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo indisponivel")

    def depositar(self, valor):
        self._saldo += valor;
        print("Valor depostisato com exito")

    def extrato(self):
        print("O cliente", self._titular, "esta com o valor atual de: R$", self._saldo)