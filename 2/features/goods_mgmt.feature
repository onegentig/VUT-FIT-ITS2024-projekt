# @author: onegen (xkrame00)
# @date: 2024-04-07
#        2024-04-20
#

Feature: Goods Management
     As a store admin
     I want to be able to manage products in the store
     So that I can keep the store up to date with sold goods

     Background:
          Given admin is logged in

     # Coverage matrix col.: 12
     Scenario: Add new product
          Given admin is on product management page
          When admin adds a new product with name "Sennheiser HD 25"
          Then product "Sennheiser HD 25" is present in the product list

     # Coverage matrix col.: 13
     Scenario: Update product
          Given admin is on product management page
          When admin opens product "Product 8"
          When admin renames the product to "Product 9 Pro"
          Then product "Product 9 Pro" is present in the product list
          And product "Product 8" is not present in the product list

     # Coverage matrix col.: 14
     Scenario: Remove product
          Given admin is on product management page
          When admin removes the product "Sennheiser HD 25"
          Then product "Sennheiser HD 25" is not present in the product list
