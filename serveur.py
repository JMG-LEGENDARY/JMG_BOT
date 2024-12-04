import discord
from config import bot, MANAGER_ROLE_ID, player_data, ACTIONS
from discord import app_commands
try :
    from aternos import servs
except Exception as e :
    print("Impossible d'établir une connexion aux serveurs aternos")
    print(f"Erreur : {e}")




async def last_player(interaction: discord.Interaction):
    """Commande pour récupérer le dernier joueur ayant exécuté une commande dans ce salon."""
    global channel_id
    channel_id = interaction.channel_id
    if interaction.channel_id in player_data:
        await interaction.response.send_message(
            f"Le dernier joueur ayant exécuté une commande dans ce salon est {player_data[interaction.channel_id]}."
        )
    else:
        await interaction.response.send_message(
            "Aucun joueur n'a encore exécuté de commande dans ce salon."
        )


class CommandAutoComplete(app_commands.Choice[str]):
    """Classe pour définir les choix d'autocomplétion."""
    pass


async def autocomplete_action(interaction: discord.Interaction, current: str):
    """Fournit des suggestions d'autocomplétion basées sur l'entrée actuelle."""
    return [
        app_commands.Choice(name=action, value=action)
        for action in ACTIONS
        if current.lower() in action.lower()
    ]

