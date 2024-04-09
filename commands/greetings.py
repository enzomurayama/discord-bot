import settings
import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Mensagem de boas-vindas 
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel

        embed = discord.Embed(
            title=f"Boas-vindas a {member.guild}!",
            description="Agora você faz parte deste servidor incrível! \nNão se esqueça de obedecer as regras.",
            colour=0x07a330
        )
        embed.add_field(name=":placard: Por onde começar?", value="Para começar, que tal digitar [***!help***]? \nEste comando exibe a lista de todos os comandos disponíveis", inline=False)
        embed.set_image(url="https://i.pinimg.com/originals/50/24/01/502401a4090714971eff352ea91b899c.gif")

        if channel is not None:
            await channel.send(f"Bem-vindo, {member.mention}! :penguin:")
            await channel.send(embed=embed)

    # Mensagem de apresentação do bot
    @commands.command(
        description="Comando que apresenta informações sobre o bot.",
        brief="Informações sobre o bot"
    )
    async def sobre(self, ctx):
        embed = discord.Embed(
            title=f"Olá, meu nome é {ctx.bot.user.name}!",
            description="Sou um bot capaz de realizar muitas tarefas e estou aqui para melhorar a sua experiência com este servidor!",
            colour=0x07a330
        )
        embed.add_field(name=":card_box: Repositório", value="Você pode me encontrar aqui: \nhttps://github.com/enzomurayama/discord-bot\a", inline=False)
        embed.add_field(name=":man_mage: Criador", value=f"Projeto desenvolvido por: <@{settings.ALWABES_SECRET_ID}>", inline=False)
        embed.set_image(url="https://i.pinimg.com/originals/45/1e/3a/451e3afe79bed487254964431dfb168d.gif")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Greetings(bot))