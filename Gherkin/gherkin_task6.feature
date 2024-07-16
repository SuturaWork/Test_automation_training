#Task6: Product feedback
#Description: Write a product feedback function

Feature: Product feedback

Background:
    Given the webshop is opened
    And product name is entered in search field
    And product is selected on result page

    Scenario: Successful product feedback
        Given the product details page is displayed
        When scolled to "Feedback" section
        And 5 stars are clicked
        And "correct" text is entered in feedback field
        And "Send" button is clicked
        Then successful feedback message is displayed
        And the feedback is added to product

    Scenario: Unuccessful product feedback with empty field
        Given the product details page is displayed
        When scolled to "Feedback" section
        And 5 stars are clicked
        And no text is entered in feedback field
        And "Send" button is clicked
        Then text feedback is required message is displayed
        And the feedback is not added to product    