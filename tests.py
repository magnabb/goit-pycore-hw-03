def test_get_numbers_ticket():
    from main import get_numbers_ticket

    result = get_numbers_ticket(1, 3, 3)
    assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"
    assert get_numbers_ticket(1, 3, 4) == [], "Expected empty list for quantity > range"
    assert get_numbers_ticket(3, 1, 2) == [], "Expected empty list for min > max"

    result = get_numbers_ticket(1, 49, 6)
    assert len(result) == 6 and all(1 <= num <= 49 for num in result), "Expected 6 unique numbers in range [1, 49]"
    
    assert get_numbers_ticket(1, 1000, 0) == [], "Expected empty list for zero quantity"
    assert get_numbers_ticket(1.0, 10, 1) == [], "Expected empty list for non-integer min value"

test_get_numbers_ticket()