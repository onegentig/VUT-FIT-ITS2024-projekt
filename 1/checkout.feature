Feature: Checkout
     As a customer
     I want to be able to checkout my shopping cart
     So that I can pay for and recieve my items

     Background:
          Given the user’s shopping cart is not empty

     Scenario: Guest Checkout
          Given the user is not logged in
          When the user proceeds to checkout
          And the user fills out billing and personal information
          And the user fills out shipping information
          And user selects a payment method
          And the user confirms the order
          Then order confirmation should be displayed

     Scenario: Registered User Checkout
          Given the user is logged in
          And the user has an address saved in address book
          When the user proceeds to checkout
          And the user selects a saved address
          And user selects a payment method
          And the user confirms the order
          Then order confirmation should be displayed

     Scenario Outline: Shipping Cost
          Given the user is checking out with suntotal <subtotal>
          When user selects a shipping method that costs <shipping>
          Then the total cost should be <total>

          Examples:
               | cart    | shipping | total    |
               | 123.20  | 8.00     | 131.20   |
               | 200.00  | 5.00     | 205.00   |
