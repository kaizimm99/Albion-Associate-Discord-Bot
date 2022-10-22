# Albion-Associate-Discord-Bot
The bot evaluates the attendance of players in a guild. It uses https://zvz.aotools.net/g/ to get the required data.
Based on credits, the bot will make a list of who should get an attendance/associate role.

A player will get a credit at 20:00 UTC every day, if he participated in a fight with 20+ players with 10+ kills during 16:30UTC of the day before and 16:30 of the current day.
Every Saturday at 17:05UTC the credits are evaluatet and a list is created. 
If a player participated at a pvp event on 2 or more days during the last 7 days, he will be market as eligable for attendance/associate role.

Steps to get the bot running:
- change file ".env-model" to ".env"
- fill .env
- setup mongodb database
- setup hosting
