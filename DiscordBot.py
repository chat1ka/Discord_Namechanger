import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(''):
        aut = message.author
        await message.author.edit(nick="LabRat")

with open("token.txt", "r") as f:
    token = f.read()

client.run(token)
