from model.Usuario import Usuario

class PessoaJuriduca(Usuario):
    def __init__(self, userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal, cnpj, demandas):
        super().__init__(userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal)
        self.cnpj = cnpj
        self.demandas = demandas

    def verificaAntecedentes(self):
        pass
    def verificaCNPJ(self):
        pass
    def addDemanda(self):
        pass
    def deletaDemanda(self):
        pass
