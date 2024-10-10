from PessoaFisica import PessoaFisica

class Assessorado(PessoaFisica):
    def __init__(self, userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal, demandas):
        super().__init__(userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal)
        self.demandas = []