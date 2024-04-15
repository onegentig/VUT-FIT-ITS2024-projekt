# Prostředí pro ITS testy v Behave+Selenium+Python
#
# @author: onegen (xkrame00)
# @date: 2024-04-15
#

from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_scenario(context: Context, feature):
    # Chrome driver
    # context.driver = webdriver.Chrome()
    context.driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
    )

    # Doporučené čekání na DOM elementy
    context.driver.implicitly_wait(15)

    # Další props
    context.base_url = "http://opencart:8080"


def after_scenario(context, feature):
    # Zavřít a vyčistit testovací prohlížeč
    context.driver.quit()
    context.driver = None
