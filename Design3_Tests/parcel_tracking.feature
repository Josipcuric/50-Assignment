Feature: Track parcel delivery

  Scenario: Logistics Coordinator updates delivery status
    Given I am logged in as a Logistics Coordinator
    And a parcel is marked as "In Transit"
    When I update the status to "Delivered"
    Then the parcel should show as "Delivered" in the system
