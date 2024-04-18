# @author: onegen (xkrame00)
# @date: 2024-04-06
#        2024-04-17
#


Feature: Checkout
     As a customer
     I want to be able to checkout my shopping cart
     So that I can pay for and recieve my items

     Background:
          Given user’s shopping cart is not empty

     # Coverage matrix col.: 9
     Scenario: Guest Checkout
          Given user is not logged in
          When user proceeds to checkout
          And user selects guest checkout
          And user fills out personal information
          And user selects a shipping option
          And user selects a payment method
          And user confirms the order
          Then order confirmation is displayed

     # Coverage matrix col.: 10
     Scenario: Registered User Checkout
          Given user is logged in
          And user has an address saved in address book
          When user proceeds to checkout
          And user selects a saved address
          And user selects a payment method
          And user confirms the order
          Then order confirmation is displayed
