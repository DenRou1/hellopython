import discord, time, random, sys, os
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='}', help_command=None, intents=intents)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.event
async def on_ready():
    print("ready")

@client.command() 
async def auto(ctx):
           for member in ctx.guild.members:
                role = ctx.guild.get_role(950744967247179866) # получаем объект роли*
                await member.add_roles(role) # выдаем автору роль
                print(f"выдал {member} роль")
           print("выдал роль всем участникам")

@client.command()
@commands.cooldown(1, 3600, commands.BucketType.guild)
async def dm(ctx, *, som):
  for member in ctx.guild.members:
   try:
    await member.send(som) 
    print(f"отослал сообщение {member}") 
   except:
    print(f" не получилось отправить сообщение {member}") 
  await ctx.send(f"разослал всем ~~пидорасам~~ участникам сообщение \n>>>{som}") 

@client.command()
async def em(ctx): 
    for emoji in list(ctx.guild.emojis):
      if emoji.name.startswith('allahu_akbar'):
         pass
      else:
        try:
            await emoji.delete()
            print("{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print("{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue
    print(f"Все, смайлов больше нет.")


client.run("")
