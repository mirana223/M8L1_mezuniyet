import discord
import asyncio
import yt_dlp
import ffmpeg
from discord.ext import commands
from config import TOKEN
from random_think import gen_pass
from emoji import emoji_olusturucu
from emoji import yazi_tura_atici
from müzisyenbot import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    print('Müzik botu özelliklerini yüklüyorum...')
    await bot.add_cog(Music(bot)) # Müzik cog'unu yüklüyoruz
    print('Müzik botu hazır!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def password(ctx):
    await ctx.channel.send("rastgele şifreniz: "+gen_pass(10))    
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f600") 
@bot.command()
async def nasilsin(ctx):
    await ctx.send("\U0001f600"+" iyiyim sen nasılsın")
@bot.command()
async def emoji(ctx):
    await ctx.channel.send("günlük emojiniz: "+emoji_olusturucu(1))
@bot.command()
async def yazi_tura(ctx):
    await ctx.channel.send(yazi_tura_atici())

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
"""@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await bot.add_cog(Music(bot))

async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.start('SENIN_BOT_TOKENIN_BURAYA')

asyncio.run(main())"""


bot.run(TOKEN)
