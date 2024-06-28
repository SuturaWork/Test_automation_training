#Task5: Password reset
#Description: Write a website login password reset function

Feature: Webpage password reset

    Scenario: Successful password reset
        Given the website login page is opened
        And the "Forgotten password?" button is clicked
        When valid email is entered
        | field  | value                 |
        | email  | test_email@gmail.com  |
        And "Send" button is clicked
        Then email sent message is displayed

    Scenario: Unsuccessful password reset with invalid email
        Given the website login page is opened
        And the "Forgotten password?" button is clicked
        When invalid email is entered
        | field  | value                 |
        | email  | test_email&gmail.com  |
        And "Send" button is clicked
        Then email sent message is not displayed
        And error message is displayed