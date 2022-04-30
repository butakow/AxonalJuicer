"""AxonalJuicer script"""

import os
import sys
import config

sys.path.append(os.getcwd() + r'/discord.py')

import discord
from discord.ext import commands

GUILD = discord.Object(config.server_id)

AxonalJuicer = commands.Bot(command_prefix="%", intents=discord.Intents.none())

@AxonalJuicer.tree.command(guild=GUILD)
async def ping(interaction):
    """Pings AxonalJuicer"""
    await interaction.response.send_message("Pong!", ephemeral=True)

@AxonalJuicer.event
async def on_ready():
    """Syncs AxonalJuicer's command tree with its guild"""
    await AxonalJuicer.tree.sync(guild=GUILD)

AxonalJuicer.run(config.token)

print()
