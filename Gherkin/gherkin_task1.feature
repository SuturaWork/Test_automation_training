#Task1: Login
#Description: Write a website login function

Feature: Website Login

  Scenario: Successful login
    Given the website login page is opened
    When the valid username and password are entered
    And the login button is clicked
    Then the user is logged in successfully

  Scenario: Unsuccessful login
    Given the website login page is opened
    When the valid username and password are entered
    And the login button is clicked
    Then the user is not logged
    And and error message is displayed