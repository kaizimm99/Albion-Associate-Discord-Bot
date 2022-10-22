import os
import discord
from dotenv import load_dotenv
from commands import Commands
from botspecificFunctions import BotFunctions
from discord.message import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is running as {client.user}')

    scheduler = AsyncIOScheduler(timezone="UTC")
    scheduler.start()

    botFunctions = BotFunctions(client=client)
    #Note: ZvZ Activity Tool page updates every day at 16:30UTC
    scheduler.add_job(botFunctions.giveAssociateCredits, trigger='cron', day_of_week='0-6', hour='17') 
    scheduler.add_job(botFunctions.updateAssociates, trigger='cron', day_of_week='6', hour='17', minute='5')


@client.event
async def on_message(msg: Message):
    if (msg.author == client.user):
        return 

    commands = Commands(msg=msg, client=client)

    if commands.check_if_command() == 'no':
        await msg.channel.send("Invalid Command, use !help")
        return

    elif commands.check_if_command() == 'msg':
        return

    elif commands.check_if_command() == 'yes':
        #await all possible commands
        await commands.help_command()
        await commands.getAssociates_command()


if __name__ == '__main__':
    client.run(DISCORD_TOKEN)
    