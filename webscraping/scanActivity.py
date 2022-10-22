import os
import time
from .params import GUILD_NAME, MIN_PLAYERS, MIN_KILLS

from webdriver_manager.firefox import GeckoDriverManager #Driver for Firefox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ScanActivityTool:
    def execute(numberDays, minAttendance, fromUTC = 0, toUTC = 23):
        print("Trying to get list of players...")
        os.environ['MOZ_HEADLESS'] = '1' #Setting to suppress browser window opening on driver.get
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install())) #Firefox
        

        driver.get("https://zvz.aotools.net/g/") #Page updates every day at 16:30UTC
        inputGuild = driver.find_element("id", "search_guild")
        inputPlayers = driver.find_element("id", "minp")
        inputKills = driver.find_element("id", "mink")
        inputDays = driver.find_element("id", "range")
        inputUTC = driver.find_element("id", "cta")
        inputSortBy = driver.find_element("id", "sort")
        inputGuild.clear()
        inputPlayers.clear()
        inputKills.clear()
        inputDays.clear()
        inputGuild.send_keys(GUILD_NAME)
        inputPlayers.send_keys(MIN_PLAYERS)
        inputKills.send_keys(MIN_KILLS)
        inputDays.send_keys(numberDays)
        inputUTC.send_keys(f"{fromUTC}-{toUTC}")
        time.sleep(0.5)

        #navigate to button and click button with enter key
        inputUTC.send_keys(Keys.TAB)
        time.sleep(0.5)
        inputSortBy.send_keys(Keys.TAB)
        time.sleep(2.5)
        #Reason for sleep: Timeout Error in try block because button is not clicked and table is not loading.
        #Reason dor Error: Probably some kind of race condition. Sometimes it runs successfully. Assuming script acts faster then browser can handle it.
        driver.find_element(By.LINK_TEXT, "Filter").click()
        
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'activityTable')))
            table = driver.find_element(By.ID, 'activityTable') # Get specific html-element from page
            table.find_element(By.CSS_SELECTOR, "#activityTable > tbody:nth-child(1)")

            associateList = []
            attendance = minAttendance
            row = 2

            while(attendance >= minAttendance):
                try:
                    name = table.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div/div/table/tbody/tr[{row}]/td[2]/a").get_attribute("innerHTML")
                except:
                    name = table.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div/div/table/tbody/tr[{row}]/td[2]").get_attribute("innerHTML")
                
                attendance = int(table.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div/div/table/tbody/tr[{row}]/td[8]/span/b").get_attribute("innerHTML"))
                if (attendance >= minAttendance):
                    associateList.append(name)
                    row = row + 3

            print(f"Successfully sent list of players ({len(associateList)}).")
            driver.close()
            return associateList
            
        except TimeoutException:
            print("TimoutException when trying to load web-page. No Data.")
            driver.close()
            return []

        