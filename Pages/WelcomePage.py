import time
from appium import webdriver
from selenium.webdriver.common.by import By



class WelcomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_get_started_button(self):
        get_started_button = self.driver.find_element(By.ID, "com.google.android.apps.tasks:id/welcome_get_started")
        get_started_button.click()
