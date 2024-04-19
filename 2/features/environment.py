# Prostředí pro ITS testy v Behave+Selenium+Python
#
# @author: onegen (xkrame00)
# @date: 2024-04-15
#

import time
from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

OC_ROOT_URL = "http://opencart:8080"
WD_HUB_URL = "http://localhost:4444/wd/hub"


def await_driver(timeo=30) -> webdriver.Remote:
    """
    Počkat na dostupnost WD hubu.
    """
    hub_reached = False
    driver: webdriver.Remote
    attempts = 0
    max_attempts = timeo // 2
    while not hub_reached and attempts < max_attempts:
        try:
            driver = webdriver.Remote(
                command_executor=WD_HUB_URL,
                desired_capabilities=DesiredCapabilities.CHROME,
            )
            hub_reached = True
        except:
            attempts += 1
            time.sleep(2)
    assert hub_reached, "WebDriver hub is not reachable!"
    return driver


def await_website(driver: webdriver.Remote, timeo=30):
    """
    Počkat na dostupnost OpenCart stránky.
    """
    oc_reached = False
    attempts = 0
    max_attempts = timeo // 2
    while not oc_reached and attempts < max_attempts:
        try:
            driver.get(OC_ROOT_URL)
            oc_reached = True
        except:
            attempts += 1
            time.sleep(2)
    assert oc_reached, "OpenCart website is not reachable!"


def before_all(context: Context):
    # Chrome driver na lok. spuštění
    # context.driver = webdriver.Chrome()
    context.driver = await_driver()  # s čekáním – prevence ConnectionResetError

    # Doporučené čekání na DOM elementy
    context.driver.implicitly_wait(15)

    # Další props
    context.base_url = "http://opencart:8080"

    # Počkat na dostupnost stránky – prevence net::ERR_CONNECTION_REFUSED
    await_website(context.driver)


def after_all(context):
    # Zavřít a vyčistit testovací prohlížeč
    context.driver.quit()
    context.driver = None
