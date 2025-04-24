Feature: Upload and approve content

  Scenario: Content Designer uploads new content
    Given I am logged in as a Content Designer
    When I upload a new banner file to Campaign Alpha
    Then the content should appear as "Pending Approval"

  Scenario: Campaign Manager approves content
    Given I am logged in as a Campaign Manager
    And there is pending content for Campaign Alpha
    When I approve the content
    Then the content status should change to "Approved"
