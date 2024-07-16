#Task4: Add to cart 
#Description: Write a webshop add to cart function

Feature: Webshop Add to Cart

Background:
    Given the webshop is opened
    And product name is entered in search field

  Scenario: Add a product to cart
    Given the product result page is displayed
    When "Add to cart" button is clicked
    Then the product is added to the cart
    And the correct number is displayed next to the cart

  Scenario: Add product with quantity to cart
    Given the product result page is displayed
    When the quantity of selected product is entered
    And "Add to cart" button is clicked
    Then the entered quantity of product is added to the cart
    And the correct number is displayed next to the cart