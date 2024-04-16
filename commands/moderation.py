import asyncio
import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Comando para expulsar membro do servidor
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        channel = member.guild.system_channel

        if reason == None:
            reason = "Foi expulso sem motivo!"

        embed = discord.Embed(
            title="Pengus manda você ir embora!",
            colour=0xfc8003
        )
        embed.add_field(name="", value=f"{member.mention} acaba de ser expulso", inline=False)
        embed.add_field(name="", value=f"**Motivo:** {reason}", inline=False)
        embed.set_thumbnail(url=member.avatar.url)

        if channel is not None:
            await channel.send(embed=embed)

        await ctx.guild.kick(member)
        
    
    # Comando para banir membro do servidor
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        channel = member.guild.system_channel

        if reason == None:
            reason = "Foi banido sem motivo!"

        embed = discord.Embed(
            title="Pengus manda você nunca mais voltar!",
            colour=0xff0000
        )
        embed.add_field(name="", value=f"{member.mention} acaba de ser banido", inline=False)
        embed.add_field(name="", value=f"**Motivo:** {reason}", inline=False)
        embed.set_thumbnail(url=member.avatar.url)

        if channel is not None:
            await channel.send(embed=embed)

        await ctx.guild.ban(member)


    # Comando para desbanir membro do servidor
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def unban(self, ctx, member:discord.Member, *, reason=None):
        channel = member.guild.system_channel

        if reason == None:
            reason = "Foi perdoado sem motivo"

        embed = discord.Embed(
            title="Pengus decidiu te perdoar!",
            colour=0x0267f5
        )
        embed.add_field(name="", value=f"{member.mention} acaba de ser desbanido", inline=False)
        embed.add_field(name="", value=f"**Motivo:** {reason}", inline=False)
        embed.set_thumbnail(url=member.avatar.url)

        if channel is not None:
            await channel.send(embed=embed)

        await ctx.guild.unban(member)


    # Comando para mutar um membro do servidor
    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, member:discord.Member, time=0, type='s'):
        if type == 'm':
            time *= 60
        
        elif type == 'h':
            time *= 3600

        await ctx.message.add_reaction("✅")
        await member.edit(mute=True)

        if time != 0:
            await ctx.send(f"> {member.mention} foi mutado por {time}s") 
        else: 
            await ctx.send(f"> {member.mention} foi mutado")

        if time:
            await asyncio.sleep(time)
            await member.edit(mute=False)


    # Comando para desmutar um membro do servidor
    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member:discord.Member):
        await ctx.message.add_reaction("✅")
        await member.edit(mute=False)
        await ctx.send(f"> {member.mention} foi desmutado")

    
    # Comando para retirar o áudio de um membro do servidor
    @commands.command()
    @commands.has_guild_permissions(deafen_members=True)
    async def deafen(self, ctx, member:discord.Member, time=0, type='s'):
        if type == 'm':
            time *= 60
        
        elif type == 'h':
            time *= 3600

        await ctx.message.add_reaction("✅")
        await member.edit(deafen=True)

        if time != 0:
            await ctx.send(f"> {member.mention} não conseguirá escutar nada por {time}s") 
        else: 
            await ctx.send(f"> {member.mention} não consegue escutar")

        if time:
            await asyncio.sleep(time)
            await member.edit(deafen=False)

    
    # Comando para recuperar o áudio de um membro do servidor
    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def undeafen(self, ctx, member:discord.Member):
        await ctx.message.add_reaction("✅")
        await member.edit(deafen=False)
        await ctx.send(f"> {member.mention} agora pode escutar")


async def setup(bot):
    await bot.add_cog(Moderation(bot))