import time
from appium import webdriver
from selenium.webdriver.common.by import By


class TaskPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_task_button(self):
        add_task_button = self.driver.find_element(By.ID, "com.google.android.apps.tasks:id/tasks_fab")
        add_task_button.click()

    def enter_task_title(self, title):
        task_title_field = self.driver.find_element(By.ID, "com.google.android.apps.tasks:id/add_task_title")
        task_title_field.send_keys(title)

    def click_done_button(self):
        done_button = self.driver.find_element(By.ID, "com.google.android.apps.tasks:id/add_task_done")
        done_button.click()
