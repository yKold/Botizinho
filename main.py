import os
import discord
import random 
import armas
from dotenv import load_dotenv


# Variável para armazenar o estado da conversa
conversations = {}

vida_player = 100
vida_monstro = 50
arma_player = "Nenhuma"



comandos = ['A atual lista de comando são:','!start - Inicia um teste do RPG']

async def detalhes(arma, message):
    await message.channel.send(f"-----Detalhes da sua arma-----   \nNome: {arma['Nome']}, \nRaridade: {arma['Raridade']}, \nTipo: {arma['Tipo']}")

async def Start(message):
    await message.channel.send('Você deseja LUTAR? \n 1 - SIM \n 2 - NÃO')
    conversations[message.author.id] = 'start'

async def handle_response(message):
    user_id = message.author.id
    if user_id in conversations:
        # Verifica em qual parte da conversa o usuário está
        if conversations[user_id] == 'start':
            if message.content == '1':
                await message.channel.send('Ótimo! Vamos lutar então!')
                await message.channel.send(f'\n Player Life: {vida_player}')
                await message.channel.send('Qual arma você prefere usar? \n 1 - Machado \n 2 - Espada \n 3 - Arco')

                conversations[user_id] = 'choose_weapon'  # Define novo estado da conversa
            elif message.content == '2':
                await message.channel.send('Tudo bem, até mais!')
                del conversations[user_id]  # Limpa o estado da conversa
            else:
                await message.channel.send('Por favor, responda com 1 ou 2.')

        elif conversations[user_id] == 'choose_weapon':
            if message.content == "1":
                arma_player = armas.machado
            elif message.content == "2":
                arma_player = armas.espada
            elif message.content == "3":
                arma_player = "arco"
            else:
                await message.channel.send("Selecione um dos valores válidos!")
            await detalhes(arma_player, message)

            conversations[user_id] = 'weapon_detais'
        
        elif conversations[user_id] == 'weapon_detais':
            await detalhes(arma_player, message)
# CONTINUAR DAQUI 
#
#
###
#
###
                

            


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    

@client.event
async def on_message(message):

    if message.content == "!help":
        for i in comandos:
            await message.channel.send(i)

    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

    if message.content == "!start":
        await Start(message)

    # Verifica se há um estado de conversa ativo para o usuário
    if message.author.id in conversations:
        
        await handle_response(message)

client.run(TOKEN)
