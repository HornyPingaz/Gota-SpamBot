import time
from selenium import webdriver
import pyautogui
import sys
import os

current = os.getcwd() 
os.chdir("C:\\Program Files\\NordVPN") 
os.system("nordvpn -c -g 'Australia'") 
os.chdir(current)
print("connected to vpn")
time.sleep(4)

driver = webdriver.Chrome(r"./driver/chromedriver")
driver.get("https://gota.io/web/")

driver.maximize_window()
time.sleep(4)

#accept cookies
cookies = driver.find_element("id","acceptCookies")
cookies.click()
print("accepted cookies")
time.sleep(2)


#connect to storm server
storm = driver.find_element("id","s_Storm")
storm.click()
print("connected to server")
time.sleep(6)

#click play
play = driver.find_element("id","btn-play")
play.click()
print("pressing play button")
time.sleep(40)


#click on chat
chat = driver.find_element("id","chat-input")
print("connecting to chat")
chat.click()

f = open("spamtext", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1.5)

driver.close()
