Feature: Goods Management
     As a store admin
     I want to be able to manage products in the store
     So that I can keep the store up to date with sold goods

     Background:
          Given the admin is logged in

     # Matrix col.: 12
     Scenario: Add new product
          Given the admin is on the product management page
          When the admin adds a new product "Sennheiser HD 25" with all the required details
          Then the product "Sennheiser HD 25" should be added to the store

     # Matrix col.: 13
     Scenario: Update product
          Given the admin is on the product management page
          When the admin changes some information about the product "Apple Cinema 30"
          Then the product "Apple Cinema 30" should be updated in the store

     # Matrix col.: 14
     Scenario: Remove product
          Given the admin is on the product management page
          When the admin removes the product "iPod Classic"
          Then the product "iPod Classic" should be removed from the store
