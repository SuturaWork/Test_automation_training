#Task7: Profile update
#Description: Write a website profile update function

Feature: Profile update

Background:
    Given the website is opened
    And the user is logged in successfully
    And the "Profile" button is clicked

    Scenario: Successful profile update
        Given the user profile page is opened
        When valid data is entered
        | field       | value            |
        | First Name  | Dora             |
        | Last Name   | Dodo             |
        | Email       | xydodo@gmail.com |
        And "Save" button is clicked
        Then the successful update message is displayed

    Scenario: Unsuccessful profile update with invalid data
        Given the user profile page is opened
        When invalid data is entered
        | field       | value            |
        | First Name  | &@%Dor           |
        | Last Name   |                  |
        | Email       | @xydodo&gmailcom |
        And "Save" button is clicked
        Then the successful update message is not displayed
        And error message is displayed
        
