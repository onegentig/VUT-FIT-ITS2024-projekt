Feature: Shopping Cart
    As a customer
    I want to manage products in my shopping cart
    So that I can review, add, and remove items before making a purchase

    # Matrix col.: 3
    Scenario: Add to shopping cart from homepage
        Given user is on the store’s homepage
        And homepage features "iPhone" on its homepage
        When user adds "iPhone" to their shopping cart
        Then shopping cart contains am "iPhone"

    # Matrix col.: 4
    Scenario: Add to shopping cart from category
        Given user is on "Monitor" category page
        And store sells "Samsung SyncMaster 941BW" in "Monitor" category
        When user adds "Samsung SyncMaster 941BW" to their shopping cart
        Then shopping cart contains a "Samsung SyncMaster 941BW"

    # Matrix col.: 5
    Scenario: Add to shopping cart from search
        Given user has searched for "galaxy tab"
        And search results contain "Samsung Galaxy Tab 10.1"
        When user adds "Samsung Galaxy Tab 10.1" to their shopping cart
        Then shopping cart contains a "Samsung Galaxy Tab 10.1"

    # Matrix col.: 6
    Scenario: Add multiple to shopping cart
        Given user is on "Palm Treo Pro" product page
        When user sets quantity to "3"
        And user adds "Palm Treo Pro" to their shopping cart
        Then shopping cart contains "3" "Palm Treo Pro"

    # Matrix col.: 7
    Scenario Outline: Change quantity in shopping cart
        Given user is on their shopping cart page
        And user has <start> "iPhone" in their shopping cart
        When user changes quantity of "iPhone" to <end>
        Then shopping cart contains <end> "iPhone"

        Examples:
            | start | end |
            | 1     | 2   |
            | 3     | 1   |
            | 2     | 5   |

    # Matrix col.: 8
    Scenario: Remove from shopping cart
        Given user has "iPhone" in their shopping cart
        When user removes "iPhone" from their shopping cart
        Then shopping cart does not contain "iPhone"
