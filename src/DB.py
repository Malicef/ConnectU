import sqlite3 

def configurarBanco():
    conexao = sqlite3.connect('Usuario.db')
    cursor = conexao.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DisponibilidadeHorario (
        disponibilidadeHorarioID INTEGER PRIMARY KEY AUTOINCREMENT,
        horarioInicio TEXT NOT NULL,
        horarioFim TEXT NOT NULL)
    ''')

    conexao.commit()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DisponibilidadeLocal (
        disponibilidadeLocalID INTEGER PRIMARY KEY AUTOINCREMENT,
        local TEXT NOT NULL)
    ''')
    
    conexao.commit()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        cep TEXT NOT NULL,
        rua TEXT NOT NULL,
        numeroDaResidencia INTEGER NOT NULL,
        disponibilidadeHorarioID INTEGER , 
        disponibilidadeLocalID INTEGER,
        FOREIGN KEY (disponibilidadeHorarioID) REFERENCES DisponibilidadeHorario(disponibilidadeHorarioID),
        FOREIGN KEY (disponibilidadeLocalID) REFERENCES DisponibilidadeLocal(disponibilidadeLocalID)) ''')
    
    conexao.commit()

    conexao.close()

