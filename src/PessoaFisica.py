from Usuario import Usuario

class PessoaFisica(Usuario):
    def __init__(self, userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal):
        super().__init__(userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal)
        self.cpf = cpf
        self.avaliacaoMedia = avaliacaoMedia

    def verificaAntecedentesCriminais(self):
        pass
    def verificaCPF(self):
        pass
    def calculaMediaAvaliacao(self):
        pass