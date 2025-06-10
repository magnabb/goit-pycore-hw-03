def test_get_days_from_today():
    from main import get_days_from_today
    from datetime import datetime, timedelta

    today = datetime.strptime("2025-10-11", "%Y-%m-%d")

    assert get_days_from_today("2025-10-6", today) == 5, "Expected 5 days for a date 5 days in the past"
    assert get_days_from_today("2025-10-11", today) == 0, "Expected 0 days for today's date"
    assert get_days_from_today("2025-10-14", today) == -3, "Expected -3 days for a date 3 days in the future"

    # Test with an invalid input (string)
    try:
        get_days_from_today("not a date")
        assert False, "Expected ValueError for invalid input"
    except ValueError:
        pass

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

def test_normalize_phone():
    from main import normalize_phone
 
    assert normalize_phone("    +38(050)123-32-34") == "+380501233234", "Failed to normalize phone with country code and formatting"
    assert normalize_phone("0503451234    ") == "+380503451234", "Failed to normalize phone with local format"
    assert normalize_phone("(050)8889900") == "+380508889900", "Failed to normalize phone with parentheses"
    assert normalize_phone("38050-111-22-22") == "+380501112222", "Failed to normalize phone with dashes"
    assert normalize_phone("38050 111 22 11   ") == "+380501112211", "Failed to normalize phone with spaces"

def test_get_upcoming_birthdays():
    from main import get_upcoming_birthdays
    from datetime import datetime

    assert all('name' in res and 'congratulation_date' in res and '2025.06.13' == res['congratulation_date'] for res in get_upcoming_birthdays([{"name": "Alice", "birthday": "2025.06.13"}], datetime.strptime("2025.06.11", "%Y.%m.%d"))), "upcoming_birthdays should handle single user"

test_get_days_from_today()
test_get_numbers_ticket()
test_normalize_phone()
test_get_upcoming_birthdays()
