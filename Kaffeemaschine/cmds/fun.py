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


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    ################################################################################################################hack

    @commands.command()
    async def hack(self, ctx, txt):
        msg = await ctx.send(f"[▘] loading Hack on {txt}")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▝] getting IP Adress")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▗] **IP Adress:** 192.168.170.255")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▖] succesfully sold IP to the Government")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▘] generating virus for users Discriminator")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▝] Infected the Discriminator")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▗] looking for last DM")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▖] **Last DM was:** Please tell nobody about my nsfw folder!")
        await asyncio.sleep(1.3)
        await msg.edit(content="[▘] leaking personal data")
        await asyncio.sleep(2)
        await msg.edit(content=f"☑ Finished hacking {txt}")
        await asyncio.sleep(1)
        await ctx.send("👍 The completly legal, and dangerous hack has been completed!")
        await ctx.message.delete

    ################################################################################################################kill

    @commands.command()
    async def kill(self, ctx, message):
        if not discord.user.mention:
            await ctx.send('Bitte erwähne jemanden um diesen Command zu benutzen')
        elif message.content('me'):
            Selbstmord = ['SUICIDE IS BADASS!',
                          '{} hat den Fallschirm vergessen'.format(ctx.author)]
            await ctx.send(f'{Selbstmord}')

    ##########################################################################################################lachanfall

    @commands.command()
    async def lol(self, ctx):
        embed = discord.Embed(title='', color=botcolor,
                              description=f'{ctx.author.mention} hat einen Lachanfall 🤣🤣🤣!')
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/712204941501923330/713825123089514566/tenor.gif')
        await ctx.send(embed=embed)

    #################################################################################################################fbi

    @commands.command()
    async def fbi(self, ctx):
        embed = discord.Embed(title='**FBI, OPEN UP**', color=botcolor,
                              description=f'Das FBI ist da um {ctx.author.mention} festzunehmen⛓⛓')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/669970015084085279/700101865731260446/tenor.gif')
        await ctx.send(embed=embed)
        await ctx.message.delete

    ################################################################################################################rage

    @commands.command()
    async def rage(self, ctx):
        embed = discord.Embed(title=' ', color=botcolor,
                              description=f'{ctx.author.mention} **IST AM AUSRASTEN,ALSO ALLE IN DECKUNG!!!🤬**',
                              inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete


########################################################################################################################

def setup(bot):
    bot.add_cog(fun(bot))
