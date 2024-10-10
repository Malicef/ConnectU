# from AgendaDeServicos import AgendaDeServicos
from src.model.DisponibilidadeHorario import DisponibilidadeHorario

class Usuario: 
    def __init__(self, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal ):
        
        self._userID = None
        self._servicos = "AgendaDeServicos()"
        self._nome = nome
        self._email = email
        self._cep = cep 
        self._rua = rua
        self._numeroDaResidencia = numeroDaResidencia
        self._disponibilidadeHorario : DisponibilidadeHorario = disponibilidadeHorario
        self._disponibilidadeLocal = disponibilidadeLocal

    