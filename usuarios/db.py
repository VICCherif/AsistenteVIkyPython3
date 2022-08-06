import mysql.connector

def conectar():

    database = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database="",
        port=3306
    )

    cursor = database.cursor(buffered=True)
    return [database, cursor]