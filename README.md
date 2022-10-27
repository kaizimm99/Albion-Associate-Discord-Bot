# Albion-Associate-Discord-Bot
Tis bot evaluates the attendance of players in a guild. It uses https://zvz.aotools.net/g/ to get the required data. Based on a credit-system, the bot will make a list of who should get an attendance/associate role.

## Technologies
- Python (Bot)
- MongoDB (Credits and Associate List)
- Raspberry PI (Hosting)

## Credit System
Credits will be given out at 20:00 UTC every day to whoever partivipated at a pvp event with the following parametrs at least once.\n
### Parameters:\n
- 20 or more players in the battle
- at least 10 deaths during the battle

## Who will be eligable for associate rank?
Every sunday at 20:05UTC the credits are evaluatet and a list is created. Any player that participated at a pvp event (note the parameters) on **2 or more days** during the **last 7 days**, he will be market as eligable for attendance/associate role.

## Steps to get the bot running:
- change file ".env-model" to ".env"
- fill .env
- setup mongodb database
- setup hosting

## Hosting
For initial private use the bot was self hosted on a raspberry pi. The bot.py script is executed via @reboot cronjob. You may decide on a different hosting method.
