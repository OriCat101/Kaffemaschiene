from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='k!')

botcolor = 0x000088

bot.remove_command('help')

url = 'https://media.discordapp.net/attachments/712204941501923330/713040083430670446/DKHPB.png'


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ###############################################################################################################help1

    @bot.command()
    async def help(self, ctx):
        if not ctx.author.bot:
            id = str(ctx.author.id)
            embed = discord.Embed(
                color=botcolor)
            embed.set_author(name='𝙼𝚞𝚞𝚗 Hilfe Menü')
            embed.add_field(name='🔰', value='Member Hilfe Menü', inline=False)
            embed.add_field(name='⚜', value='Admin Hilfe Menü', inline=False)
            embed.add_field(name='🏁', value='Zurück zu dieser Seite', inline=False)
            embed.set_thumbnail(url=url)
            embed.set_footer(text='𝙼𝚞𝚞𝚗 Help Menü')
            embed.timestamp = datetime.utcnow()
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction("🔰")
            await msg.add_reaction("⚜")
            await msg.add_reaction("🏁")

    ###############################################################################################################help2

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        id = str(user.id)
        if reaction.message.author.id == self.bot.user.id:
            if not user.bot:
                if reaction.emoji == "🔰":
                    embed = discord.Embed(color=botcolor)
                    embed.set_author(name='𝙼𝚞𝚞𝚗 Hilfe Menü')
                    embed.add_field(name="Guten Morgen", value="k!gm", inline=False)
                    embed.add_field(name="Gute Nacht", value="k!gn", inline=False)
                    embed.add_field(name='Serverinfo', value='k!serverinfo', inline=False)
                    embed.add_field(name='Userinfo', value='k!userinfo *Member*', inline=False)
                    embed.add_field(name="8 Ball", value="k!8ball *Frage*", inline=False)
                    embed.add_field(name="Avatar", value="k!avatar *Member*", inline=False)
                    embed.add_field(name="Ping", value="k!ping", inline=False)
                    embed.add_field(name="Rage", value="k!rage", inline=False)
                    embed.add_field(name="FBI", value="k!fbi", inline=False)
                    embed.add_field(name="Hack", value="k!hack", inline=False)
                    embed.add_field(name='🏁', value='Zurück zur Startseite', inline=False)
                    embed.set_thumbnail(url=url)
                    embed.set_footer(text='𝙼𝚞𝚞𝚗 Help Menü')
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("🔰", user)
                if reaction.emoji == "⚜":
                    embed = discord.Embed(color=botcolor)
                    embed.set_author(name='Admin Hilfe Menü')
                    embed.add_field(name="Clear", value="k!clear *Zahl*", inline=False)
                    embed.add_field(name="Kick", value="k!kick *Member*", inline=False)
                    embed.add_field(name="say", value="k!say *Text*", inline=False)
                    embed.add_field(name="Ban", value="k!ban *Member*", inline=False)
                    embed.set_footer(text='𝙼𝚞𝚞𝚗 Help Menü')
                    embed.timestamp = datetime.utcnow()
                    embed.add_field(name='🏁', value='Zurück zur Startseite', inline=False)
                    embed.set_thumbnail(url=url)
                    embed.set_footer(text='𝙼𝚞𝚞𝚗 Help Menü')
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("⚜", user)
                if reaction.emoji == "🏁":
                    embed = discord.Embed(color=botcolor)
                    embed.set_author(name='𝙼𝚞𝚞𝚗 Hilfe Menü')
                    embed.add_field(name='🔰', value='Member Hilfe Menü', inline=False)
                    embed.add_field(name='⚜', value='Admin Hilfe Menü', inline=False)
                    embed.add_field(name='🏁', value='Zurück zu dieser Seite', inline=False)
                    embed.set_thumbnail(url=url)
                    embed.set_footer(text='𝙼𝚞𝚞𝚗 Help Menü')
                    embed.timestamp = datetime.utcnow()
                    await reaction.message.edit(embed=embed)
                    await reaction.message.remove_reaction("🏁", user)


########################################################################################################################

def setup(bot):
    bot.add_cog(help(bot))
