from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

koodi = ""
i = 0

koodi = input("Input code: ")
botit = input("How many bots: ")
nimi = input("Name for bots: ")

while i < int(botit):
    selain = webdriver.Chrome()
    selain.get("http://kahoot.it/")
    kirjoitus = selain.find_element_by_id("game-input")
    kirjoitus.send_keys(koodi)
    kirjoitus.send_keys(Keys.RETURN)
    time.sleep(1)
    nickname = selain.find_element_by_id("nickname")
    nickname.send_keys(nimi, i)
    nickname.send_keys(Keys.RETURN)
    i = i + 1