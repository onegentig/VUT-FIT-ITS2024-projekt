# Behave kroky k otestování správy zboží (goods_mgmt.feature)
#
# @author: onegen (xkrame00)
# @date: 2024-04-20
#

import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.utils import MyContext, await_popup_dismiss, get_admin


def find_product_in_table(context: MyContext, name: str):
    """
    Pomocná funkce na vyhledání produktu a vrácení řádku tabulky
    (vrátí None jestli neexistuje).
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


@given("admin is logged in")
def step_impl(context: MyContext):
    if "user_token=" in context.driver.current_url:
        pass

    context.driver.get(context.base_url + "/administration")
    curr_page = context.driver.current_url
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, "#form-login button").click()

    # Počkat a ověřit
    WebDriverWait(context.driver, 15).until(EC.url_changes(curr_page))
    assert "user_token=" in context.driver.current_url, "Admin login failed!"


@given("admin is on product management page")
def step_impl(context: MyContext):
    get_admin(
        context.driver,
        context.base_url + "/administration/index.php?route=catalog/product",
    )


@when('admin opens product "{name}"')
def step_impl(context: MyContext, name: str):
    product = find_product_in_table(context, name)
    assert product is not None, "Product not found!"
    p_btn = product.find_element(By.CSS_SELECTOR, "td:nth-child(7) a")
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", p_btn
    )


@when('admin adds a new product with name "{name}"')
def step_impl(context: MyContext, name: str):
    get_admin(
        context.driver,
        context.base_url + "/administration/index.php?route=catalog/product.form",
    )

    # General tab
    context.driver.find_element(By.ID, "input-name-1").send_keys(name)  # Jméno
    context.driver.find_element(By.ID, "input-meta-title-1").send_keys(
        name.lower().replace(" ", "-")
    )  # URI

    # Data tab
    data_tab_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#form-product .nav-item:nth-child(2) a"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", data_tab_btn
    )
    context.driver.find_element(By.ID, "input-model").send_keys(name)  # Model

    # SEO tab
    seo_tab_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#form-product .nav-item:nth-child(11) a"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", seo_tab_btn
    )
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys(
        name.lower().replace(" ", "-")
    )

    # Potvrdit
    save_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#content button[type='submit']"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", save_btn
    )

    await_popup_dismiss(context.driver)


@when('admin removes the product "{name}"')
def step_impl(context: MyContext, name: str):
    product = find_product_in_table(context, name)
    assert product is not None, "Product not found!"

    # Zvolit produkt
    p_select = product.find_element(By.CSS_SELECTOR, "td:nth-child(1) input")
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", p_select
    )

    # Smazat zvolené
    remove_btn = context.driver.find_element(
        By.CSS_SELECTOR, ".page-header button:nth-child(4)"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", remove_btn
    )

    # Potvrdit alert
    WebDriverWait(context.driver, 15).until(EC.alert_is_present())
    alert = context.driver.switch_to.alert
    alert.accept()
    await_popup_dismiss(context.driver)


@when('admin renames the product to "{name}"')
def step_impl(context: MyContext, name: str):
    p_name_in = context.driver.find_element(By.ID, "input-name-1")
    p_name_in.clear()
    p_name_in.send_keys(name)

    save_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#content button[type='submit']"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", save_btn
    )

    await_popup_dismiss(context.driver)


@then('product "{name}" is present in the product list')
def step_impl(context: MyContext, name: str):
    assert find_product_in_table(context, name) is not None, "Product not found!"


@then('product "{name}" is not present in the product list')
def step_impl(context: MyContext, name: str):
    assert find_product_in_table(context, name) is None, "Product found!"
