# Prostředí pro ITS testy v Behave+Selenium+Python
#
# @author: onegen (xonege00)
# @date: 2024-04-15
#

from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_scenario(context: Context, feature):
    # Get Chrome driver
    # context.driver = webdriver.Chrome()
    context.driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
    )

    # Apply suggested implicit wait
    context.driver.implicitly_wait(15)

    # Other props
    context.base_url = "http://opencart:8080"


def after_scenario(context, feature):
    # Close and clear the testing browser
    context.driver.quit()
    context.driver = None
