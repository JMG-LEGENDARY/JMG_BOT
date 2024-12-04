import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


TOKEN = 'MTI5NzUyMDU0MzQxODgxNDUwNQ.GTsqRU.NW2ZBi8dOum6Bj7JpoJq8yEFnBfM3PFPbw7JCE'  # Remplace par le token de ton bot
MC_CHANNEL_ID = 1302323091002626170  # ID du salon cible
SRV2_CHANNEL_ID = 1310153235096535151
SRV3_CHANNEL_ID = 1310153374355685427
MC_JOIN_ID = 1302325126976634990  # ID du bot MC.join
MC2_JOIN_ID = 1310163036505509888
MC3_JOIN_ID = 1310914291742015520
ROLE_ID = 1258299603342725151     # ID du rôle 'Membres IO_OI'
MANAGER_ROLE_ID = 1258298144316456990
SERVEUR_ID = 993457171759120424
SERVER_OFF_MSGS = ["le serveur minecraft est arrêté", "stopping the server"]
SERVER_ON_MSG = "le serveur minecraft a démarré"
DB_PATH_MC = r'C:\JMG_bot\db\MC.sql'
DB_DIR_MC = r'C:\JMG_bot\db'

DB_PATH_SRV2 = r'C:\JMG_bot\db\SRV2.sql'
DB_PATH_SRV3 = r'C:\JMG_bot\db\SRV3.sql'

DB_DIR_SRV2 = r'C:\JMG_bot\db'
DB_DIR_SRV3 = r'C:\JMG_bot\db'

SERVER_CHANNELS = {
    "MC": MC_CHANNEL_ID,
    "SRV2": SRV2_CHANNEL_ID,
    "SRV3": SRV3_CHANNEL_ID,
}

SERVER_IDS = {
    "MC": MC_JOIN_ID,
    "SRV2": MC2_JOIN_ID,
    "SRV3": MC3_JOIN_ID,
}

SERVER_DB_PATHS = {
    "MC": DB_PATH_MC,
    "SRV2": DB_PATH_SRV2,
    "SRV3": DB_PATH_SRV3,
}

server_status = {
    "MC": "offline",
    "SRV2": "offline",
    "SRV3": "offline",
}

mc_status = "offline"
server_2_status = "offline"
server_3_status = "offline"
previous_mc_status = "unknow"
previous_2_status = "unknow"
previous_3_status = "unknow"

player = ''

player_data = {}

COMMANDES_CREATOR = [
    "/gamemode creative {player}",  # Forcer le mode créatif
    "/effect give {player} minecraft:invisibility infinite 1",  # Invisibilité
    "/effect give {player} minecraft:resistance 9999 255",  # Résistance maximale
    "/effect give {player} minecraft:weakness infinite 255 ",    # Faiblesse maximale (pas de dégâts)
    "/team add {player} no_interaction", # Ajouter à une équipe (facultatif)
    "/team modify no_interaction collisionRule never",  # Empêcher les collisions avec d'autres joueurs
    "/tag {player} add createur"
]

ACTIONS = ["démarre", "stop"]

indent = []
serv0 = []
player = []
channel_list = []

i = -1

temps_2 = 0
temps_3 = 0
temps_mc = 0

