from bubble_sort import bubble_sort
import pytest
from collections import Counter

def test_general_cases_and_immutability():
    messy = [5, 1, 4, 2, 8, 5, -3, 2.5]
    original = list(messy)
    assert bubble_sort(messy) == sorted(messy)
    # original list should remain unchanged
    assert messy == original

    # negatives and duplicates mixed in
    nums = [3, -1, 3, 0, -1, 2]
    assert bubble_sort(nums) == sorted(nums)

def test_edge_cases_and_early_exit():
    # empty
    assert bubble_sort([]) == []
    # single
    assert bubble_sort([42]) == [42]
    # already sorted triggers early exit
    sorted_list = list(range(10))
    assert bubble_sort(sorted_list) == sorted_list
    # reverse sorted 
    rev = list(range(9, -1, -1))
    assert bubble_sort(rev) == sorted(rev)


def test_many_duplicates_and_negatives():
    # lots of repeats and negatives also verify element counts are preserved
    data = [0, -1, -1, 2, 2, 2, -3, -3, -3, -3, 5, 5, 5]
    result = bubble_sort(data)
    assert result == sorted(data)
    assert Counter(result) == Counter(data)  # multiset preserved

def test_iterables_and_type_errors():
    # iterable input should return a list
    t = (3, 1, 2, 1)
    out = bubble_sort(t)
    assert isinstance(out, list)
    assert out == [1, 1, 2, 3]

    # Mixed incomparable types should raise error
    with pytest.raises(TypeError):
        bubble_sort([1, "a", 2])