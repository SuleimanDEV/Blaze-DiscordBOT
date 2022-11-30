import discord
import requests
import json
from discord.ext import commands

client = commands.Bot(command_prefix = "/", case_insensitive = True)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    await client.process_commands(message)


@client.event
async def on_ready(): 
  print(f'[+] Central Online!')

## START

@client.command()
async def start(ctx):
  await ctx.send(f'\n\n🔍 𝗖𝗢𝗠𝗔𝗡𝗗𝗢𝗦: 🔍\n\n                                      > 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 𝗗𝗘 𝗙𝗨𝗟𝗟: /chk 544731xxxxxxxxxx|12|2025|000 (OFF)\n> 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔𝗥 𝗕𝗜𝗡: /bin (bin)\n> 𝐂𝐎𝐍𝐒𝐔𝐋𝐓𝐀𝐑 𝐂𝐏𝐅: /cpf (cpf)\n> 𝐁𝐎𝐓 𝐂𝐑𝐈𝐀𝐃𝐎 𝐁𝐘: $trike#9050 \n\n')



## CPF

@client.command()
async def cpf(ctx, cpf):
  data = requests.get(f"http://suleimandyz.ddns.net/cpf.php?cpf={cpf}").text

  await ctx.send(data)

 ## CNPJ

@client.command()
async def cnpj(ctx, cnpj):
  data = requests.get(f"https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}").json()
  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗖𝗡𝗣𝗝 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍 \n\n"

  try:
    error = data["error"]
    await ctx.send('⚠️ 𝗖𝗡𝗣𝗝 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!')
    return
  except Exception:
    pass

  text += f"> • 𝗖𝗡𝗣𝗝: {data['CNPJ']}\n"
  text += f"> • 𝗡𝗢𝗠𝗘 𝗙𝗔𝗡𝗧𝗔𝗦𝗜𝗔: {data['NOME FANTASIA']}\n"
  text += f"> • 𝗥𝗔𝗭𝗔𝗢 𝗦𝗢𝗖𝗜𝗔𝗟: {data['RAZAO SOCIAL']}\n"
  text += f"> • 𝗦𝗧𝗔𝗧𝗨𝗦: {data['STATUS']}\n"
  text += f"> • 𝗖𝗡𝗔𝗘 𝗗𝗘𝗦𝗖𝗥𝗜𝗖𝗔𝗢: {data['CNAE PRINCIPAL DESCRICAO']}\n"
  text += f"> • 𝗖𝗡𝗔𝗘 𝗖𝗢𝗗𝗜𝗚𝗢: {data['CNAE PRINCIPAL CODIGO']}\n"
  text += f"> • 𝗖𝗘𝗣: {data['CEP']}\n"
  text += f"> • 𝗗𝗔𝗧𝗔 𝗔𝗕𝗘𝗥𝗧𝗨𝗥𝗔: {data['DATA ABERTURA']}\n"
  text += f"> • 𝗗𝗗𝗗: {data['DDD']}\n"
  text += f"> • 𝗧𝗘𝗟𝗘𝗙𝗢𝗡𝗘: {data['TELEFONE']}\n"
  text += f"> • 𝗘𝗠𝗔𝗜𝗟: {data['EMAIL']}\n"
  text += f"> • 𝗧𝗜𝗣𝗢 𝗟𝗢𝗚𝗥𝗔𝗗𝗢𝗨𝗥𝗢: {data['TIPO LOGRADOURO']}\n"
  text += f"> • 𝗟𝗢𝗚𝗥𝗔𝗗𝗢𝗨𝗥𝗢: {data['LOGRADOURO']}\n"
  text += f"> • 𝗡𝗨𝗠𝗘𝗥𝗢: {data['NUMERO']}\n"
  text += f"> • 𝗖𝗢𝗠𝗣𝗟𝗘𝗠𝗘𝗡𝗧𝗢: {data['COMPLEMENTO']}\n"
  text += f"> • 𝗕𝗔𝗜𝗥𝗥𝗢: {data['BAIRRO']}\n"
  text += f"> • 𝗠𝗨𝗡𝗜𝗖𝗜𝗣𝗜𝗢: {data['MUNICIPIO']}\n"
  text += f"> • 𝗨𝗙: {data['UF']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## BLAZE CRASH

@client.command()
async def crash(ctx,):
  data = requests.get(f"http://20.28.179.112/api_crash.php").text

  await ctx.send(data)

## BLAZE DOUBLE

@client.command()
async def double(ctx,):
  data = requests.get(f"http://20.28.179.112/api_double.php").text

  await ctx.send(data)

## TELEFONE
@client.command()
async def telefone(ctx, tel):
  data = requests.get(f"https://www.dualitybuscas.org/privado/consultar_telefone_api.php?consulta={tel}").text

  await ctx.send(data)

## CLEAR

@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.send(f'{amount} messages cleared.')
  await ctx.channel.purge(limit=amount)

## NOME

@client.command()
async def nome(ctx, nome1):
  nome1 = nome1.replace(" ","%20")
  data = requests.get(f"https://dualitybuscas.org/privado/nome.php?consulta={nome1}").text

  await ctx.send(data)

## COMANDOS RANDOM

@client.event 
async def on_ready():
    activity = discord.Game(name='Consultas FREE: discord.gg/171', type=3)
    await client.change_presence(status=discord.Status.online, activity=activity) 
    print('[+] SYSTEM Online!\n') 
    print(f'Nome: {client.user}\n')
## RANDOM

@client.event 
async def on_ready():
    print('[+] SYSTEM Online!\n') 
    print(f'Nome: {client.user}\n')

@client.command() # definimos o comando
async def donate(ctx):  #aqui definimos o comando quando digitarmos /ola o bot vai responder 
    msg = 'Pix [Email]: suleiman | Link PC: https://xvideos.com/porno-gay'  #criamos uma váriavel para a msg
    await ctx.send(msg) 
            #colocamos para o bot mandar essa msg no chat do ctx ou membro 

## NOMES POR CEP

@client.command()
async def cep2(ctx, cep2):
  data = requests.get(f"https://dualitybuscas.org/privado/cep.php?consulta={cep2}").text

  await ctx.send(data)

## PLACA

@client.command()
async def placa(ctx, tel2):
  data = requests.get(f"https://dualitybuscas.xyz/privado/placa.php?consulta={tel2}").text

  await ctx.send(data)
## CEP

@client.command()
async def cep(ctx, cep):
  data = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

  if data.status_code != 200:
    await ctx.send("⚠️ 𝗖𝗘𝗣 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!")
    return

  data = data.json()

  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗖𝗘𝗣 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍 \n\n"

  text += f"> • 𝗖𝗘𝗣: {data['cep']}\n"
  text += f"> • 𝗟𝗢𝗚𝗥𝗔𝗗𝗢𝗨𝗥𝗢: {data['logradouro']}\n"
  text += f"> • 𝗖𝗢𝗠𝗣𝗟𝗘𝗠𝗘𝗡𝗧𝗢: {data['complemento']}\n"
  text += f"> • 𝗕𝗔𝗜𝗥𝗥𝗢: {data['bairro']}\n"
  text += f"> • 𝗖𝗜𝗗𝗔𝗗𝗘: {data['localidade']}\n"
  text += f"> • 𝗘𝗦𝗧𝗔𝗗𝗢: {data['uf']}\n"
  text += f"> • 𝗜𝗕𝗚𝗘: {data['ibge']}\n"
  text += f"> • 𝗦𝗜𝗔𝗙𝗜: {data['siafi']}\n"
  text += f"> • 𝗗𝗗𝗗: {data['ddd']}\n"
  text += f"> • 𝐂𝐑𝐈𝐀𝐃𝐎𝐑: Suleiman\n\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## BIN

@client.command()
async def bin(ctx, bin):
  data = requests.get(f"https://lookup.binlist.net/{bin}")

  if data.status_code != 200:
    await ctx.send("⚠️ 𝗕𝗜𝗡 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!")
    return

  data = data.json()
  
  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗕𝗜𝗡 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍\n\n"

  text += f"> • 𝗕𝗜𝗡: {bin}\n"
  text += f"> • 𝗕𝗔𝗡𝗗𝗘𝗜𝗥𝗔: {data['scheme']}\n"
  text += f"> • 𝗧𝗜𝗣𝗢: {data['type']}\n"
  text += f"> • 𝗡𝗜𝗩𝗘𝗟: {data['brand']}\n"
  text += f"> • 𝗣𝗔𝗜𝗦: {data['country']['name']}\n"
  text += f"> • 𝗦𝗜𝗚𝗟𝗔: {data['country']['alpha2']}\n"
  text += f"> • 𝗕𝗔𝗡𝗗𝗘𝗜𝗥𝗔 𝗣𝗔𝗜𝗦: {data['country']['emoji']}\n"
  text += f"> • 𝗠𝗢𝗘𝗗𝗔: {data['country']['currency']}\n"
  text += f"> • 𝐂𝐑𝐈𝐀𝐃𝐎𝐑: Suleiman\n\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## IP

@client.command()
async def ip(ctx, ip):
  data = requests.get(f"http://ip-api.com/json/{ip}").json()
  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗜𝗣 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍\n\n"

  if data["status"] != "success":
    await ctx.send('⚠️ 𝗜𝗣 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!')
    return

  text += f"> • 𝗣𝗔𝗜𝗦: {data['country']}\n"
  text += f"> • 𝗦𝗜𝗚𝗟𝗔 𝗣𝗔𝗜𝗦: {data['countryCode']}\n"
  text += f"> • 𝗘𝗦𝗧𝗔𝗗𝗢: {data['regionName']}\n"
  text += f"> • 𝗦𝗜𝗚𝗟𝗔 𝗘𝗦𝗧𝗔𝗗𝗢: {data['region']}\n"
  text += f"> • 𝗖𝗜𝗗𝗔𝗗𝗘: {data['city']}\n"
  text += f"> • 𝗖𝗘𝗣: {data['zip']}\n"
  text += f"> • 𝗟𝗔𝗧𝗜𝗧𝗨𝗗𝗘: {data['lat']}\n"
  text += f"> • 𝗟𝗢𝗡𝗚𝗜𝗧𝗨𝗗𝗘: {data['lon']}\n"
  text += f"> • 𝗙𝗢𝗥𝗡𝗘𝗖𝗘𝗗𝗢𝗥 𝗗𝗘 𝗜𝗡𝗧𝗘𝗥𝗡𝗘𝗧: {data['isp']}\n"
  text += f"> • 𝗘𝗠𝗣𝗥𝗘𝗦𝗔: {data['org']}\n"
  text += f"> • 𝗙𝗨𝗦𝗢 𝗛𝗢𝗥𝗔𝗥𝗜𝗢: {data['timezone']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"
  await ctx.send(text)

## COVID

@client.command()
async def covid(ctx, covid):
  data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()
  text = "🔍 𝗖𝗢𝗩𝗜𝗗𝟭𝟵 𝗕𝗥𝗔𝗦𝗜𝗟! 🔍\n\n"

  try:
    error = data["error"]
    await ctx.send('⚠️ 𝗘𝗦𝗧𝗔𝗗𝗢 𝗜𝗡𝗩𝗔𝗟𝗜𝗗𝗢!')
    return
  except Exception:
    pass

  text += f"> • 𝗘𝗦𝗧𝗔𝗗𝗢: {data['state']} - {data['uf']}\n"
  text += f"> • 𝗖𝗔𝗦𝗢𝗦: {data['cases']}\n"
  text += f"> • 𝗠𝗢𝗥𝗧𝗘𝗦: {data['deaths']}\n"
  text += f"> • 𝗖𝗔𝗦𝗢𝗦 𝗦𝗨𝗦𝗣𝗘𝗜𝗧𝗢𝗦: {data['suspects']}\n"
  text += f"> • 𝗖𝗔𝗦𝗢𝗦 𝗗𝗘𝗦𝗖𝗔𝗥𝗧𝗔𝗗𝗢𝗦: {data['refuses']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## SIM OU NÂO

@client.command()
async def eu(ctx):
  data = requests.get(f"https://yesno.wtf/api/?ref=devresourc.es").json()

  text = f"{data['image']}\n"

  await ctx.send(text)

## WHATSAPP

@client.command()
async def wpp(ctx, tel):

  info = ('💯 𝗦𝗘𝗨 𝗟𝗜𝗡𝗞 𝗣𝗔𝗥𝗔 𝗢 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣:\n\n')
  data = ('> https://api.whatsapp.com/send?phone=')
  text = info + data + (tel)

  await ctx.send(text)

## INSTA

@client.command()
async def insta(ctx,):

  info = ('🍎 𝗦𝗘𝗨 𝗟𝗜𝗡𝗞 𝗣𝗔𝗥𝗔 𝗢 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠:\n\n')
  data = ('> https://www.instagram.com/')
  text = info + data + (insta)

  await ctx.send(text)

## GERADORES

## GERADOR DE CPF

@client.command()
async def gerarcpf(ctx,):

    cpf = CPF()
    cpf = cpf.generate(True)

    text = ("• CPF GERADO:\n\n") + (cpf)
    await ctx.send(text)

client.run('BOT TOKEN')
