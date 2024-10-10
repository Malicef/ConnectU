import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.DB import configurarBanco
from src.model.Usuario import Usuario
from src.model.DisponibilidadeHorario import DisponibilidadeHorario
from src.control.UsuarioController import UsuarioController

# Configurando o banco de dados
configurarBanco()

horario = DisponibilidadeHorario("10:30", "13:50")

cliente = Usuario("Pedro", "Pedro@gmail.com", "9999-000", "Paulo Freire", 19, horario, "São Miguel" )

UsuarioController.cadastrarUsuario(cliente)