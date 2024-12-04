import asyncio
from config import *
import discord
from aternos import *

@bot.event
async def on_guild_channel_create(channel):
    if "ticket-" in channel.name:
        await asyncio.sleep(0.2)
        await channel.send("Bienvenue dans ce ticket ! Pour rejoindre notre serveur Minecraft, veuillez répondre avec votre **pseudo Minecraft** uniquement (Pas d'espace, pas d'emojis ou caractères spéciaux).")




def setup_events(bot):
    bot.event(on_guild_channel_create)