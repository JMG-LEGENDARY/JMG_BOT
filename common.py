import asyncio
import sqlite3
from config import *
import discord



async def write(server_name, channel):
    db_path = SERVER_DB_PATHS[server_name]
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, content FROM messages_table")
        messages = cursor.fetchall()
        for message_id, content in messages:
            if content.strip():  # Ignore les messages vides
                if server_status[server_name] == "online":
                    try:
                        await channel.send(content)
                        print(f"Message envoyé pour {server_name} : {content}")
                        cursor.execute("DELETE FROM messages_table WHERE id = ?", (message_id,))
                        conn.commit()
                        await asyncio.sleep(0.1)
                    except discord.HTTPException as e:
                        print(f"Erreur lors de l'envoi du message sur Discord ({server_name}) : {e}")
                        break
        conn.close()
        print(f"Tous les messages pour {server_name} ont été envoyés et la base de données est à jour.")
    except sqlite3.Error as e:
        print(f"Erreur lors de la récupération ou de la suppression dans la base de données ({server_name}) : {e}")
    finally:
        conn.close()


def setup_serveur(bot):
    pass
