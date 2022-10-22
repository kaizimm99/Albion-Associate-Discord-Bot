from discord.client import Client
from discord.message import Message
from webscraping.params import GUILD_NAME
from dotenv import load_dotenv
from database import db
import os

class Commands:
    load_dotenv()
    channel_id = os.getenv("CHANNEL_ID")

    def __init__(self, msg: Message, client: Client):
        self.msg = msg
        self.client = client
        self.content = self.msg.content.split(" ")

    def check_if_command(self):
        first_char = self.content[0][0]
        first_word = self.content[0][1:]
        commands_quantity = len(self.content)

        command_rules = [first_word == 'help' and commands_quantity == 1,
                        first_word == 'getassociates' and commands_quantity == 1]

        if first_char == '!':
            if any(command_rules):
                return 'yes'
            else:
                return 'no'

        return 'msg'

    async def help_command(self):
        if self.content[0] == "!help":
            await self.msg.channel.send("Use !getassociates to get a list of all associates.")

    async def getAssociates_command(self):
        if self.content[0] == "!getassociates":
            await self.msg.channel.send("Loading...")
            
            messageContent = [f"**List of {GUILD_NAME} associates:**"]
            list = db.get_collection("associates").find_one({"name": "List of associates"})["associateList"]

            for player in list:
                messageContent.append(player) 
            messageContent.append(f"\nTotal number of players: {len(list)}")
            message = '\n'.join(messageContent)

            await self.msg.channel.send(message)