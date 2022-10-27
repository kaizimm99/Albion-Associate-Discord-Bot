# Albion-Associate-Discord-Bot
This bot evaluates the attendance of players in a guild. It uses https://zvz.aotools.net/g/ to get the required data. Based on a credit-system, the bot will make a list of who should get an attendance/associate role.

## Technologies
- Python (Bot)
- MongoDB (Credits and Associate List)
- Raspberry PI (Hosting)

## Credit System
Credits will be given out at 20:00 UTC every day to whoever participated at a pvp event with the following parameters at least once.
### Parameters:
- 20 or more players in the battle
- at least 10 deaths during the battle

## Who will be eligable for associate rank?
Every sunday at 20:05UTC the credits are evaluatet and a list is created. Any player that participated in a pvp event (note the parameters) on **2 or more days** during the **last 7 days** will be market as eligable for attendance/associate role. Once the list is evaluated on sunday 22:05 UTC, a list of players that should be granted the associate role is sent as a discord message. All existing credits will be removed/reset for the following week.

## Commands
- !getassociates (get the current list of associates)

## Steps to get the bot running:
- change file ".env-model" to ".env"
- fill .env
- in file "params.py" in directory webscraping, change GUILD_NAME to your guilds name
- setup mongodb database
- setup hosting

## Hosting
For initial private use the bot was self hosted on a raspberry pi. The bot.py script is executed via @reboot cronjob. You may decide on a different hosting method.


_Creator: schmusekai#3971 (Discord)_
