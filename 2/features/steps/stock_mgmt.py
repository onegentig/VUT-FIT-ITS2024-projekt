# Behave kroky k otestování správy zásoby zboží (stock_mgmt.feature)
#
# @author: onegen (xkrame00)
# @date: 2024-04-20
#

from behave import *
from selenium.webdriver.common.by import By
from lib.utils import (
    MyContext,
    await_popup_dismiss,
    find_product_admin_table,
)


@given('product "{product_name}" has amount {amount:d} in stock')
def step_impl(context: MyContext, product_name: str, amount: int):
    product = find_product_admin_table(context, product_name)
    assert product is not None, "Product not found!"

    stock_str = product.find_element(By.CSS_SELECTOR, "td:nth-child(6)")
    stock = int(stock_str.get_attribute("innerText"))
    assert stock == amount, f"Product stock amount is {stock}, expected {amount}!"


@given('product "{product_name}" has non-zero amount in stock')
def step_impl(context: MyContext, product_name: str):
    product = find_product_admin_table(context, product_name)
    assert product is not None, "Product was not found!"

    stock_str = product.find_element(By.CSS_SELECTOR, "td:nth-child(6)")
    stock = int(stock_str.get_attribute("innerText"))
    assert stock > 0, "Product stock amount is zero!"


@when("admin changes stock of the product to {amount:d}")
def step_impl(context: MyContext, amount: int):
    # Tab nav
    data_tab_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#form-product .nav-item:nth-child(2) a"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", data_tab_btn
    )

    # Nastavit
    stock_in = context.driver.find_element(By.ID, "input-quantity")
    stock_in.clear()
    stock_in.send_keys(amount)

    # Potvrdit
    save_btn = context.driver.find_element(
        By.CSS_SELECTOR, "#content button[type='submit']"
    )
    context.driver.execute_script(
        "arguments[0].scrollIntoView(); arguments[0].click();", save_btn
    )

    await_popup_dismiss(context.driver)


@then('product "{product_name}" has amount {amount:d} in stock')
def step_impl(context: MyContext, product_name: str, amount: int):
    context.execute_steps(
        f'Given product "{product_name}" has amount {amount} in stock'
    )


@then('product "{product_name}" is sold out')
def step_impl(context: MyContext, product_name: str):
    product = find_product_admin_table(context, product_name)
    context.execute_steps(f'Given product "{product_name}" has amount 0 in stock')
