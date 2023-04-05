from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
import os

from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3527667247&f_AL=true&keywords=software%20engineer%20intern&refresh=true&sortBy=R")

time.sleep(1)

submit = driver.find_element(
    By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

time.sleep(1)

username.send_keys(os.getenv('LOG'))
password.send_keys(os.getenv('TSP'))

time.sleep(1)

submit = driver.find_element(
    By.XPATH, "//*[@id='organic-div']/form/div[3]/button").click()

time.sleep(1)

# pressing the easy apply button
easy_apply = driver.find_element(
    By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button").click()

time.sleep(1)

next_button1 = driver.find_element(
    By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button').click()

time.sleep(1)

next_button2 = driver.find_element(
    By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()

time.sleep(1)

next_button3 = driver.find_element(
    By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()

time.sleep(1)

next_button4 = driver.find_element(
    By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div/fieldset/div[1]").click()

time.sleep(1)

next_button5 = driver.find_element(
    By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div/fieldset/div[1]/label").click()

time.sleep(1)

next_button6 = driver.find_element(
    By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]").click()

time.sleep(1)

submit = driver.find_element(
    By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]").click()

time.sleep(10)
