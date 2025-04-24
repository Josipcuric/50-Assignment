Feature: Generate campaign reports

  Scenario: Campaign Manager views a report
    Given I am logged in as a Campaign Manager
    When I select a campaign and generate a report
    Then I should see parcel counts and delivery statuses
