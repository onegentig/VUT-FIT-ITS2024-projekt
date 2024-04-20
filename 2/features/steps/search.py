# Behave kroky k otestování vyhledávání (search.feature)
#
# @author: onegen (xkrame00)
# @date: 2024-04-14
#

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib.utils import MyContext


@given("user is on a page with a search bar")
def step_impl(context: MyContext):
    # Rychlá kontrola searche, i tak většinou třeba přejít na homepage
    has_search = context.driver.execute_script(
        "return document.getElementById('search') !== null;"
    )

    if not has_search:
        context.execute_steps(
            """
            Given user is on the store’s homepage
            """
        )
        assert (
            context.driver.find_element(By.ID, "search") is not None
        ), "No search bar found even after homepage nav!"


@given('store sells products with "{keyword}" in their name')
def step_impl(context, keyword):
    pass  # předpokládejme že platí


@given('store does not sell products with "{keyword}" in their name')
def step_impl(context, keyword):
    pass  # předpokládejme že platí


@when('user searches for "{keyword}"')
def step_impl(context: MyContext, keyword: str):
    search = context.driver.find_element(By.CSS_SELECTOR, "#search input")
    search.click()
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)


@then('products with "{keyword}" in their name are shown')
def step_impl(context: MyContext, keyword: str):
    # Kontrola zda se zobrazily nějaké produkty
    search_content = context.driver.find_element(
        By.CSS_SELECTOR, "#product-search #content"
    )
    product_list = search_content.find_element(By.ID, "product-list")
    assert product_list is not None, "No products found!"

    # Kontrola zda produkty obsahují keyword
    product_titles = product_list.find_elements(By.CSS_SELECTOR, ".description h4")
    for title in product_titles:
        assert (
            keyword.lower() in title.get_attribute("innerText").lower()
        ), "Product without keyword found!"


@then("no products are shown")
def step_impl(context: MyContext):
    # Kontrola zda se zobrazily nějaké produkty
    search_content = context.driver.find_element(
        By.CSS_SELECTOR, "#product-search #content"
    )

    # Najít "not found" zprávu (rychlejší než ověření neexistence produktů)
    message = search_content.find_element(By.XPATH, "/html/body/main/div[2]/div/div/p")
    assert (
        message.text == "There is no product that matches the search criteria."
    ), "Products found! (none were supposed to be found)"
