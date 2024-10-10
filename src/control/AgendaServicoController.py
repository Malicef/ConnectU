from model.AgendaDeServicos import AgendaDeServicos

class AgendaServicoController:
       
    def cadastraServico(self, servico):
        self.__agenda_de_servicos.append(servico)
        self.calculaMediaAvaliacao()
        print(f"Serviço {servico.servico} cadastrado com sucesso.")

    def buscaServico(self, servico_id):
        for servico in self.__agenda_de_servicos:
            if servico.servicoId == servico_id:
                return servico
        return None

    def cancelarServico(self, servico_id):
        servico = self.buscaServico(servico_id)
        if servico:
            self.__agenda_de_servicos.remove(servico)
            self.calculaMediaAvaliacao()
            print(f"Serviço {servico.servico} cancelado com sucesso.")
        else:
            print("Serviço não encontrado.")

    def listaServicos(self):
        return self.__agenda_de_servicos

    def calculaMediaAvaliacao(self):
        if not self.__agenda_de_servicos:
            self.__media_avaliacao = 0
        else:
            soma_avaliacoes = sum(servico.avaliacao for servico in self.__agenda_de_servicos)
            self.__media_avaliacao = soma_avaliacoes / len(self.__agenda_de_servicos)

    def getMediaAvaliacao(self):
        return self.__media_avaliacao