import settings
import discord
from discord.ext import commands

def bot_start():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        # Carrega os comandos
        for commands_file in settings.COMMANDS_DIR.glob("*.py"):
            if commands_file != "__init__.py":
                await bot.load_extension(f"commands.{commands_file.name[:-3]}")

    bot.run(settings.DISCORD_SECRET_TOKEN)


if __name__ == "__main__":
    bot_start()