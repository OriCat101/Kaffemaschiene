import asyncio
import random
import time
from datetime import datetime

import aiohttp
import discord
from discord.ext import commands

bild = 'https://media.discordapp.net/attachments/712204941501923330/713040083430670446/DKHPB.png'

bot = commands.Bot(command_prefix='k!')

botcolor = 0x000088

bot.remove_command('help')


class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    ####################################################################################################################

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title="Unbekannter Command",
                                  description="Der Command, den du versucht hast zu nutzen ist entweder falsch eingegeben oder existiert nicht!",
                                  color=botcolor)
            embed.set_thumbnail(url=bild)
            await ctx.send(embed=embed)
            await asyncio.sleep(7.5)
            await ctx.message.delete()


########################################################################################################################

def setup(bot):
    bot.add_cog(error(bot))