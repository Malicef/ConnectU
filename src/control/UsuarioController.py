import sqlite3
from model.Usuario import Usuario

class UsuarioController:
    def cadastrarUsuario( usuario : Usuario ):
        conexao = sqlite3.connect('Usuario.db')
        cursor = conexao.cursor()

        cursor.execute(''' INSERT INTO Usuario 
            (nome, email, cep, rua, numeroDaResidencia, disponibilidadeHorarioID, disponibilidadeLocalID) 
            VALUES (?,?,?,?,?,?,?) ''', (usuario.nome, usuario.email, usuario.cep, usuario.rua, usuario.numeroDaResidencia, usuario.disponibilidadeHorario.horarioID, usuario.disponibilidadeLocal))
            
        conexao.commit()
        conexao.close()

        return f"Usuário {usuario.nome} cadastrado com sucesso!"
    
    def logarUsuario(self):
        pass

    def excluirUsuario(self):
        pass

    def editarUsuario(self):
        pass