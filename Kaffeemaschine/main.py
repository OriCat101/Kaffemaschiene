import asyncio
import random

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='k!')

botcolor = 0x000088

bot.remove_command('help')

########################################################################################################################
extensions = ['cmds.alles', 'cmds.help', 'cmds.gmgn', 'cmds.fun', 'cmds.mod', 'cmds.tapply', 'cmds.error', 'cmds.emojis']


########################################################################################################################
@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot ist bereit.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------------------')
    bot.loop.create_task(status_task())


########################################################################################################################
async def status_task():
    while True:
        user = sum(len(s.members) for s in bot.guilds)
        await bot.change_presence(activity=discord.Game('with the community'), status=discord.Status.online)
        await asyncio.sleep(15)

        await bot.change_presence(activity=discord.Game('mit {0} Usern'.format(user)), status=discord.Status.online)
        await asyncio.sleep(15)

        await bot.change_presence(activity=discord.Game('k!help | Help'), status=discord.Status.online)
        await asyncio.sleep(15)

        await bot.change_presence(activity=discord.Activity(name='der Kaffeehaus Community zu'.format(str(len)),
                                                            type=discord.ActivityType.watching))
        await asyncio.sleep(15)


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('Ein Fehler ist in {} aufgetreten: [{}]'.format(extension, error))
########################################################################################################################

bot.run('Njg4ODcyODIwNjkxODI4NzUx.XpbyCw.mBTeP2CY5UFj5wvVtGCIQh1kc9c')
