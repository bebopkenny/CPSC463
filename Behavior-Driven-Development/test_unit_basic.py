from pytest_bdd import scenarios, given, when, then, parsers
from cucumbers import CucumberBasket

scenarios("unit_basic.feature")

@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="basket")
def _(start):
    return CucumberBasket(start)

@when(parsers.parse("I add {added:d} cucumbers to the basket"))
def add_cucumbers(basket, added):
    basket.add(added)

@when(parsers.parse("I remove {removed:d} cucumbers from the basket"))
def remove_cucumbers(basket, removed):
    basket.remove(removed)

@then(parsers.parse("I should have {final:d} cucumbers in the basket"))
def should_have_cucumbers(basket, final):
    assert basket.count == final

@when(parsers.parse("I add {added:d} cucumbers to the basket"))
def add_cucumbers(basket, added):
    print(f"When: add {added}")
    basket.add(added)

from pytest_bdd import when

@when("I clear the basket")
def clear_basket(basket):
    basket.clear()

from pytest_bdd import then

@then("the basket should be empty")
def basket_should_be_empty(basket):
    assert basket.is_empty()

from pytest_bdd import given, when, parsers

@given(parsers.parse("the basket capacity is {cap:d}"))
def set_capacity(basket, cap):
    basket.max_count = cap

@when(parsers.parse("I add up to {n:d} cucumbers"))
def when_add_up_to(basket, n):
    actually_added = basket.add_up_to(n)
    print(f"add_up_to requested={n}, added={actually_added}")

from pytest_bdd import when, parsers

@when(parsers.parse("I remove up to {n:d} cucumbers"))
def when_remove_up_to(basket, n):
    removed = basket.remove_up_to(n)
    # Optional print for your video:
    print(f"remove_up_to requested={n}, removed={removed}")
