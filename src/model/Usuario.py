# from AgendaDeServicos import AgendaDeServicos
from DisponibilidadeHorario import DisponibilidadeHorario

class Usuario: 
    def __init__(self, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal ):
        
        self.__userID = None
        self.__servicos = "AgendaDeServicos()"
        self.__nome = nome
        self.__email = email
        self.__cep = cep 
        self.__rua = rua
        self.__numeroDaResidencia = numeroDaResidencia
        self.__disponibilidadeHorario : DisponibilidadeHorario = disponibilidadeHorario
        self.__disponibilidadeLocal = disponibilidadeLocal
