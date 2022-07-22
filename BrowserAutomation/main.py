# Author: Tharcisio Leone #
# Dataset: Performing browser automation with Selenium #

## Create an automation to download files in internet
# 0. Import selenium and webdriver-manager
# 1. Import Libraries
# 2. Install updated version o Chrome Driver
# 3. Open the homepage of World Bank
# 4. Find and download the dataset


# 0. Import selenium and webdriver-manager
#Open Anaconda Prompt(anaconda3)
#pip install selenium
#pip install webdriver-manager


# 1. Import Libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# 2. Install updated version o Chrome Driver
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


# 3. Open the homepage of World Bank
browser.get('https://data.worldbank.org/indicator/SP.POP.TOTL')


# 4. Find and download the dataset
browser.find_element('xpath', '/html/body/div/div/div/div/div[3]/article/aside/div/div[2]/div/p/a[1]').click()