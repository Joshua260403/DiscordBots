import discord
import asyncio
import random
import json
import os

client = discord.Client()

@client.event
async def on_ready():
    print('User:')
    print(client.user.name)
    print(client.user.id)
    print("-----------")

@client.event
async def on_message(message):
    role_names = [role.name for role in message.author.roles]
    #print(message.author)
    #print(message.author.roles)
    #print(role_names)
    if 'Admin' in role_names:
        if message.content.startswith('$say'):
             await client.send_message(message.channel, message.content[5:])
        if message.content.startswith('$kick'):
            try:
                kickuser = message.mentions[0]
                role_names_ = [role.name for role in kickuser.roles]
                if not 'Admin' in role_names_:
                    await client.kick(kickuser)
                    print(kickuser + " got kicked")
            except Exception:
                pass

client.run('Mzc5NjUzNDY1Nzg3MzM0NjU3.DOtP_g.MHYr_AXhuuZaQwckxhMowXprd-I')
# You can try that token but that is the old one.
