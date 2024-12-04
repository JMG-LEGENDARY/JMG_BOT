import sqlite3
import os
from config import *



if not os.path.exists(DB_DIR_MC):
    os.makedirs(DB_DIR_MC)

def init_all_dbs():
    for server_name, db_path in SERVER_DB_PATHS.items():
        db_dir = os.path.dirname(db_path)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS messages_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            content TEXT 
        ) ''')
        conn.commit()
        conn.close()
        print(f"Base de données initialisée pour le serveur {server_name}.")




def show_db_content_mc():
    conn = sqlite3.connect(DB_PATH_MC)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages_table")
    messages = cursor.fetchall()
    conn.close()
    print("MC_FOREVER : Contenu de la base de données au lancement :")
    for msg in messages:
        print(f"ID: {msg[0]}, Contenu: {msg[1]}")

def show_db_content_2():
    conn = sqlite3.connect(DB_PATH_SRV3)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages_table")
    messages = cursor.fetchall()
    conn.close()
    print("SRV 2 : Contenu de la base de données au lancement :")
    for msg in messages:
        print(f"ID: {msg[0]}, Contenu: {msg[1]}")



def show_db_content_3():
    conn = sqlite3.connect(DB_PATH_SRV3)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages_table")
    messages = cursor.fetchall()
    conn.close()
    print("SRV 3 : Contenu de la base de données au lancement :")
    for msg in messages:
        print(f"ID: {msg[0]}, Contenu: {msg[1]}")




def read(message_content, author_id, server_name):
    global server_status
    if server_status[server_name] == "offline" and author_id != SERVER_IDS[server_name]:
        db_path = SERVER_DB_PATHS[server_name]
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages_table (content) VALUES (?)", (message_content,))
            conn.commit()
            conn.close()
            print(f"\nMessage stocké pour {server_name} : {message_content}\n")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'insertion dans la base de données ({server_name}) : {e}")
