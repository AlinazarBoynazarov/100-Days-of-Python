# speed of an internet provider: 74.7 Mbps
# 150Mbps download, 10Mbps upload.


from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys


# load environment variables from .env file
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()


class InternetSpeedTwitterBot:
    # . In the init() method, create the Selenium driver and 2 other properties down and up .
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.down = 0
        self.up = 0

    # Create two methods - get_internet_speed() and tweet_at_provider() .
    def get_internet_speed(self):
        #     self.driver.get('https://www.speedtest.net')
        #     time.sleep(3)
        #     go_button = self.driver.find_element(
        #         By.CSS_SELECTOR, '.start-button a').click()
        #     time.sleep(60)

        #     close_btn = self.driver.find_element(
        #         By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a').click()

        #     time.sleep(5)

        #     self.up = self.driver.find_element(By.XPATH,
        #                                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        #     self.down = self.driver.find_element_by_xpath(
        #         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.up = 228.08
        self.down = 210.54

        print(self.up)
        print(self.down)

    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(os.getenv('TWITTER_EMAIL'))
        # password = self.driver.find_element(By.XPATH,
        #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        # email.send_keys(os.getenv('TWITTER_EMAIL'))
        # password.send_keys(os.getenv('TWITTER_PASSWORD'))
        # time.sleep(2)
        # password.send_keys(Keys.ENTER)

        # time.sleep(5)
        # tweet_compose = self.driver.find_element_by_xpath(
        #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        # tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {os.getenv('PROMISED_DOWN')}down/{os.getenv('PROMISED_UP')}up?"
        # tweet_compose.send_keys(tweet)
        # time.sleep(3)

        # tweet_button = self.driver.find_element_by_xpath(
        #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        # tweet_button.click()

        # time.sleep(2)
        # self.driver.quit()


# Outside of the class, initialise the object and call the two methods in order. Where you first get the internet speed and then tweet at the provider.
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
