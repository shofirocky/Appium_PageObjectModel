import time
from appium import webdriver
from selenium.webdriver.common.by import By


class TaskListPage:
    def __init__(self, driver):
        self.driver = driver

    def mark_task_complete(self):
        complete_button = self.driver.find_element(By.XPATH, '(//android.view.View[@content-desc="Mark as complete"])[2]')
        complete_button.click()
