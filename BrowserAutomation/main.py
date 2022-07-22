# Author: Tharcisio Leone #
# Dataset: Performing browser automation with Selenium #

## Create an automation to download files in internet
# 0. Importing selenium and webdriver-manager
# 1. Importing Libraries
# 2. Open the homepage of World Bank
# 3. Find and download the dataset


# 0. Importing selenium and webdriver-manager
#Open Anaconda Prompt(anaconda3)
#pip install selenium
#pip install webdriver-manager

# 1. Importing Libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install())

# 2. Open the homepage of World Bank