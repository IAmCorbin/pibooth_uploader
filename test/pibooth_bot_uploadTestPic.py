import settings
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.find('testing') != -1:
        filename='test.jpg'
        fp = open(filename,'rb')
        discordFile=discord.File(fp, filename=filename)
        await message.channel.send(content='Please Stand By. . . ',file=discordFile)
        await message.channel.send('Ok, Im done')
    elif message.content.find('echo') != -1:
        await message.channel.send(message.content)
    elif message.content.find('dumb bot') != -1:
        await message.channel.send('Jerk! Bots have feelings too!!!!')
		
client.run(settings.token)