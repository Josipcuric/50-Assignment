Feature: Assign contents to a parcel

  Scenario: Logistics Coordinator assigns content to a parcel
    Given I am logged in as a Logistics Coordinator
    And there is an existing parcel for Campaign Alpha
    And there are available content items in the database
    When I assign 10 flyers to the parcel
    Then the parcel should include 10 flyers
