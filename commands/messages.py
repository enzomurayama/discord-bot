import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Comando para apagar mensagens do chat
    @commands.command()
    async def clear(self, ctx, amount="0"):
        if amount == "all":
            await ctx.channel.purge()
            await ctx.send(f"Todas as mensagens deste canal foram apagadas.", delete_after=5)

        elif int(amount) > 0:
            await ctx.channel.purge(limit=int(amount)+1)
            await ctx.send(f"Foram apagadas {amount} mensagens!", delete_after=5)
        

async def setup(bot):
    await bot.add_cog(Messages(bot))