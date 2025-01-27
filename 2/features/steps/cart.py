# Behave kroky k otestovaní košíku (cart.feature)
#
# @author: onegen (xkrame00)
# @date: 2024-04-16
#

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from lib.utils import MyContext, await_popup_dismiss, find_elem_by_text, toggle_cart


@given("user is on the store’s homepage")
def step_impl(context: MyContext):
    context.driver.get(context.base_url)


@given('store sells "{product_name}" in "{category}" category')
def step_impl(context: MyContext, product_name: str, category: str):
    pass  # předpokládejme že platí


@given("user is on their shopping cart page")
def step_impl(context: MyContext):
    context.driver.get(context.base_url + "?route=checkout/cart")


@given('user has searched for "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    # Použít kroky v search.py
    context.execute_steps(
        f"""
        Given user is on the store’s homepage
        When user searches for "{product_name}"
        """
    )


@given('user is on "Monitor" category page')
def step_impl(context: MyContext):
    context.driver.get(context.base_url + "/catalog/component/monitor")


@given('user is on "Palm Treo Pro" product page')
def step_impl(context: MyContext):
    context.driver.get(context.base_url + "/product/palm-treo-pro")


@given('search results contain "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    # Kontrola zda se zobrazily nějaké produkty
    product_list = context.driver.find_element(
        By.CSS_SELECTOR, "#product-search #content #product-list"
    )
    assert product_list is not None, "No products found!"

    # Najít produkt
    product_titles = product_list.find_elements(By.CSS_SELECTOR, ".description h4")
    product = find_elem_by_text(product_titles, product_name, strict=True)
    assert product is not None, "No product found!"


@given('user has "{product_name}" in their shopping cart')
def step_impl(context: MyContext, product_name: str):
    toggle_cart(context.driver)

    # Najít produkt
    cart_products = context.driver.find_element(
        By.CSS_SELECTOR, "#header-cart ul table"
    ).find_elements(By.CSS_SELECTOR, "tbody tr")
    product = find_elem_by_text(
        cart_products, product_name, text_selector="td:nth-child(2)"
    )
    assert product is not None, "Product not found in cart!"

    toggle_cart(context.driver)


@given('user has {quantity:d} "{product_name}" in their shopping cart')
def step_impl(context: MyContext, quantity: int, product_name: str):
    toggle_cart(context.driver)

    # Najít produkt
    cart_products = context.driver.find_element(
        By.CSS_SELECTOR, "#header-cart ul table"
    ).find_elements(By.CSS_SELECTOR, "tbody tr")
    product = find_elem_by_text(
        cart_products, product_name, text_selector="td:nth-child(2)"
    )
    assert product is not None, "Product not found in cart!"

    # Zkontrolovat množství
    qty_elm = product.find_element(By.CSS_SELECTOR, "td:nth-child(3)")
    qty = int(qty_elm.get_attribute("innerText").replace("x", ""))
    print(f"qty: {qty}, quantity: {quantity}")
    assert qty == quantity, "Product quantity does not match!"

    toggle_cart(context.driver)


@given('homepage features "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    # Najít featured sekci
    feat_row = context.driver.find_element(
        By.XPATH, "/html/body/main/div[2]/div/div/div[2]"
    )
    assert feat_row is not None, "Featured row not found!"
    feat_titles = feat_row.find_elements(By.CSS_SELECTOR, ".description h4")

    # Najít produkt
    product = find_elem_by_text(feat_titles, product_name)
    assert product is not None, "No featured product found!"


@when("user sets current item’s quantity to {quantity:d}")
def step_impl(context: MyContext, quantity: int):
    qty_input = context.driver.find_element(By.CSS_SELECTOR, "input[name='quantity']")
    qty_input.click()
    qty_input.clear()
    qty_input.send_keys(str(quantity))


@when("user adds current item to their shopping cart")
def step_impl(context: MyContext):
    context.driver.find_element(
        By.CSS_SELECTOR, "#form-product button#button-cart"
    ).click()

    await_popup_dismiss(context.driver)


@when('user adds "{product_name}" to their shopping cart')
def step_impl(context: MyContext, product_name: str):
    products = context.driver.find_elements(By.CSS_SELECTOR, ".product-thumb .content")

    # Najít produkt
    product = find_elem_by_text(products, product_name, text_selector=".description h4")
    assert product is not None, "Product not found!"

    # Přidat do košíku
    product_btn = product.find_element(
        By.CSS_SELECTOR, ".button-group button:nth-child(1)"
    )
    context.driver.execute_script("arguments[0].click();", product_btn)

    await_popup_dismiss(context.driver)


@when('user changes quantity of "{product_name}" to {quantity:d}')
def step_impl(context: MyContext, product_name: str, quantity: int):
    # Najít produkt
    cart_products = context.driver.find_element(
        By.CSS_SELECTOR, "#shopping-cart table"
    ).find_elements(By.CSS_SELECTOR, "tbody tr")
    product = find_elem_by_text(
        cart_products, product_name, text_selector="td:nth-child(2) a"
    )
    assert product is not None, "Product not found in cart!"

    # Změnit množství
    qty_input = product.find_element(
        By.CSS_SELECTOR, "td:nth-child(4) input:nth-child(1)"
    )
    qty_input.click()
    qty_input.clear()
    qty_input.send_keys(str(quantity))
    qty_input.send_keys(Keys.ENTER)

    await_popup_dismiss(context.driver)


@when('user removes "{product_name}" from their shopping cart')
def step_impl(context: MyContext, product_name: str):
    toggle_cart(context.driver)

    # Najít produkt
    cart_products = context.driver.find_element(
        By.CSS_SELECTOR, "#header-cart ul table"
    ).find_elements(By.CSS_SELECTOR, "tbody tr")
    product = find_elem_by_text(
        cart_products, product_name, text_selector="td:nth-child(2)"
    )
    assert product is not None, "Product not found in cart!"

    # Odebrat produkt
    product.find_element(By.CSS_SELECTOR, ".text-end button").click()

    await_popup_dismiss(context.driver)


@then('shopping cart contains "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    context.execute_steps(
        f"""
        Given user has "{product_name}" in their shopping cart
        """
    )


@then('shopping cart does not contain "{product_name}"')
def step_impl(context: MyContext, product_name: str):
    toggle_cart(context.driver)

    # Najít produkt
    cart_products = context.driver.find_element(
        By.CSS_SELECTOR, "#header-cart ul table"
    ).find_elements(By.CSS_SELECTOR, "tbody tr > td:nth-child(2)")
    product = find_elem_by_text(cart_products, product_name)
    assert product is None, "Product found in cart!"

    toggle_cart(context.driver)


@then('shopping cart contains {quantity:d} "{product_name}"')
def step_impl(context: MyContext, quantity: int, product_name: str):
    context.execute_steps(
        f"""
        Given user has {quantity} "{product_name}" in their shopping cart
        """
    )
