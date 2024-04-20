# Zdílené utility/helper funkce pro ITS projekt 2.
#
# @author: onegen (xkrame00)
# @date: 2024-04-20
#

from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class MyContext(Context):
    driver: webdriver.Remote
    base_url: str


def toggle_cart(driver: webdriver.Remote):
    """
    Otevře/zavře košík.
    """
    cart = driver.find_element(By.CSS_SELECTOR, "#header-cart button")
    driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", cart)


def check_cart_empty(driver: webdriver.Remote) -> bool:
    toggle_cart(driver)

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
        toggle_cart(driver)
        return empty


def await_popup_show(driver: webdriver.Remote) -> WebElement:
    """
    Počká na zobrazení alert popup-u a vrátitjeho element.
    """
    WebDriverWait(driver, 15).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, "div#alert").text != ""
    )
    return driver.find_element(By.CSS_SELECTOR, "div#alert")


def await_popup_hide(driver: webdriver.Remote):
    """
    Po čká na skrytí alert popup-u.
    """
    WebDriverWait(driver, 15).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, "div#alert").text == ""
    )


def popup_close(driver: webdriver.Remote):
    """
    Zavře popup.
    """
    close_btn = driver.find_element(By.CSS_SELECTOR, "div#alert button.btn-close")
    driver.execute_script("arguments[0].click();", close_btn)


def await_popup_dismiss(driver: webdriver.Remote):
    """
    Počká na zobrazení alert popup-u a následně ho zavˇře.
    """
    await_popup_show(driver)
    popup_close(driver)
    await_popup_hide(driver)


def get_admin(driver: webdriver.Remote, url: str):
    """
    Zavolá driver.get() se zachováním user_tokenu.
    """
    user_token = driver.current_url.split("user_token=")[1]
    driver.get(url + "&user_token=" + user_token)


def find_elem_by_text(
    elem_list: list[WebElement], text: str, text_selector=None, strict=False
) -> WebElement | None:
    """
    Najde element v list-u WebElementů podle textu.
    """
    for elem in elem_list:
        elem_title = (
            elem.get_attribute("innerText")
            if text_selector is None
            else elem.find_element(By.CSS_SELECTOR, text_selector).get_attribute(
                "innerText"
            )
        )

        if strict:
            if text == elem_title:
                return elem
        else:
            if text in elem_title:
                return elem
    return None


def find_product_admin_table(context: MyContext, name: str):
    """
    Najde produkt v tabulce produktů v administraci.
    """
    get_admin(
        context.driver,
        context.base_url + "/administration/index.php?route=catalog/product",
    )

    # Filtr na vyhledání
    filter_btn = context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div[1]/div/div/button[1]'
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", filter_btn
    )
    p_filter_in = context.driver.find_element(
        By.CSS_SELECTOR, 'input[name="filter_name"]'
    )
    p_filter_in.clear()
    p_filter_in.send_keys(name)
    apply_btn = context.driver.find_element(By.ID, "button-filter")
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", apply_btn
    )

    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#form-product table tr"))
    )

    # Získat všechny produkty
    products = context.driver.find_elements(By.CSS_SELECTOR, "#form-product table tr")

    # Skontrolovat jestli bylo něco nalezeno
    if len(products) == 2 and "No results!" in products[1].get_attribute("innerText"):
        return None

    # Najít produkt
    product = None
    for p in products:
        title = p.find_element(By.CSS_SELECTOR, "td:nth-child(3)").get_attribute(
            "innerText"
        )
        if name in title:
            product = p
            break
    return product
