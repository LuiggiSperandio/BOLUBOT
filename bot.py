import os
from twitchio.ext import commands
import text_archive
from random import randint
import re

from dotenv import load_dotenv()
load_dotenv()

# set up the bot
bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

print('bot ontheliner')

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event()
async def event_message(ctx):
    # 'Runs every time a message is sent in chat.'
    print(ctx.author.name)
    print(ctx.author.is_mod)
    print(ctx.content)

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # Bot agression check  
    if bool(re.search('bot.*burro', ctx.content.lower())):
        await ctx.channel.send('BibleThump')
        return

    # Soneca Check
    if bool(re.search(' soneca ', ctx.content.lower())):
        await ctx.channel.send('PogChamp Oda mentioned PogChamp')
        return

    # Enzo Check
    if bool(re.search(' soneca ', ctx.content.lower())):
        await ctx.channel.send('PogChamp Enzo mentioned PogChamp')
        return

    # Adair Check
    if bool(re.search(' oda | adair ', ctx.content.lower())):
        await ctx.channel.send('Meu deus!!! Falou algo pesado aí, aqui chegou a cair a conexão com o chat! LUL')
        return

    # Salve Check
    if 'salve' in ctx.content.lower():
        await ctx.channel.send(f"Salve, @{ctx.author.name}!")
        return
    
    #Roleta Russa
    a=0
    # Mod micro agression
    if randint(1, 5) == 3 and ctx.author.is_mod:
        a=1
        await ctx.channel.send(f'Mod é broxa @{ctx.author.name}')
    # Boludo micro agression
    if (randint(1, 30) == 15) and a == 0:
        a=1
        await ctx.channel.send('15 anos no Brasil e não fala um portugues sem sotaque')
    # Viva o funk
    if (randint(1, 10) == 5) and a == 0:
        await ctx.channel.send('Bota um funk ai pra nois Boludo')
    a=0
    #End Roleta Russa



@bot.command(name='shrek')
async def test(ctx):
    await ctx.send(text_archive.a)
    await ctx.send(text_archive.b)
    await ctx.send(text_archive.c)
    await ctx.send(text_archive.d)
    await ctx.send(text_archive.e)
    await ctx.send(text_archive.f)
    await ctx.send(text_archive.g)


if __name__ == "__main__":
    bot.run()