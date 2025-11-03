from pytest_bdd import given, when, then, parsers
from cucumbers import CucumberBasket

# If you already have a "there are {start:d} cucumbers" step, reuse it.
@given(parsers.parse("the basket capacity is {cap:d}"))
def set_capacity(basket, cap):
    basket.max_count = cap

@when(parsers.parse("I add up to {n:d} cucumbers"))
def when_add_up_to(basket, n):
    basket.add_up_to(n)

@when(parsers.parse("I remove up to {n:d} cucumbers"))
def when_remove_up_to(basket, n):
    basket.remove_up_to(n)

@when("I clear the basket")
def when_clear(basket):
    basket.clear()

@then("the basket should be empty")
def then_empty(basket):
    assert basket.is_empty()

@then("the basket should be full")
def then_full(basket):
    assert basket.is_full()

@then(parsers.parse("the basket should be {p:float} full"))
def then_percent(basket, p):
    assert abs(basket.percentage_full() - p) < 1e-9
