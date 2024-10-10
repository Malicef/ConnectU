import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
from model.Usuario import Usuario

class UsuarioController:
    def cadastrarUsuario( usuario : Usuario ):
        conexao = sqlite3.connect('Usuario.db')
        cursor = conexao.cursor()

        cursor.execute(''' INSERT INTO Usuario 
            (nome, email, cep, rua, numeroDaResidencia, disponibilidadeHorarioID, disponibilidadeLocalID) 
            VALUES (?,?,?,?,?,?,?) ''', (usuario._nome, usuario._email, usuario._cep, usuario._rua, usuario._numeroDaResidencia, usuario._disponibilidadeHorario._horarioID, usuario._disponibilidadeLocal))
            
        conexao.commit()
        conexao.close()

        # return f"Usuário {usuario._nome} cadastrado com sucesso!"
    
    def logarUsuario(self):
        pass

    def excluirUsuario(self):
        pass

    def editarUsuario(self):
        pass