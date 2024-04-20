# @author: onegen (xkrame00)
# @date: 2019-04-07

Feature: Stock Management
     As a store admin
     I want to be able to manage stock of products
     So I can inform customers about product availability and order products from suppliers when needed

     Background:
          Given admin is logged in
          And admin is on product management page

     # Coverage matrix col.: 15
     Scenario Outline: Change stock of product
          Given product "<product>" has amount <start> in stock
          When admin opens product "<product>"
          And admin changes stock of the product to <end>
          Then product "<product>" has amount <end> in stock

          Examples:
               | product      | start |  end  |
               | Canon EOS 5D | 7     | 10    |
               | HP LP3065    | 1000  | 10    |
               | iPod Nano    | 994   | 1000  |

     # Coverage matrix col.: 16
     Scenario: Sell-out product
          Given product "Canon EOS 5D" has non-zero amount in stock
          When admin opens product "Canon EOS 5D"
          And admin changes stock of the product to 0
          Then product "Canon EOS 5D" is sold out
