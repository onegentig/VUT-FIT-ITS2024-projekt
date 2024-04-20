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
from lib.utils import (
    MyContext,
    await_popup_dismiss,
    find_product_admin_table,
    get_admin,
)


@given("admin is logged in")
def step_impl(context: MyContext):
    if "user_token=" in context.driver.current_url:
        pass

    # Navigace na `/administration` často selže, alespoň tomu dám několik pokusů
    attempts = 0
    max_attempts = 3
    curr_page = context.driver.current_url
    while attempts < max_attempts:
        if attempts % 2 == 0:
            context.driver.get(context.base_url + "/administration")
        else:
            context.driver.get(context.base_url + "/administration/index.php")

        curr_page = context.driver.current_url

        has_form = context.driver.execute_script(
            "return document.getElementById('input-username') !== null;"
        )

        if has_form:
            break
        attempts += 1
        time.sleep(1)

    assert (
        has_form
    ), "Navigation to admin login failed after 5 attempts (issue in report.pdf)"

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


@when('admin opens product "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    product = find_product_admin_table(context, product_name)
    assert product is not None, "Product not found!"
    p_btn = product.find_element(By.CSS_SELECTOR, "td:nth-child(7) a")
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", p_btn
    )


@when('admin adds a new product with name "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    get_admin(
        context.driver,
        context.base_url + "/administration/index.php?route=catalog/product.form",
    )

    # General tab
    context.driver.find_element(By.ID, "input-name-1").send_keys(product_name)  # Jméno
    context.driver.find_element(By.ID, "input-meta-title-1").send_keys(
        product_name.lower().replace(" ", "-")
    )  # URI

    # Data tab
    data_tab_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#form-product .nav-item:nth-child(2) a"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", data_tab_btn
    )
    context.driver.find_element(By.ID, "input-model").send_keys(product_name)  # Model

    # SEO tab
    seo_tab_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#form-product .nav-item:nth-child(11) a"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", seo_tab_btn
    )
    context.driver.find_element(By.ID, "input-keyword-0-1").send_keys(
        product_name.lower().replace(" ", "-")
    )

    # Potvrdit
    save_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#content button[type='submit']"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", save_btn
    )

    await_popup_dismiss(context.driver)


@when('admin removes the product "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    product = find_product_admin_table(context, product_name)
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


@when('admin renames the product to "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    p_name_in = context.driver.find_element(By.ID, "input-name-1")
    p_name_in.clear()
    p_name_in.send_keys(product_name)

    save_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#content button[type='submit']"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", save_btn
    )

    await_popup_dismiss(context.driver)


@then('product "{product_name}" is present in the product list')
def step_impl(context: MyContext, product_name: str):
    assert (
        find_product_admin_table(context, product_name) is not None
    ), "Product not found!"


@then('product "{product_name}" is not present in the product list')
def step_impl(context: MyContext, product_name: str):
    assert find_product_admin_table(context, product_name) is None, "Product found!"
