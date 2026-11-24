import sqlite3


def fazer_login(usuario, senha):
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    cursor.execute  (
    "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (usuario, senha),
    )
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."