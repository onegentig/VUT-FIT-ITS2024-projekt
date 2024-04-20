# @author: onegen (xkrame00)
# @date: 2024-04-06
#

Feature: Searching
    As a customer
    I want to search available products
    So I can find the product I want to buy

    Background:
        Given user is on a page with a search bar

    # Coverage matrix col.: 1
    Scenario: Search for existing product
        Given store sells products with "mac" in their name
        When user searches for "mac"
        Then products with "mac" in their name are shown

    # Coverage matrix col.: 2
    Scenario: Search for non-existing product
        Given store does not sell products with "spaghetti" in their name
        When user searches for "spaghetti"
        Then no products are shown
