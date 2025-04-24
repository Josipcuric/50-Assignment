Feature: Manage users

  Scenario: Admin creates a new user
    Given I am logged in as an Admin
    When I create a new user with the role "Logistics Coordinator"
    Then the user should appear in the system with the correct role
