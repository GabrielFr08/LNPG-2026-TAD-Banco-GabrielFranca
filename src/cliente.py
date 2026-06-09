class Cliente:

    def validar_nome(self, nome):

        return nome is not None and len(nome) >= 5

    def limpar_numeros(self, texto):

        resultado = ""

        for caractere in texto:

            if caractere.isdigit():
                resultado += caractere

        return resultado

    def validar_cpf(self, cpf):

        cpf = self.limpar_numeros(cpf)

        return len(cpf) == 11

    def validar_telefone(self, telefone):

        telefone = self.limpar_numeros(telefone)

        return len(telefone) == 10 or len(telefone) == 11

    def validar_email(self, email):

        return email is not None and "@" in email

    def __init__(self, nome, cpf, telefone=None, email=None):

        self.nome = None
        self.cpf = None
        self.telefone = None
        self.email = None

        if self.validar_nome(nome):
            self.nome = nome

        if self.validar_cpf(cpf):
            self.cpf = self.limpar_numeros(cpf)

        if telefone is not None:

            if self.validar_telefone(telefone):
                self.telefone = self.limpar_numeros(telefone)

        if email is not None:

            if self.validar_email(email):
                self.email = email

    def getNome(self):
        return self.nome

    def getCpf(self):
        return self.cpf

    def getTelefone(self):
        return self.telefone

    def getEmail(self):
        return self.email

    def alterarTelefone(self, telefone):

        if self.validar_telefone(telefone):
            self.telefone = self.limpar_numeros(telefone)

    def alterarEmail(self, email):

        if self.validar_email(email):
            self.email = email
