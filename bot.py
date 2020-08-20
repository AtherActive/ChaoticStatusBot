import discord
import time

from requests.exceptions import ConnectionError
from mcstatus import MinecraftServer
from discord.ext import commands

# some default values...
client = discord.Client()
consolePrefix = 'ServerBot // '
CP = consolePrefix
global ServerOnline
ServerOnline = 1
css_oldStatus = 1

#Admin account. Change to owners token  (only one person has access to admin commands)
admin = 189317034360832001

#Customizable during runtime soontm, for now on restart


# Bot prefix, used in rewriting code...
bots = commands.Bot(command_prefix=',')

# set server....
server = MinecraftServer.lookup("hub.chaoticscave-mc.nl:2559")

# Checks and updates server status really
ids = 743953801542893588

async def CheckServerStat(old):
    print("Checking server status....")
    try:
        print(server.ping())
        if old <= 0:
            print("Server restarting")
            return
        ServerOnline = 1
        return ServerOnline

    except Exception:
        channel = client.get_channel(ids)
        print(old)
        ServerOnline = 0
        if old != 0:
            print("server ded")
            test = client.get_channel(ids)
            await test.send("test")
        return ServerOnline

# for when me 0iq
def printD(message):
    printd(message)

# Customized print command. Not special rlly
def printd(message):
    if message == '':
        message = 'no message added you fuck'
    else:
        print(consolePrefix, message)


# Sends a message on discord
async def sendMessage(inpu, sendText):
    printd('Message is valid, sending!')
    # Checks what type of message we want. 0: Regular, 1: Maintenance
    send = sendText
    printd(send)
    await inpu.channel.send(send)
    if inpu.author == client.user:
        return
    else:
        await inpu.delete()
        printd('Deleted original message')

async def publicCommands(message):
    printd(message.author.id)

    # Dynmap command
    if message.content.startswith(',dynmap'):
        await sendMessage(message, "**The dynamic map for Magma Anarchy** \n http://magma.chaoticscave-mc.nl/")
        return

    if message.content.startswith(',website'):
        await sendMessage(message, "**Visit our website for info and the latest server news** \n https://chaoticscave.net/")
        return

    # Server info
    elif message.content.startswith(',info'):
        await sendMessage(message, "**We own three servers:** \n \n **EMERALD** \n > Vanilla Survival \n > IP: hub.chaoticscave-mc.nl \n > STS: Down for Maintenance \n \n **MAGMA** \n > Modded Anarchy \n > IP: hub.chaoticscave-mc.nl \n > STS: Stable")
        return


# checks console not important
@client.event
async def on_ready():
    printd('Logged in as {0.user}'.format(client))

# Legacy code, being rewritten to work with bot.command
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    ServerOnline = await CheckServerStat()
# Welcome to the IF-spam. all commands rlly
    if message.author.id == admin:
        #Test Commands. Used as a starting Point
        if message.content.startswith(',test-crash'):
            await sendMessage(message, "**TESTSERVER**: Server has crashed. Restarting now!")
            return

        elif message.content.startswith(',test-restart'):
            await sendMessage(message, '**TESTSERVER**: Server is restarting.. Back soon!')
            return

        elif message.content.startswith(',test-start'):
            await sendMessage(message, "**TESTSERVER**: Server is starting up. Standby!")
            return

        elif message.content.startswith(',test-stop'):
            await sendMessage(message, "**TESTSERVER**: Server is shutting down.")
            return

        elif message.content.startswith(',test-maintenance'):
            await sendMessage(message, "**TESTSERVER**: Server is shutting down for maintenance. Read the post for more info.")
            return

        elif message.content.startswith(',test-updated'):
            await sendMessage(message, "**TESTSERVER**: Server has been updated. Read the latest post for more info.")
            return

        # Magma Server Commands
        if message.content.startswith(',magma-crash'):
            await sendMessage(message, "**MAGMA**: Server has crashed. Restarting now!")
            return

        elif message.content.startswith(',magma-restart'):
            await sendMessage(message, '**MAGMA**: Server is restarting.. Back soon!')
            return

        elif message.content.startswith(',magma-start'):
            await sendMessage(message, "**MAGMA**: Server is starting up. Standby!")
            return

        elif message.content.startswith(',magma-stop'):
            await sendMessage(message, "**MAGMA**: Server is shutting down.")
            return

        elif message.content.startswith(',magma-maintenance'):
            await sendMessage(message, "**MAGMA**: Server is shutting down for maintenance. Read the post for more info.")
            return

        elif message.content.startswith(',magma-updated'):
            await sendMessage(message, "**MAGMA**: Server has been updated. Read the latest post for more info.")
            return

        # Custom message support
        elif message.content.startswith(',custom-msg'):
            msg = message.content
            msg = msg.replace(',custom-msg', '')
            printd(msg)
            await sendMessage(message, msg)
            return
        # Some minor annoyances in command form
        # Flans Mod crash
        elif message.content.startswith(',flans'):
            await sendMessage(message, "**MAGMA**: Some libtard did not listen to the announcements and killed the server with Flans Mod. We thank you all:rage:. It will now restart")
            return

        elif message.content.startswith(',windows'):
            await sendMessage(message, ":desktop: Windows is the big funny (not) and now the server is down for updating... We all like you windows! This will take a while.")
            return

        else:
            await publicCommands(message)
            printd(message.author)
            printd(message.content)
    else:
        if message.author == client.user:
            return
        else:
            await publicCommands(message)


client.run('NzQ1NjQ0Nzg5ODU2MzM4MDQ3.Xz0x0w.wXJ58fFJmERMhU25I0-eBYEZE24')

