import random
from discord.ext import commands

class Gamble(commands.Cog):

    # Seleciona uma opção aleatória entre as digitadas
    @commands.command()
    async def rand(self, ctx, *options):
        await ctx.send(random.choice(options)) 
    
    
async def setup(bot):
    await bot.add_cog(Gamble())