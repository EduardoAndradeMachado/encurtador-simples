import sqlite3

# Função para resetar o banco de dados
def reset_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM urls;")
        cursor.execute("DELETE FROM logs;")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='urls';")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='logs';")
        conn.commit()
        print("Banco de dados resetado com sucesso.")
    except Exception as e:
        print(f"Erro ao resetar o banco de dados: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    reset_db()