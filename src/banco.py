class Banco:

    def validar_nome(self, nome):

        return nome is not None and len(nome) >= 3

    def validar_numero_positivo(self, numero):

        return numero > 0

    def __init__(self, nome, codigo):

        self.nome = None
        self.codigo = None
        self.contas = []

        if self.validar_nome(nome):
            self.nome = nome

        if self.validar_numero_positivo(codigo):
            self.codigo = codigo

    def adicionarConta(self, conta):

        for conta_existente in self.contas:

            if conta_existente.getNumero() == conta.getNumero():
                return False

        self.contas.append(conta)

        return True

    def removerConta(self, numero):

        for conta in self.contas:

            if conta.getNumero() == numero:
                self.contas.remove(conta)
                return True

        return False

    def buscarConta(self, numero):

        for conta in self.contas:

            if conta.getNumero() == numero:
                return conta

        return None

    def quantidadeContas(self):

        return len(self.contas)

    def listarContas(self):

        return self.contas
