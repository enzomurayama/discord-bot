import settings
import discord
from discord.ext import commands

def bot_start():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)

    # Carrega os comandos do Bot
    @bot.event
    async def on_ready():
        for commands_file in settings.COMMANDS_DIR.glob("*.py"):
            if commands_file != "__init__.py":
                await bot.load_extension(f"commands.{commands_file.name[:-3]}")
    
    # Error handler
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.add_reaction("⚠️")
            await ctx.send("> Algo deu errado! O comando está incompleto. Tente utilizar ***!help***")
        
        elif isinstance(error, commands.MissingPermissions):
            await ctx.message.add_reaction("🚫")
            await ctx.send("> Você não possui as permissões para este comando!")


    bot.run(settings.DISCORD_SECRET_TOKEN)

if __name__ == "__main__":
    bot_start()