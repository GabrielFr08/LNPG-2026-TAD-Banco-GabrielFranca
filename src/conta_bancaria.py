class ContaBancaria:

    def validar_numero_positivo(self, numero):

        return numero > 0

    def __init__(self, numero, titular, banco, saldoInicial):

        self.numero = 0
        self.titular = None
        self.banco = None
        self.saldo = 0

        if self.validar_numero_positivo(numero):
            self.numero = numero

        if titular is not None:
            self.titular = titular

        if banco is not None:
            self.banco = banco

        if saldoInicial >= 0:
            self.saldo = saldoInicial

    def depositar(self, valor):

        if self.validar_numero_positivo(valor):
            self.saldo += valor

    def sacar(self, valor):

        if not self.validar_numero_positivo(valor):
            return False

        if valor > self.saldo:
            return False

        self.saldo -= valor

        return True

    def consultarSaldo(self):

        return self.saldo

    def getNumero(self):

        return self.numero

    def getTitular(self):

        return self.titular

    def getBanco(self):

        return self.banco

    def estaAtiva(self):

        return self.saldo > 0
