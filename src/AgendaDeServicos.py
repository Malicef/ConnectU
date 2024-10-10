class AgendaDeServicos:
    def __init__(self):
        self.__agendaDeServicos = []
        self.__mediaAvaliacao = 0

    def cadastraServico(self, servico):
        self.__agendaDeServicos.append(servico)
        self.calculaMediaAvaliacao()
        print(f"Serviço {servico.servico} cadastrado com sucesso.")

    def buscaServico(self, servico_id):
        for servico in self.__agendaDeServicos:
            if servico.servicoId == servico_id:
                return servico
        return

    def cancelarServico(self, servico_id):
        servico = self.buscaServico(servico_id)
        if servico:
            self.__agendaDeServicos.remove(servico)
            self.calculaMediaAvaliacao()
            print(f"Serviço {servico.servico} cancelado com sucesso.")
        else:
            print("Serviço não encontrado.")

    def listaServicos(self):
        return self.__agendaDeServicos

    def calculaMediaAvaliacao(self):
        if not self.__agendaDeServicos:
            self.__mediaAvaliacao = 0
        else:
            soma_avaliacoes = sum(servico.avaliacao for servico in self.__agendaDeServicos)
            self.__mediaAvaliacao = soma_avaliacoes / len(self.__agendaDeServicos)

    def getMediaAvaliacao(self):
        return self.__mediaAvaliacao