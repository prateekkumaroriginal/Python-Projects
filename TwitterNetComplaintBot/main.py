import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ookla_URL = "https://www.speedtest.net/"
twitter_login_URL = "https://twitter.com/i/flow/login"
download_speed_threshold = 100
upload_speed_threshold = 100
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("PHONE")

driver_path = r"D:\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
driver.maximize_window()

driver.get(ookla_URL)
time.sleep(1)
try:
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
except:
    pass

driver.find_element(By.CLASS_NAME, "start-text").click()
time.sleep(50)
download_speed = float(driver.find_element(By.CLASS_NAME, "download-speed").text)
upload_speed = float(driver.find_element(By.CLASS_NAME, "upload-speed").text)

driver.get(twitter_login_URL)
time.sleep(3)
username = driver.find_element(By.NAME, "text")
username.send_keys(USERNAME)
username.send_keys(Keys.ENTER)
time.sleep(2)

try:
    username = driver.find_element(By.NAME, "text")
    username.send_keys(PHONE)
    username.send_keys(Keys.ENTER)
    time.sleep(2)
except:
    pass

password = driver.find_element(By.NAME, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(5)

if download_speed < download_speed_threshold or upload_speed < upload_speed_threshold:
    message = f"Hey, Internet Provider, why my internet speed is {download_speed} down/ {upload_speed} up when I pay for 100 down/ 100 up?"
    tweet_text = driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
    tweet_text.send_keys(message)
    tweet_button = driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span")
    tweet_button.click()
else:
    print("Speed is upto the mark.")