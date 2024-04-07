Feature: Searching
    As a customer
    I want to search available products
    So I can find the product I want to buy

    Background:
        Given the user is on a page with a search bar

    # Matrix col.: 1
    Scenario: Search for existing product
        Given store sells products with "mac" in their name
        When user searches for "mac"
        Then products with "mac" in their name are shown

    # Matrix col.: 2
    Scenario: Search for non-existing product
        Given store does not sell products with "spaghetti" in their name
        When user searches for "spaghetti"
        Then no products are shown
