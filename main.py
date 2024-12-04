# main.py
import re
import discord
import json
import time
import os
import subprocess
    
# Import des modules spécifiques
from discord.ext import commands, tasks
from asyncio import Lock
from config import *
from sql import *
from events import *
from salut import *
from common import *
from serveur import *
from messages import *


# Dictionnaire pour stocker les chronos en cours pour chaque serveur
chronos = {}

update_lock = Lock()


# Initialisation du bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)


# Initialisation des bases de données
init_all_dbs()
show_db_content_mc()
show_db_content_2()
show_db_content_3()



#débogage :
async def writeee() :
    await write("MC", MC_CHANNEL_ID)
    await write("SRV2", SRV2_CHANNEL_ID)
    await write("SRV3", SRV3_CHANNEL_ID)



# Configuration des événements et commandes

setup_serveur(bot)


@tasks.loop()
async def update_servs() :
    try:
        await all_serveurs_statut(bot)
    except Exception as e:
        print(f"Erreur lors de la mise à jour des statuts : {e}")


roles_dict = {}

def create_db_if_not_exists():
    if not os.path.exists('roles_membres.json'):
        with open('roles_membres.json', 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        print("Le fichier 'roles_membres.json' a été créé.")


# Fonction pour enregistrer les rôles dans un fichier JSON
def save_roles():
    with open('roles_membres.json', 'w', encoding='utf-8') as f:
        json.dump(roles_dict, f, ensure_ascii=False, indent=4)
    print("Les rôles ont été enregistrés dans le fichier 'roles_membres.json'.")

# Vérifier si un membre a changé de rôle
@bot.event
async def on_member_update(before, after):
    # Vérifier si les rôles du membre ont changé
    if before.roles != after.roles:
        # Mise à jour du dictionnaire des rôles avec le pseudo (display_name)
        roles_dict[after.display_name] = [role.name for role in after.roles if role.name != "@everyone"]
        
        # Sauvegarder la mise à jour dans le fichier JSON
        save_roles()

def load_roles():
    create_db_if_not_exists()  # Vérifie si la base de données existe, sinon la crée
    try:
        with open('roles_membres.json', 'r', encoding='utf-8') as f:
            roles_dict = json.load(f)
        print("Les rôles ont été chargés depuis le fichier 'roles_membres.json'.")
        return roles_dict
    except FileNotFoundError:
        print("Le fichier 'roles_membres.json' n'a pas été trouvé.")
        return {}  # Retourne un dictionnaire vide si le fichier n'existe pas
    except json.JSONDecodeError:
        print("Erreur lors de la lecture du fichier JSON.")
        return {}

# Exemple d'utilisation
roles_dict = load_roles()
print(roles_dict)

async def has_required_role(member: discord.Member, joueur, roles_to_check):
    if roles_to_check in roles_dict.get(joueur, None):
        return True
    return False


@bot.event
async def on_ready():   
    print(f'Bot connecté en tant que {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)} commandes.")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")
    print(f"Le bot est prêt à recevoir des commandes slash.")

    guild = bot.get_guild(SERVEUR_ID)  
    if guild:
        # Parcourir tous les membres du serveur et enregistrer leur pseudo (display_name)
        for member in guild.members:
            roles_dict[member.display_name] = [role.name for role in member.roles if role.name != "@everyone"]
        save_roles()
    else:
        print("Serveur discord non trouvé")
    update_servs.start()





@bot.event
async def on_message(message):
    print(f"Message reçu : {message}")
    print()
    print()
    print(f"Contenu du message : {message.content}")
    
    if message.content.startswith("/") or message.content.startswith(bot.command_prefix):
        print("\nC'est une commande\n")
        if message.channel.id == MC_CHANNEL_ID or message.author.id == MC_JOIN_ID or message.author.id == 1297520543418814505:
            ide = "MC"
            try :
                read(message.content, message.author.id, ide)
            except Exception as e:
                print(f"Message pas dans BDD, à cause de {e}")
            return
        elif "Manager Minecraft"    or "Manager (Discord et Minecraft)" in roles_dict.get(joueur, None): 
            print("\nL'utilisateur est Manager\n")
            # Si l'utilisateur est un "Manager Minecraft" ou "Manager Discord et Minecraft"
            channel = bot.get_channel(MC_CHANNEL_ID)
            await channel.send(message.content)
        
        # Commande spéciale /gamemode pour "Créateurs"
        elif message.content.startswith('/gamemode') and await has_required_role(message.author, joueur, ["Créateurs"]):
            print("\nL'utilisateur est Manager\n")
            # Si l'utilisateur est un "Créateur", envoyer dans le salon de gestion Minecraft
            channel = bot.get_channel(MC_CHANNEL_ID)
            await channel.send(f"Commande /gamemode reçue de {message.author.name}: {message.content}")
        await bot.process_commands(message)
        return

    
    global server_status
    if message.channel.id == MC_CHANNEL_ID:
        print("\n\nLe message est reçu dans le salon MC FOREVER\n\n")
        ide = "MC"
        read(message.content, message.author.id, ide)
        if message.author.id == MC_JOIN_ID:
            join_match = re.search(r"\[MinecraftServer\]: (\w+) joined the game", message.content)
            print(join_match)
            leave_match = re.search(r"\[MinecraftServer\]: (\w+) left the game", message.content)
            print(leave_match)
        
            if join_match:
                joueur = join_match.group(1)
                bienvenu = message_bienvenue(joueur)
                await message.channel.send(bienvenu)
                print(f"\n\n\n{joueur} a rejoint le serveur.\n")
                print(f"Rôles de {joueur} : {roles_dict.get(joueur)}")
                if joueur in roles_dict :
                    print("Joueur dans la BDD")
                    if "Créateurs" in roles_dict.get(joueur, None):
                        print(f"\n👷 {joueur} a rejoint le jeu et est un Créateur.")
                            
                            # Envoyer les commandes Minecraft pour limiter les actions
                        for commande in COMMANDES_CREATOR:
                                    commande_formatee = commande.format(player=joueur)
                                    await message.channel.send(commande_formatee)
                                    print(f"Commande envoyée : {commande_formatee}")
                    else:
                            print(f"\n⚔️ {joueur} est un joueur normal.")
                        # Envoyer la commande Minecraft pour donner un effet de résistance
                            commande_minecraft = f"/effect give {joueur} minecraft:resistance 120 255 true"
                            await message.channel.send(commande_minecraft)
                            print(f"🛡️ Commande envoyée : {commande_minecraft}")
                else :
                    print("Le joueur n'est pas dans la BDD")
        if leave_match:
            joueur = leave_match.group(1)
            msg = message_au_revoir(joueur)
            await message.channel.send(msg)
            print(f"{joueur} a quitté le serveur.")
                

    if message.channel.id == SRV2_CHANNEL_ID:
        ide = "SRV2"
        read(message.content, message.author.id, ide)
    if message.channel.id == SRV3_CHANNEL_ID:
        ide = "SRV3"
        read(message.content, message.author.id, ide)

    if "ticket-" in message.channel.name and not message.author.bot:
        member = message.author

        if message.content.lower() != "fermer le ticket":
            pseudo_minecraft = message.content
            await message.channel.send(f"Pseudo **{pseudo_minecraft}** enregistré avec succès. Vous pouvez maintenant fermer le ticket.")
            await member.edit(nick=pseudo_minecraft)

            role = message.guild.get_role(ROLE_ID)
            if role and member:
                await member.add_roles(role)
            else:
                print("Rôle ou membre introuvable.")


            whitelist_command = f"/whitelist add {pseudo_minecraft}"
            minecraft_channel = discord.utils.get(message.guild.channels, name="💾-gestion-minecraft")
            if minecraft_channel:
                await minecraft_channel.send(whitelist_command)

            await message.channel.send("Votre pseudo a été mis à jour, et vous avez été ajouté à la liste blanche du serveur Minecraft. Vous pouvez maintenant rejoindre le serveur. Nous vous invitons à continuer l'installation en vous rendant dans la catégorie [🔧]-Installation, si ce n'est pas déjà fait.")

    
@bot.event
async def send_mess(serv1):
    global index, temps_2, temps_3, temps_mc
    print(player,"\n",serv0,"\n",channel_list,"\n",indent)
    try :
        print("Contenu de serv0 :", serv0)  # Debug
        print("Recherche de :", str(serv1))
        index = serv0.index(str(serv1))
    except ValueError as e :
        print(f"Erreur avec l'index : {e}")
        if serv0 == []:
            return
    async def send2(bot, channel0):
        channel1 = bot.get_channel(int(channel0))
        if channel1 is None:
            print(f"Le salon avec l'ID {channel0} est introuvable.")
            return
        if serv0[index]== "0":
            serv2 = "Serveur 2"
            temps = temps_2 if temps_2 != 0 else "inconnu"
        if serv0[index]== "1":
            serv2 = "MC_FOREVER"
            temps = temps_mc if temps_mc != 0 else "inconnu"
        if serv0[index]== "2":
            serv2 = "Serveur 3"
            temps = temps_3 if temps_3 != 0 else "inconnu"
        else :
            print("Aucun message n'a été envoyé")
        temps = round(temps, 1)
        await channel1.send(f"{player[index]} ! Le serveur {serv2} est en ligne (en {temps} secondes) !")
        print(f"Message envoyé : {player[index]} ! Le serveur {serv2} est en ligne !")
        del player[index]
        del serv0[index]
        del channel_list[index]
        return
    await send2(bot, channel_list[index])

setup_events(bot)


    

@bot.tree.command(name="salut", description="Permet de vérifier l'état du bot")
async def salut(interaction: discord.Interaction):
    """Commande pour saluer le bot avec un ping au joueur."""
    mention_joueur = interaction.user.mention  # Récupère le format pour pinguer l'utilisateur (@Nom)
    await interaction.response.send_message(f"Salut, {mention_joueur} !\n Aternos : {aternos_client}")
    print(f"Commande /salut reçue de {interaction.user.name}. Réponse envoyée.")




@bot.tree.command(name="stop_all", description="stop tous les serveurs")
async def stop_all(interaction: discord.Interaction):
    for i in range(3):
        servs[i].stop()
    await interaction.response.send_message("Tous les serveurs sont arrétés")





@bot.tree.command(name="serveur", description="Démarre ou arrête un serveur Minecraft Aternos.")
@app_commands.describe(action="Action à effectuer (démarrer ou arrêter)", nom_serveur="Nom du serveur")
@app_commands.choices(
    action=[
        app_commands.Choice(name="Démarre", value="démarre"),
        app_commands.Choice(name="Stop", value="stop")
    ],
    nom_serveur=[
        app_commands.Choice(name="MC_FOREVER", value="1"),
        app_commands.Choice(name="Serveur 2", value="0"),
        app_commands.Choice(name="Serveur 3", value="2")
    ]
)

async def serveur(interaction: discord.Interaction, action: app_commands.Choice[str], nom_serveur: app_commands.Choice[str]):
    async with update_lock:
        global server_channel_id
        server_channel_id = interaction.channel_id  # Sauvegarde l'ID du salon d'origine
        print(f"Commande reçue : {action.value} sur {nom_serveur.name} de {interaction.user.name} dans {interaction.channel.name}.")

        # Sélection du serveur à partir de l'index fourni
        try:
            myserv = servs[int(nom_serveur.value)]
            print(f"Serveur sélectionné : {myserv}")
        except (ValueError, IndexError):
            await interaction.response.send_message("Serveur introuvable. Veuillez réessayer avec un choix valide.")
            return

        global player, serv0, indent, channel_list, i
        
        
        
        

        try:
            if action.value == "démarre":
                print("Tentative de démarrage du serveur...")
                try:
                    myserv.start()
                except Exception as e:
                    print(f"Erreur lors du démarrage : {e}")
                    await interaction.response.send_message(
                        f"Erreur : {e} sur : {nom_serveur.name}, impossible de démarrer le serveur"
                    )
                chronos[nom_serveur.name] = time.perf_counter()
                print(chronos)
                await interaction.response.send_message(f"Le serveur {nom_serveur.name} est en train de démarrer !")
                print(f"{nom_serveur.name} en démarrage.")
                player.append(interaction.user.mention)
                serv0.append(nom_serveur.value)
                channel_list.append(interaction.channel.id)
                i += 1
                indent.append(i)
                
                
                        
            elif action.value == "stop" :
                if any(role.id == MANAGER_ROLE_ID for role in interaction.user.roles):
                    print(f"Serveur demandé en arret : {myserv}")        
                    try:
                        myserv.stop()
                        await interaction.response.send_message(f"Le serveur {nom_serveur.name} est en train de s'arrêter !")
                        print(f"{nom_serveur.name} en arrêt.")
                    except Exception as e:
                        print(f"Erreur lors de l'arrêt : {e}")
                        await interaction.response.send_message(
                            f"Erreur : {e} sur : {nom_serveur.name}", ephemeral=True
                        )
                else:
                    await interaction.response.send_message(
                        "Vous n'avez pas la permission d'arrêter le serveur.",
                        ephemeral=True
                    )
                    print(f"Permission refusée pour arrêter le serveur {nom_serveur.name}.")
            else:
                print("Commande invalide reçue.")
                await interaction.response.send_message('Commande invalide. Utilisez "démarre" ou "stop".')

        except Exception as e:
            print(f"Erreur lors de l'exécution de la commande : {e}")
            await interaction.response.send_message(f"Erreur : {e}")


COMMANDES = {
    "/serveur": "Démarre le serveur Minecraft.",
    "/arreter": "Arrête le serveur Minecraft. (Réservé au rôle Manager Minecraft)",
    "/status": "Affiche le statut actuel du serveur Minecraft.",
    "/tp <pseudo>": "Téléporte un joueur à vos coordonnées.",
    "/give <objet> <quantité>": "Donne un objet à un joueur.",
    "/aide": "Affiche la liste des commandes disponibles."
}

# Commande /aide
@bot.tree.command(name="aide", description="Affiche la liste des commandes disponibles.")
async def aide(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Liste des commandes disponibles",
        description="Voici la liste des commandes et leur utilisation :",
        color=discord.Color.blue()
    )
    
    for commande, description in COMMANDES.items():
        embed.add_field(name=commande, value=description, inline=False)

    await interaction.response.send_message(embed=embed)




async def update_server_mc(bot):
    global mc_status, previous_mc_status, temps_mc
    channel = bot.get_channel(MC_CHANNEL_ID)
    if channel:
        async for message in channel.history(limit=8192):
            if message.author.id == MC_JOIN_ID:
                if any(off_msg.lower() in message.content.lower() for off_msg in SERVER_OFF_MSGS):
                    previous_mc_status = mc_status
                    mc_status = "offline"
                    server_status["MC"] = "offline"
                    return
                elif SERVER_ON_MSG.lower() in message.content.lower():
                    if "MC_FOREVER" in chronos:
                        temps_mc = time.perf_counter() - chronos["MC_FOREVER"]
                    if previous_mc_status == "offline" :
                        await send_mess(1)
                    mc_status = "online"
                    previous_mc_status = mc_status
                    server_status["MC"] = "online"
                    del chronos["MC_FOREVER"]
                    return
    #print(f"État actuel du serveur MC_FOREVER : {mc_status}")


async def update_server_2(bot):
    global server_2_status, previous_2_status, temps_2
    channel = bot.get_channel(SRV2_CHANNEL_ID)
    if channel:
        async for message in channel.history(limit=8192):
            if message.author.id == MC2_JOIN_ID:
                if any(off_msg.lower() in message.content.lower() for off_msg in SERVER_OFF_MSGS):
                    previous_2_status = server_2_status
                    server_2_status = "offline"
                    server_status["SRV2"] = "offline"
                    return
                elif SERVER_ON_MSG.lower() in message.content.lower():
                    if "Serveur 2" in chronos:
                        temps_2 = time.perf_counter() - chronos["Serveur 2"]
                    if previous_2_status == "offline":
                        await send_mess(0)
                    server_2_status = "online"
                    previous_2_status = server_2_status
                    server_status["SRV2"] = "online"
                    del chronos["Serveur 2"]
                    return
    #print(f"État actuel du serveur 2 : {server_2_status}")
    

async def update_server_3(bot):
    global server_3_status, previous_3_status, temps_3
    channel = bot.get_channel(SRV3_CHANNEL_ID)
    if channel:
        async for message in channel.history(limit=8192):
            if message.author.id == MC3_JOIN_ID:
                if any(off_msg.lower() in message.content.lower() for off_msg in SERVER_OFF_MSGS):
                    previous_3_status = server_3_status
                    server_3_status = "offline"
                    server_status["SRV3"] = "offline"
                    return
                if SERVER_ON_MSG.lower() in message.content.lower():
                    if "Serveur 3" in chronos:
                        temps_3 = time.perf_counter() - chronos["Serveur 3"]
                    if previous_3_status == "offline":
                        await send_mess(2)
                    server_3_status = "online"
                    previous_3_status = server_3_status
                    server_status["SRV3"] = "online"
                    if chronos ["Serveur 3"] :
                        del chronos["Serveur 3"]
                    return
    #print(f"État actuel du serveur 3 : {server_3_status}")
    

async def all_serveurs_statut(bot):
    try :
        await update_server_mc(bot)
    except Exception as e:
        error = 1
    print(f"Etat actuel de MC_FOREVER : {mc_status}")
    if mc_status == "online":
        channel = bot.get_channel(MC_CHANNEL_ID)
        if channel:
            await write("MC", channel)
    try:
        await update_server_2(bot)
    except Exception as e:
        error = 1
    print(f"Etat actuel de SRV 2 : {server_2_status}")
    if server_2_status == "online":
        channel = bot.get_channel(SRV2_CHANNEL_ID)
        if channel:
            await write("SRV2", channel)
    try :
        await update_server_3(bot)
    except Exception as e:
        error = 1
    print(f"Etat actuel de SRV 3  : {server_3_status}")
    if server_3_status == "online":
        channel = bot.get_channel(SRV3_CHANNEL_ID)
        if channel:
            await write("SRV3", channel)
















async def bot_run():
    while True:
        try:
            # Tentative de connexion à Discord
            await bot.start(TOKEN)
            break  # Si la connexion réussit, on sort de la boucle
        except Exception as e:
            print("Connexion à Discord impossible")
            print(f"Erreur : {e}")
            print("Réessai dans 2 secondes...")
            await asyncio.sleep(2)  # Attendre 2 secondes avant de réessayer

# Lancer la fonction avec asyncio
asyncio.run(bot_run())