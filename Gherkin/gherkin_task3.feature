#Task3: Registration
#Description: Write a website registration function

Feature: Website Registration

  Scenario: Successful registration
    Given the website registration page is opened
    When valid registration data is entered
    | field       | value            |
    | First Name  | Dora             |
    | Last Name   | Szeli            |
    | Email       | xy@gmail.com     |
    | Password    | 1234             | 
	  And the registration button is clicked
    Then the welcome page is displayed

  Scenario: Unsuccessful registration
    Given the website registration page is opened
    When invalid registration data is entered
    | field       | value            |
    | First Name  | Dora             |
    | Last Name   |                  |
    | Email       | xy@gmail         |
    | Password    | 1234             | 
    And the registration button is clicked
    Then the registration page is remained
    And error message is displayed