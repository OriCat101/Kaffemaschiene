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


class alles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    ###############################################################################################################8ball

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *args: str):
        question = ' '.join(args)
        responses = ['YESSIR!',
                     'Ohne Zweifel',
                     'Ich denke, dass geht fit',
                     'Warscheinlich',
                     'Es wurde von Gott so bestimmt',
                     'Vermutlich hast du recht',
                     'Ich tendiere zu der Antwort: JA!'
                     'Natürlich stimmt das!',
                     'Gute Aussichten',
                     'Lasset das Schicksal entscheiden _handing Schicksal 10000Euro_',
                     'System.exe überlastet',
                     'Das kann ich im Augenblick nicht vorhersagen',
                     'hnsddfvvbsfuvfboinvbsfdvunwsdbvidfav',
                     'Vielleicht...',
                     'Nö.',
                     'Schlechte Aussichten',
                     'Ich glaube nicht',
                     'Antrag abgelehnt',
                     'Meine Quellen sagen Nein. Und meine Quellen stimmen immer']
        embed = discord.Embed(title="🎱 8Ball 🎱", color=botcolor,
                              description=f'Frage: {question}\nAntwort: {random.choice(responses)}')
        embed.set_thumbnail(url=bild)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #################################################################################################################say

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send("{}" .format(msg))

    ################################################################################################################ping

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def ping(self, ctx):
        start = time.time()
        async with self.session.get("https://discordapp.com"):
            duration = time.time() - start
        start = time.time()
        async with self.session.get("https://www.youtube.com"):
            duration2 = time.time() - start
        async with self.session.get("https://www.twitch.tv"):
            duration3 = time.time() - start
        embed = discord.Embed(title="", color=botcolor,
                              description='Der Ping von mir beträgt: **{}** ms.\n'
                                          'Der Ping zu Discord beträgt: **{}** ms.\n'
                                          'Der Ping zu YouTube beträgt: **{}** ms.\n'
                                          'Der Ping zu Twitch beträgt: **{}** ms.\n'.format(
                                  round(self.bot.latency * 1000), round(duration * 1000), round(duration2 * 1000),
                                  round(duration3 * 1000)))
        await ctx.send(embed=embed)
        await ctx.message.delete()

    ##############################################################################################################avatar

    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        if not ctx.author.bot:
            member = user or ctx.author
            embed = discord.Embed(color=botcolor)
            embed.set_image(url=member.avatar_url)
            embed.set_footer(text="Das Profilbild von {}".format(member.name),
                             icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    ############################################################################################################userinfo

    @commands.command()
    async def userinfo(self, ctx, user: discord.Member = None):
        if ctx.author.bot:
            return
        else:
            user = user or ctx.author
            user_passed1 = (datetime.now() - user.joined_at).days
            user_created1 = (datetime.now() - user.created_at).days
            l = list(permi for permi, value in user.guild_permissions if str(value) == 'True')
            i = '\n📍 '.join(l)
            rl = len(list(role.mention for role in user.roles if not role.name == "@everyone"))
            embed = discord.Embed(title="{}'s Info".format(user.name), description="Hier ist das Benutzerprofil",
                                  color=botcolor)
            embed.add_field(name="Name", value=user.name, inline=True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Discord Tag", value="#{0}".format(user.discriminator), inline=True)
            embed.add_field(name="Status", value=user.status, inline=True)
            embed.add_field(name="Höchste Rolle", value=user.top_role.mention, inline=True)
            embed.add_field(name="Rollen", value=rl, inline=True)
            embed.add_field(name='User Rechte:', value='📍 {0}'.format(i), inline=False)
            embed.add_field(name="Beigetreten am:",
                            value=(
                                "{} (vor {} Tagen!)".format(user.joined_at.strftime("%d %b %Y %H:%M"), user_passed1)),
                            inline=False)
            embed.add_field(name="Erstell am:", value=(
                "{} (vor {} Tagen!)".format(user.created_at.strftime("%d %b %Y %H:%M"), user_created1)), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text='Die Nachricht wurde angefordert von {}'.format(ctx.message.author),
                             icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    ############################################################################################################roleinfo

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def roleinfo(self, ctx, role: discord.Role):
        if not ctx.message.author.bot:
            server = ctx.guild
            role_info1 = (datetime.utcnow() - role.created_at).days
            l = list(permi for permi, value in role.permissions if str(value) == 'True')
            i = '\n📍 '.join(l)
            embed = discord.Embed(color=role.color)
            embed.add_field(name='__Role Info__', value='** **', inline=False)
            embed.add_field(name='Name der Rolle:', value='{0}'.format(role.name), inline=False)
            embed.add_field(name='Rollen-ID:', value='{0}'.format(role.id), inline=True)
            embed.add_field(name='Farbe der Rolle:', value='{0}'.format(role.color), inline=True)
            embed.add_field(name='Wird die Rolle rechts angezeigt?:', value='{0}'.format(role.hoist), inline=True)
            embed.add_field(name='Position der Rolle:', value='{0}'.format(role.position), inline=True)
            embed.add_field(name='Erwähnbare Rolle:', value='{0}'.format(role.mentionable), inline=True)
            embed.add_field(name='Rollen-Berechtigungen:', value='📍 {0}'.format(i), inline=False)
            embed.add_field(name='Erstellt am:', value='{}'.format(
                "{} (Vor {} Tagen erstellt!)".format(role.created_at.strftime("%d. %b. %Y %H:%M"), role_info1)),
                            inline=False)
            author = ctx.message.author
            embed.set_thumbnail(url="{0}".format(server.icon_url))
            embed.set_footer(text='Die Nachricht wurde angefordert von {0}'.format(author),
                             icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    ##########################################################################################################serverinfo

    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def serverinfo(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.guild
            server_info1 = (datetime.utcnow() - server.created_at).days
            rl = list(role.mention for role in server.roles if not role.name == "@everyone")
            Bot = list(member.bot for member in server.members if member.bot is True)
            user = list(member.bot for member in server.members if member.bot is False)
            embed = discord.Embed(title="Server Info", color=botcolor)
            embed.add_field(name='Name:', value='{}'.format(server.name), inline=True)
            embed.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
            embed.add_field(name='Region:', value='{}'.format(server.region), inline=True)
            embed.add_field(name='Mitgliederanzahl:', value='{} Mitglieder'.format(server.member_count), inline=True)
            embed.add_field(name='Bot-Anzahl:', value='{} Bots'.format(str(len(Bot))), inline=True)
            embed.add_field(name='Anzahl der Menschen:', value='{} users'.format(str(len(user))), inline=True)
            embed.add_field(name='Großer Server:', value='{} (250+ Mitglieder)'.format(server.large), inline=True)
            embed.add_field(name='Serverbesitzer:', value='{}'.format(server.owner), inline=True)
            embed.add_field(name='Serverrollen:', value=str(len(rl)), inline=True)
            embed.add_field(name='Erstellt am:', value='{}'.format(
                "{} (Vor {} Tagen erstellt!)".format(server.created_at.strftime("%d. %b. %Y %H:%M"), server_info1)),
                            inline=False)
            embed.set_thumbnail(url="{0}".format(server.icon_url))
            embed.set_footer(text='Die Nachricht wurde angefordert von {}'.format(ctx.message.author),
                             icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg1 = await ctx.send(embed=embed)

    ##################################################################################################autoreact-feedback

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 713858058614341633:
            await message.add_reaction("👍")
            await message.add_reaction("❤")
            await message.add_reaction("👎")

    ################################################################################################autoreact-vorschläge

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 713858300520955904:
            await message.add_reaction("✅")
            await message.add_reaction("❎")

    ############################################################################################################coinflip

    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx):
        choices =  ['Kopf', 'Zahl']
        rancoin = random.choice(choices)
        embed = discord.Embed(title="💶Coinflip💶", color=botcolor,
                              description=f' Das Ergebnis ist: {rancoin}')
        embed.set_thumbnail(url=bild)
        await ctx.send(embed=embed)
        await ctx.message.delete()


########################################################################################################################

def setup(bot):
    bot.add_cog(alles(bot))
