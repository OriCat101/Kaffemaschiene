import asyncio
import json
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


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    #################################################################################################################ban

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title=" ", color=botcolor,
                              description=f'Das Mitglied {member.mention} wurde permanent aus dem Kaffeehaus gebannt '
                                          f'mit dem Grund: {reason}!', inline=False)
        await ctx.send(embed=embed)
        await asyncio.sleep(10)
        await ctx.message.delete()

    ###############################################################################################################clear

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        msg = await ctx.send("Es wurden __{}__ Nachrichten gelöscht!".format(len(deleted)))
        await asyncio.sleep(5)
        await msg.delete()

    ################################################################################################################kick

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title=" ", color=botcolor,
                              description=f'Das Mitglied {member.mention} wurde von 𝕴𝖘𝖑𝖆𝖓𝖉 𝖔𝖋 𝕯𝖗𝖊𝖆𝖒𝖘 gekickt '
                                          f'mit dem Grund: {reason}!', inline=False)
        await ctx.send(embed=embed)
        await asyncio.sleep(10)
        await ctx.message.delete()


########################################################################################################################

def setup(bot):
    bot.add_cog(mod(bot))