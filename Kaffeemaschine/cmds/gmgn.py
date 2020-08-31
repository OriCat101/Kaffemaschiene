import aiohttp
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='k!')

botcolor = 0x000088

bot.remove_command('help')


class gmgn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    ##################################################################################################################gm

    @commands.command()
    async def gm(self, ctx):
        embed = discord.Embed(title='', color=botcolor,
                              description=f'{ctx.author.mention} hat ausgeschlafen, und wünscht euch einen guten Morgen🌅', inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    ##################################################################################################################ga

    @commands.command()
    async def ga(self, ctx):
        embed = discord.Embed(title='', color=botcolor,
                              description=f'{ctx.author.mention} wünscht euch einen guten Abend', inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    ##################################################################################################################gt

    @commands.command()
    async def gt(self, ctx):
        embed = discord.Embed(title='', color=botcolor,
                              description=f'{ctx.author.mention} ist angekommen, und schmeißt das übliche "GUTEN TACH LEUDE" in den Raum!', inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    ##################################################################################################################gn

    @commands.command()
    async def gn(self, ctx):
        embed = discord.Embed(title='', color=botcolor,
                              description=f'{ctx.author.mention} wünscht euch eine gute Nacht🌇', inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()


########################################################################################################################


def setup(bot):
    bot.add_cog(gmgn(bot))
