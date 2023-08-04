from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

# get access to environment variables
load_dotenv()

class InternetSpeedTwitterBot:
    def __init__(self, driver_path) -> None:
        # setting up the selenium webdriver to work with Chrome using chromedriver
        service = Service(executable_path=driver_path)
        options = ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=service, options=options)
        
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get('http://www.speedtest.net')
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '.start-button a').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        self.driver.quit()


    def tweet_at_provider(self):
        self.driver.maximize_window()
        self.driver.get('http://www.twitter.com')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a').click()
        time.sleep(2)
        self.driver.find_element(By.TAG_NAME, 'input').send_keys(os.environ.get('TWITTER_USER') + Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(os.environ.get('TWITTER_PASSWORD') + Keys.ENTER)
        time.sleep(2)
        
        tweet = 'Testing my bot'
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(tweet)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div').click()

bot = InternetSpeedTwitterBot(os.environ.get('CHROMEDRIVER_PATH'))
# bot.get_internet_speed()
# print(f'Up: {bot.up} | Down: {bot.down}')
bot.tweet_at_provider()
