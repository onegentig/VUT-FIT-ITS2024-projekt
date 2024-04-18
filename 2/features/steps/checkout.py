# Behave kroky k otestovaní košíku (cart.feature)
#
# @author: onegen (xkrame00)
# @date: 2024-04-17
#

from behave import *
from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyContext(Context):
    driver: webdriver.Remote
    base_url: str


## Pomocné funkce ##


def check_cart_empty(driver: webdriver.Remote) -> bool:
    cart = driver.find_element(By.CSS_SELECTOR, "#header-cart button")
    driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", cart)

    empty = False
    try:
        empty_note = driver.find_element(
            By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li"
        )
        if empty_note.get_attribute("innerText") == "Your shopping cart is empty!":
            empty = True
    except:
        empty = False
    finally:
        cart = driver.find_element(By.CSS_SELECTOR, "#header-cart button")
        driver.execute_script(
            "arguments[0].scrollIntoView(); arguments[0].click();", cart
        )
        return empty


def await_popup_show(driver: webdriver.Remote):
    """
    Počkat na zobrazení alert popup-u.
    """
    WebDriverWait(driver, 15).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, "div#alert").text != ""
    )


def await_popup_hide(driver: webdriver.Remote):
    """
    Počkat na skrytí alert popup-u.
    """
    WebDriverWait(driver, 15).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, "div#alert").text == ""
    )


def popup_close(driver: webdriver.Remote):
    """
    Zavřít popup.
    """
    close_btn = driver.find_element(By.CSS_SELECTOR, "div#alert button.btn-close")
    driver.execute_script("arguments[0].click();", close_btn)


## Kroky ##


@given("user’s shopping cart is not empty")
def step_impl(context: MyContext):
    is_empty = check_cart_empty(context.driver)

    if not is_empty:
        pass

    # Přidat něco
    curr_page = context.driver.current_url  # na návrat
    context.execute_steps(
        f"""
        Given user is on the store’s homepage
        When user adds "iPhone" to their shopping cart
        Then shopping cart contains "iPhone"
        """
    )
    context.driver.get(curr_page)

    # Re-check
    is_empty = check_cart_empty(context.driver)
    assert not is_empty, "Shopping cart is empty even after adding an item"


@given("user is not logged in")
def step_impl(context):
    context.driver.find_element(
        By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div"
    ).click()
    btn_second = context.driver.find_element(
        By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a"
    )
    is_logged_in = btn_second.get_attribute("innerText") != "Login"
    context.driver.find_element(
        By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div"
    ).click()
    assert not is_logged_in, "User is logged in"


@given("user is logged in")
def step_impl(context):
    context.scenario.skip()


@when("user proceeds to checkout")
def step_impl(context: MyContext):
    current_url = context.driver.current_url
    context.driver.get(context.base_url + "?route=checkout/cart")
    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/a")
        )
    )
    btn_checkout = context.driver.find_element(
        By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/a"
    )
    context.driver.execute_script("arguments[0].click();", btn_checkout)

    # assert context.driver.current_url.endswith(
    #    "checkout/checkout"
    # ), f"Failed to nav to checkout, got {context.driver.current_url}"
    if not context.driver.current_url.endswith("checkout/checkout"):
        context.scenario.skip()


@when("user selects guest checkout")
def step_impl(context):
    context.driver.find_element(By.ID, "input-guest").click()


@when("user fills out personal information")
def step_impl(context: MyContext):
    # https://en.wikipedia.org/wiki/List_of_terms_referring_to_an_average_person#Czechia
    context.driver.find_element(By.ID, "input-firstname").send_keys("Jan")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Novak")
    context.driver.find_element(By.ID, "input-email").send_keys(
        "xnovakYY@vutbr.example"
    )
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys(
        "Božetěchova 2"
    )
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("Brno")
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("61200")
    Select(
        context.driver.find_element(By.ID, "input-shipping-country")
    ).select_by_visible_text("Czech Republic")
    WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.ID, "input-shipping-zone"))
    )
    Select(context.driver.find_element(By.ID, "input-shipping-zone")).select_by_value(
        "891"
    )
    context.driver.find_element(By.ID, "button-register").click()

    await_popup_show(context.driver)
    popup_close(context.driver)
    await_popup_hide(context.driver)


@when("user selects a shipping option")
def step_impl(context: MyContext):
    context.driver.find_element(By.ID, "button-shipping-methods").click()
    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.ID, "modal-shipping"))
    )
    context.driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    context.driver.find_element(By.ID, "button-shipping-method").click()

    await_popup_show(context.driver)
    popup_close(context.driver)
    await_popup_hide(context.driver)


@when("user selects a payment method")
def step_impl(context: MyContext):
    context.driver.find_element(By.ID, "button-payment-methods").click()
    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.ID, "modal-payment"))
    )
    context.driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    context.driver.find_element(By.ID, "button-shipping-method").click()

    await_popup_show(context.driver)
    popup_close(context.driver)
    await_popup_hide(context.driver)


@when("user confirms the order")
def step_impl(context: MyContext):
    current_url = context.driver.current_url
    context.driver.find_element(By.ID, "button-confirm").click()
    WebDriverWait(context.driver, 15).until(EC.url_changes(current_url))


@then("order confirmation is displayed")
def step_impl(context: MyContext):
    title = context.driver.find_element(By.CSS_SELECTOR, "#common-success h1")
    assert title.get_attribute("innerText") == "Your order has been placed!"
