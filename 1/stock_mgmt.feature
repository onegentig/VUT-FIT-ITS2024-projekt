Feature: Stock Management
     As a store admin
     I want to be able to manage stock of products
     So I can inform customers about product availability and order products from suppliers when needed

     Background:
          Given the admin is logged in

     # Matrix col.: 15
     Scenario Outline: Change stock of product
          Given there is a product with name <product> with <start>
          When the admin changes stock of the product to <end>
          Then the stock of the product should be <end>

          Examples:
               | product      | start |  end  |
               | Canon EOS 5D | 7     | 10    |
               | HP LP3065    | 1000  | 10    |
               | iPod Nano    | 994   | 1000  |

     # Matrix col.: 16
     Scenario: Sell-out product
          Given there is a product with name "Canon EOS 5D" with non-zero stock
          When the admin changes stock of the product to 0
          Then the product appears as out of stock
