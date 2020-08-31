import asyncio
import random
from datetime import datetime

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='k!')

botcolor = 0x000088

applylist = [713045582452752444]
answers = ["Ich mag deine Antwort:", "Interessante Antwort.", ":eyes:.Gute Antwort.", "Großartig!"]
questions = [" Uh Nice du bist bei einer Frage! ", "Huh? Wo bin ich? Oh heyo!", "Deine Antworten - Die sind Super!",
             "Ich bin ein Bot. Beantworte die Frage 😂"]


class tapply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ####################################################################################################################

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.category.id in applylist:
            await channel.send(
                "Hallöchen du da! Ja, genau du! Ich bin dein Bewerbungsassistent, \n Ich werde dir heute bei deiner Bewerbung ein paar Fragen stellen. \nMöchtest du "
                "denn Starten?".format(
                    self.bot.user.name))
            await asyncio.sleep(5)
            await channel.send("Gebe **__k!startapply__** zum starten ein!")

    ####################################################################################################################

    @commands.command()
    @commands.cooldown(1, 800, commands.BucketType.channel)
    async def startapply(self, ctx):
        if not ctx.channel.category.id in applylist:
            return

        def pred(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send(
            "♥-lich Wilkommen in unserem Bewerbungsprogramm! Bist du bereit? \n Bitte antworte mit **y**, wenn du bereit bist, und ich dir meine Fragen stellen darf. Andernfalls antworte mit **n**.")
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=60.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert..., versuchs später nochmal!')
                return
            if msg.content == "y":
                await ctx.send("Großartig!!! \n Beginnen wir mit wenigen Erläuterungen.")
                break
            elif msg.content == "n":
                await ctx.send("Oh ok. bis zum nächsten mal dann!")
                return
            else:
                await ctx.send("Ops, ungültige Eingabe! \n Schreibe **y** für Start und **n** für Ablehnung.")
                continue
        embed = discord.Embed(
            color=botcolor)
        embed.set_author(name='Vielen Dank für deine Bewerbung! Die erste Frage startet in 20 Sekunden.')
        embed.add_field(name='Regeln:',
                        value='Wenn du etwas geschrieben hast werde ich zur nächten Frage gehen.\n Bitte antworte '
                              'wahrheitsgemäß und Ordentlich ',
                        inline=False)
        embed.add_field(name='Time:', value='Du hast für jede Frage 120 Sekunden Zeit, bevor die nächste beginnt.',
                        inline=False)
        embed.add_field(name='Überspringen und Beenden',
                        value='Du kannst Fragen überspringen mit **skip**\nWenn du abbrechen willst schreibe **end**',
                        inline=False)
        embed.set_thumbnail(
            url=self.bot.user.avatar_url)
        embed.set_footer(text='💙Bewerbungen💙')
        await ctx.send(embed=embed)
        await asyncio.sleep(20)
        await ctx.send("Ok, lass uns mit deiner ersten Frage beginnen! \n Wie alt bist du? 1/7")
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=120.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert...\nGehen wir zur nächsten Frage!')
                age = "Zeitfenster überschritten"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                age = "übersprungen"
                break
            elif "end" == msg.content:
                await ctx.send(
                    "Och wie schade😭. Dann lösche ich jetzt deine Bewerbung. Aber vielleicht sieht man sich ja irgendwann mal")
                return
            else:
                age = msg.content
                await ctx.send("Okay, du bist **{}** Jahre alt.".format(age))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nWarum bewirbst du dich? 2/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=120.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert...\nWeiter mit der nächsten Frage!')
                reason = "Zeitfenster überschritten"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                reason = "übersprungen"
                break
            elif "end" == msg.content:
                await ctx.send(
                    "Och wie schade😭. Dann lösche ich jetzt deine Bewerbung. Aber vielleicht sieht man sich ja irgendwann mal")
                return
            else:
                reason = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), reason))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nFür welchen Rang bewirbst du dich? 3/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=120.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert...\nWeiter mit der nächsten Frage!')
                mod = "Zeitfenster überschritten"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                mod = "übersprungen"
                break
            elif "end" == msg.content:
                await ctx.send(
                    "Och wie schade😭. Dann lösche ich jetzt deine Bewerbung. Aber vielleicht sieht man sich ja irgendwann mal")
                return
            else:
                mod = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), mod))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nWas ist dein Können? 4/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=120.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert...\nWeiter mit der nächsten Frage!')
                skills = "Zeitfenster überschritten"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                skills = "übersprungen"
                break
            elif "end" == msg.content:
                await ctx.send(
                    "Och wie schade😭. Dann lösche ich jetzt deine Bewerbung. Aber vielleicht sieht man sich ja irgendwann mal")
                return
            else:
                skills = msg.content
                await ctx.send("Du hast erstaunliche Fähigkeiten!\n{} ".format(skills))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send(
            "{}\nWelche Sprachen kannst du alle? 5/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=120.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert...\nWeiter mit der nächsten Frage!')
                langs = "Zeitfenster überschritten"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                langs = "übersprungen"
                break
            elif "end" == msg.content:
                await ctx.send(
                    "Och wie schade😭. Dann lösche ich jetzt deine Bewerbung. Aber vielleicht sieht man sich ja irgendwann mal")
                return
            else:
                langs = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), langs))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send(
            "{} {}-chan.\nWas machst du, wenn dich jemand beleidigt hat? 6/7".format(random.choice(questions),
                                                                                     ctx.author.name))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=120.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert...\nWeiter mit der nächsten Frage!')
                offended = "Zeitfenster überschritten"
                break
            if "skip" == msg.content:
                offended = "übersprungen"
                await ctx.send("Ok, diese Frage wird übersprungen.")
                break
            elif "end" == msg.content:
                await ctx.send(
                    "Och wie schade😭. Dann lösche ich jetzt deine Bewerbung. Aber vielleicht sieht man sich ja irgendwann mal")
                return
            else:
                offended = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), offended))
                break
        await ctx.send(
            "──────────────────────────────────────────────────")
        await asyncio.sleep(3)
        await ctx.send("{}\nMöchtest du etwas hinzufügen? 7/7".format(random.choice(questions)))
        while True:
            try:
                msg = await self.bot.wait_for('message', check=pred, timeout=120.0)
            except asyncio.TimeoutError:
                await ctx.send('Das hat mir zu lange gedauert...\nGehen wir zum Ende!')
                add = "Zeitfenster überschritten"
                break
            if "skip" == msg.content:
                await ctx.send("Ok, diese Frage wird übersprungen.")
                add = "übersprungen"
                break
            elif "end" == msg.content:
                await ctx.send("Das ist traurig. Ich werde Ihre Bewerbung löschen. Bis zum nächsten Mal!")
                return
            else:
                add = msg.content
                await ctx.send("{}\n{} ".format(random.choice(answers), add))
                break
        await ctx.send(
            "Vielen Dank für Ihre Bewerbung. Ich habe es an die Entwickler geschickt"
            "und werde Sie kontaktieren, wenn es etwas Neues gibt!")
        embed = discord.Embed(
            color=botcolor)
        embed.set_author(name='Bewerbung von {}'.format(ctx.author, ))
        embed.add_field(name="Server:", value=ctx.guild, inline=False)
        embed.add_field(name="Bewerbung für:", value=mod, inline=False)
        embed.add_field(name="Alter:", value=age, inline=False)
        embed.add_field(name='Grund der Bewerbung', value=reason, inline=False)
        embed.add_field(name='Sprachen', value=langs, inline=False)
        embed.add_field(name='Skills', value=skills, inline=False)
        embed.add_field(name='Was machst du, wenn dich jemand beleidigt hat?', value=offended, inline=False)
        embed.add_field(name='Kommentar:', value=add, inline=False)
        embed.set_thumbnail(
            url=self.bot.user.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='💙Bewerbungen💙')
        server = self.bot.get_guild(712202250792992768)
        for i in server.categories:
            if i.id == 713044854044622929:
                channel = await server.create_text_channel(name="{}s Bewerbung".format(ctx.author.name),
                                                           category=i)
                await channel.send("@here", embed=embed)


########################################################################################################################

def setup(bot):
    bot.add_cog(tapply(bot))
