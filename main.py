import os
import discord
from discord.ext import commands
import random 
import armas.todas_espadas as espadas
import armas.todos_arcos as arcos
import armas.todos_machados as machados
import monstro as mstr
from dotenv import load_dotenv


# Variável para armazenar o estado da conversa
conversations = {}

vida_player = 100
arma_player = "Nenhuma"
vida_base = 50



comandos = ['A atual lista de comando são:','!start - Inicia um teste do RPG']


async def detalhes(arma, message):
    await message.channel.send(f"-----Detalhes da sua arma-----   \nNome: {arma['Nome']}, \nRaridade: {arma['Raridade']}, \nTipo: {arma['Tipo']} \n----------------")

async def Start(message):
    await message.channel.send('Você deseja LUTAR? \n 1 - SIM \n 2 - NÃO \n----------------')
    conversations[message.author.id] = 'start'

async def handle_response(message):
    global arma_player, vida_base, monstro
    user_id = message.author.id
    conteudo = message.content
    async def env_msg(mensagem):
        await message.channel.send(mensagem)
    monstro = mstr.CriarMonstroAleatorio(3)
    

    if user_id in conversations:

        # Verifica em qual parte da conversa o usuário está
        if conversations[user_id] == 'start':
            if conteudo == '1':
                await env_msg('Ótimo! Vamos lutar então!')
                await env_msg(f'\n Player Life: {vida_player}')
                await env_msg("----------------")
                await env_msg('Qual arma você prefere usar? \n 1 - Machado \n 2 - Espada \n 3 - Arco')

                conversations[user_id] = 'choose_weapon'  # Define novo estado da conversa
            elif conteudo == '2':
                await env_msg('Tudo bem, até mais!')
                del conversations[user_id]  # Limpa o estado da conversa
            else:
                await env_msg('Por favor, responda com 1 ou 2.')
            

        elif conversations[user_id] == 'choose_weapon':
            if conteudo == "1":
                arma_player = machados.machado001
            elif conteudo == "2":
                arma_player = espadas.espada001
            elif conteudo == "3":
                arma_player = arcos.arco001
            else:
                await env_msg("Selecione um dos valores válidos!")
            await detalhes(arma_player, message)

            conversations[user_id] = 'weapon_detais'

            await env_msg("Deseja continuar? \n1 - Sim \n2 - Não")
        
        elif conversations[user_id] == 'weapon_detais':
            if conteudo == "1":
                await env_msg(f"A vida atual do player é {vida_player}.")

                await env_msg("----------------")
                await env_msg(f"O monstro está com {monstro['vida']} de vida!")
                await env_msg(f"Sua raça é {monstro['nome']}")
                await env_msg(f"Suas habilidades são:")
                for i in monstro['habilidades']:
                    await env_msg(f"-{i}")
                await env_msg("----------------")

                await env_msg("Você deseja atacar? \n1 - Sim \n2 - Não")
                conversations[user_id] = "pergunta01"
            else:
                await env_msg("Voltando ao inicio!")
                del conversations[user_id]

        elif conversations[user_id] == "pergunta01":
            if conteudo == "2":
                await env_msg("Ok! Voltando ao início.")
                del conversations[user_id]
            elif conteudo == "1":
                await env_msg("Qual habilidade deseja usar?\n")
                for i in arma_player["Habilidades"]:
                    await env_msg(f"-{i}")
                conversations[user_id] = "pergunta02"
        
        elif conversations[user_id] == "pergunta02":
            for i in arma_player["Habilidades"]:
                if message.content == i:
                    monstro['vida'] -= arma_player["Habilidades"][i]['Dano']
                    dano_levado = arma_player["Habilidades"][i]['Dano']
                    await env_msg(f"O monstro recebeu {dano_levado} de DANO!")
                    if monstro['vida'] > 0:
                        await env_msg(f"A atual vida do monstro é {monstro['vida']:.2f}.")
                        await env_msg("Use uma habilidade novamente!")
                        conversations[user_id] = "pergunta02"
                    else:
                        monstro["vida"] = 0
                        await env_msg(f"A atual vida do monstro é {monstro['vida']:.2f}.")
                        await env_msg("Você eliminou o monstro")
                        vida_base *= 1.3
                        monstro["vida"] += vida_base
                        del conversations[user_id]
                    continue

            

                

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

bot = commands.Bot(command_prefix="%", intents=intents)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    

@bot.event
async def on_message(message):

    if message.content == "!help":
        for i in comandos:
            await message.channel.send(i)

    if message.content == "!start":
        await Start(message)

    # Verifica se há um estado de conversa ativo para o usuário
    if message.author.id in conversations:
        
        await handle_response(message)

@bot.command(name="99")
async def nov_nov(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name="happy birthday")
async def niver(ctx):
    response = 'Happy Birthday! 🎈🎉'
    await ctx.send(response)

bot.run(TOKEN)
