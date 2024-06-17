#Task2: Product search
#Description: Write a website product search function

Feature: Webshop Product Search

  Scenario: Searching result available 
    Given the webshop is opened
    When valid search term is entered in search field
	And the search button is clicked
    Then the product result page is displayed
    And the search term is contained in product name

  Scenario: No result of searching
    Given the webshop is opened
    When invalid search term is entered in search field
	And the search button is clicked
    Then the product result page is displayed
    And "Not found" message is displayed