import discord
import asyncio
intents = discord.Intents(members=True)
client=discord.Client(intents=intents)
welcomechannel = client.fetch_channel(869679623850590208)
@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
 # Customise the message below to what you want to send new users!
newUserMessage = "Obrigado por se inscrever no CVV-Virtual! \n"
"Para começar, vamos verificar as regras básicas: \n"
"Formate seu nome para [NOME] [NÚMERO CVV] - por exemplo - João 12345 \n"
#Adicionar um tutorial?
"Agora, selecione sua turma nesse link: https://sites.google.com/view/candidatovirtual/Escolher-Turma \n"
"E, finalmente, quando terminar, me avise respondendo com a turma que escolheu: \n"
"!turmadomingo \n"
"!turmasegunda \n"
"!turmaterça \n"
"!turmaquarta \n"
"!turmaquinta"

#CONTINUAR DAQUI - criar um role para cada comando acima


@client.event
async def on_member_join(member):
    try: 
        await client.send_message(member, newUserMessage)
    except:
        print("Couldn't message " + member.name)

# ---------------------------------
#aguardar o comando de turma para fazer a troca de papel (segunda, terca, etc...)

    role = discord.utils.get(member.server.roles, name="name-of-your-role") #  Gets the member role as a `role` object
    await client.add_roles(member, role) # Gives the role to the user
    print("Added role '" + role.name + "' to " + member.name)

@client.event
async def on_member_leave(member):
    embed=discord.Embed(
        title="😢 Até mais "+member.name+"!",    )
client.run('token') 
