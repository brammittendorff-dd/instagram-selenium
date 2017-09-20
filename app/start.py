"""
This is the startup module for this repository
"""

import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor=os.environ['URL_SELENIUM_HUB'], desired_capabilities=DesiredCapabilities.CHROME
)

driver.get(os.environ['URL_INSTAGRAM'] + "accounts/login/")

# Login
input_username = driver.find_element_by_name('username')
input_password = driver.find_element_by_name('password')
input_username.send_keys(os.environ['USERNAME'])
input_password.send_keys(os.environ['PASSWORD'])
input_password.submit()

# Page after login
wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.current_url == os.environ['URL_INSTAGRAM'])

# Take a screenshot
driver.save_screenshot("screenshot.png")