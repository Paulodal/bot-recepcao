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
"Agora, selecione sua turma nesse link: \n"
"E, finalmente, quando terminar, me avise respondendo com a turma que escolheu: \n"
"!turmadomingo \n"
"!turmasegunda \n"
"!turmaterça \n"
"!turmaquarta \n"
"!turmaquinta"


@client.event
async def on_member_join(member):
    try: 
        await client.send_message(member, newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)
    embed=discord.Embed(
        title="Welcome "+member.name+"!"
        description="We're so glad you're here!"
        color=discord.Color.green()
    )
        
    role = discord.utils.get(member.server.roles, name="name-of-your-role") #  Gets the member role as a `role` object
    await client.add_roles(member, role) # Gives the role to the user
    print("Added role '" + role.name + "' to " + member.name)

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")
    embed=discord.Embed(
        title="😢 Goodbye "+member.name+"!",
        description="Until we meet again old friend." # A description isn't necessary, you can delete this line if you don't want a description.
        color=discord.Color.red() # There are lots of colors, you can check them here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
    )
client.run('token') 
