import os
import datetime
from discord.client import Client
from webscraping.scanActivity import ScanActivityTool
from dotenv import load_dotenv
from database import db

class BotFunctions:
    load_dotenv()

    def __init__(self, client: Client):
        self.client = client

    async def giveAssociateCredits(self):
        timestamp = datetime.datetime.now()
        date = str(timestamp.date())

        creditList = ScanActivityTool.execute(1, 1)
        for player in creditList:
            try:
                playerDocument = db.get_collection("players").find_one({"name": player})
                result = db.get_collection("players").update_one({"_id": playerDocument["_id"]}, {"$set":
                    {'credits': playerDocument["credits"]+1, 'lastAttendance': date}
                })
            except:
                result = db.get_collection("players").insert_one(
                    {"name": player, "credits": 1, "lastAttendance": date}
                )

        message = f'Gave associate credits to {len(creditList)} players.'
        print(str(timestamp) + ": " + message)
        await self.client.get_channel(int(os.getenv("CHANNEL_ID"))).send(message)

    async def updateAssociates(self):
        timestamp = datetime.datetime.now()
        date = str(timestamp.date())

        associateDocument = db.get_collection("associates").find_one()
        associateList = associateDocument["associateList"]

        playersToAdd = []
        playersToRemove = []
        playerDocuments = db.get_collection("players").find({})
        for document in playerDocuments:
            if document["credits"] >= 3 and document["name"]:
                playersToAdd.append(document["name"])
        db.get_collection("players").delete_many({})
        playersToRemove = list(set(associateList) - set(playersToAdd))
        
        result = db.get_collection("associates").update_one({"name": "List of associates"}, {"$set":
            {'associateList': playersToAdd, 'lastUpdated': date}
        })
        
        message = f'Updated List of associates! (old: {len(associateList)}, new: {len(playersToAdd)} players)'
        print(str(timestamp) + ": " + message)

        #Create update message and send in discord
        playersToAdd = list(set(playersToAdd) - set(associateList)) #Only keep player in list, that are not associate already
        if len(playersToAdd) == 0: playersToAdd = ["/"]
        if len(playersToRemove) == 0: playersToRemove = ["/"]
        updateMessageContent = []
        updateMessageContent.append(f'<@&{os.getenv("ASSOCIATE_MANAGER_ID")}>')
        updateMessageContent.append("**" + message + "**")
        updateMessageContent.append("**Grant role to:**")
        for player in playersToAdd:
            updateMessageContent.append(player)
        updateMessageContent.append("\n**Remove role from:**")
        for player in playersToRemove:
            updateMessageContent.append(player)
        updateMessageContent.append("\n_Please react to this message when you applied the changes_")
        updateMessage = '\n'.join(updateMessageContent)
        await self.client.get_channel(int(os.getenv("CHANNEL_ID"))).send(updateMessage)
