import discord, re
        
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if re.search("yuh", message.content.lower()):
        await client.add_reaction(message, "🇾")
        await client.add_reaction(message, "🇺")
        await client.add_reaction(message, "🇭")
        await client.add_reaction(message, "❕")
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzIzNTk0OTIyNTg0NDQwODMy.DB9kfg.x1p6WDL1JFolCE5QMvhDYQCvOU4')