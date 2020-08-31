import asyncio
import random
import time
from datetime import datetime

import aiohttp
import discord
from discord.ext import commands

bild = 'https://media.discordapp.net/attachments/712204941501923330/713040083430670446/DKHPB.png'

bot = commands.Bot(command_prefix='e:')

botcolor = 0x000088

bot.remove_command('help')


class emojis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    ################################################################################################################hack

    @commands.command()
    async def luck(self, ctx):
        embed = discord.Embed(title='', color=botcolor,
                              description=f'{ctx.author.mention}')
        embed.set_thumbnail(
            url='https://media.giphy.com/media/xUA7aSXE8lpQ7REDfi/giphy.gif')
        await ctx.send(embed=embed)
        await ctx.message.delete()

#################################################################################################################fbi

def setup(bot):
    bot.add_cog(emojis(bot))
