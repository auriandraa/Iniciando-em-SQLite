import sqlite3

conexao = sqlite3.connect('usuarios.db')

cursor = conexao.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               idade INT NOT NULL);''')


cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES ('João', 20);''')

conexao.commit()
conexao.close()

print('Script finalizado com sucesso!')