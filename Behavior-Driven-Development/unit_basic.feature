Scenario: Add up to capacity
  Given there are 0 cucumbers
  And the basket capacity is 10
  When I add up to 15 cucumbers
  Then I should have 10 cucumbers in the basket
  And the basket should be full

Scenario: Remove up to available
  Given there are 4 cucumbers
  When I remove up to 10 cucumbers
  Then I should have 0 cucumbers in the basket
  And the basket should be empty

Scenario: Percentage full
  Given there are 5 cucumbers
  And the basket capacity is 20
  Then the basket should be 0.25 full

Scenario: Clear basket
  Given there are 7 cucumbers
  When I clear the basket
  Then I should have 0 cucumbers in the basket
