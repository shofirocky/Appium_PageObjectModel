import time
from appium import webdriver
from selenium.webdriver.common.by import By
from Pages.WelcomePage import WelcomePage
from Pages.TaskPage import TaskPage
from Pages.TaskListPage import TaskListPage

# Set up desired capabilities
desired_caps = {}
desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
desired_caps['appPackage'] = 'com.google.android.apps.tasks'
desired_caps['appActivity'] = '.ui.TaskListsActivity'
desired_caps['automationName'] = 'UiAutomator2'

# Start the Appium driver
driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)
driver.implicitly_wait(5)

# Instantiate page objects
welcome_page = WelcomePage(driver)
task_page = TaskPage(driver)
task_list_page = TaskListPage(driver)

# Perform actions using page objects
welcome_page.click_get_started_button()
task_page.click_add_task_button()
task_page.enter_task_title("tasklist")
task_page.click_done_button()
task_list_page.mark_task_complete()

# Close the driver after test
time.sleep(2)
driver.quit()
