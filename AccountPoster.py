import getpass
from colorama import Fore, Style
from colorama import init, Fore, Back, Style
init(convert=True)
input("Welcome to Account GenBot!\nPlease remember that this software was not designed for any illegal activity &\nthe developer will not be held responsible for any improper use of the program.\nPress enter if you understand that.")
import os, time, datetime, random, asyncio, aiohttp, json, discord, time, colorama, requests
from itertools import cycle
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet
token = open('token.txt', 'r').readline()
client = commands.Bot(command_prefix='!')
client.remove_command('help')
os.system('cls')
print('Welcome, ' + getpass.getuser())
activity = discord.Game(name='Discord Account GenBot')

@client.event
def on_ready():
    print('Bot is running, do not close this window.')
    print((Fore.RED + '       ' + ' • ' + Fore.WHITE + ' ' + Style.RESET_ALL),
      end='')
    print('Current Discord Bot Name: ' + client.user.name)
    print('')
    import itertools, threading, time, sys
    done = False

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rReady... ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

        sys.stdout.write('')

    t = threading.Thread(target=animate)
    t.start()
    await client.change_presence(status=(discord.Status.idle), activity=activity)


@client.command()
def clear(ctx):
    os.system('cls')
    print('')
    print('')
    print((Fore.RED + '       ' + ' • ' + Fore.WHITE + ' ' + Style.RESET_ALL),
      end='')


@client.command()
def ping(ctx):
    await ctx.send('Pong!')


@client.command()
def help(ctx):
    await ctx.send('\n\t\n**This is the free version of this bot.**\n\t\nBot commands:\n```!spotify - generates a spotify account\n!netflix - generates a netflix account\n!hulu - generates a hulu account\n!stock - shows the stock for each account type```')


@client.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
def spotify(ctx):
    author = ctx.message.author
    with open('spotify.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('spotify.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Spotify Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await ctx.send(f"{User}:{PassFixed}")


@client.event
def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention} {exception}")


@client.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
def netflix(ctx):
    author = ctx.message.author
    with open('netflix.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('netflix.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Netflix Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await ctx.send(f"{User}:{PassFixed}")


@client.event
def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention} {exception}")


@client.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
def hulu(ctx):
    author = ctx.message.author
    with open('hulu.txt', 'r') as (f):
        text_spo = f.readlines()
        while True:
            randomline = random.choice(text_spo)
            combo = randomline.split(':')
            User = combo[0]
            Pass = combo[1]
            PassFixed = Pass.rstrip()
            if len(randomline) == 0:
                continue
            with open('hulu.txt', 'w') as (c):
                for line in text_spo:
                    if line.strip('\n') != f"{User}:{PassFixed}":
                        c.write(line)

            break

        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Hulu Account at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await ctx.send(f"{User}:{PassFixed}")


@client.event
def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention} {exception}")


@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
def stock(ctx):
    author = ctx.message.author
    num_lines = sum(1 for line in open('spotify.txt'))
    num_lines2 = sum(1 for line in open('netflix.txt'))
    num_lines3 = sum(1 for line in open('hulu.txt'))
    await ctx.send('--------------------------------------')
    await ctx.send('Current **Spotify** Stock: ' + str(num_lines))
    await ctx.send('Current **Netflix** Stock: ' + str(num_lines2))
    await ctx.send('Current **Hulu** Stock: ' + str(num_lines3))
    await ctx.send('--------------------------------------')


client.run(token.strip())