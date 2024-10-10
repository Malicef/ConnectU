from PessoaFisica import PessoaFisica

class Voluntario(PessoaFisica):
    def __init__(self, userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal, servicos_prestados):
        super().__init__(userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal)
        self.profissao = profissao
        self.servicosPrestados = []