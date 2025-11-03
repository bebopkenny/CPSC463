Feature: Cucumbers basket behavior

  Scenario: Add cucumbers
    Given there are 12 cucumbers
    When I add 5 cucumbers to the basket
    Then I should have 17 cucumbers in the basket

  Scenario: Remove cucumbers
    Given there are 10 cucumbers
    When I remove 3 cucumbers from the basket
    Then I should have 7 cucumbers in the basket

Scenario: Clear the basket
  Given there are 7 cucumbers
  When I clear the basket
  Then I should have 0 cucumbers in the basket

Scenario: Basket reports empty
  Given there are 0 cucumbers
  Then the basket should be empty

Scenario: Add up to capacity
  Given there are 8 cucumbers
  And the basket capacity is 10
  When I add up to 5 cucumbers
  Then I should have 10 cucumbers in the basket

Scenario: Remove up to available
  Given there are 3 cucumbers
  When I remove up to 10 cucumbers
  Then I should have 0 cucumbers in the basket


