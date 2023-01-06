Feature: Github API validation

  Scenario: Session Management Check
    Given I have github credentials
    When I execute github repo API of git
    Then status code should be 200

