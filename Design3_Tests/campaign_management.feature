Feature: Campaign creation

  Scenario: Campaign Manager creates a new campaign
    Given I am logged in as a Campaign Manager
    When I fill out the campaign creation form with valid data
    And I submit the form
    Then a new campaign should be listed on my dashboard
