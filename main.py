from datetime import datetime
import random as rand

def get_days_from_today(date_str: str) -> int:
    """Calculates the number of days from today to a given date.
    Args:
        date_str (str): A string representing a date in 'YYYY-MM-DD' format.
    Returns:
        int: The number of days from today to the given date. If the date is in the future, returns a negative number.
    Raises:
        ValueError: If the input string is not in the correct format or is not a string.
    Examples:
        >>> get_days_from_today("2025-06-05")
        0
        >>> get_days_from_today("2025-06-06")
        -1
        >>> get_days_from_today("2025-06-04")
        1
        >>> get_days_from_today("2025-06-32")
        Traceback (most recent call last):
            ...ValueError: String must be in 'YYYY-MM-DD' format
    """
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("String must be in 'YYYY-MM-DD' format")

    return int((datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - date).days)

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Generates a list of unique random integers within a specified range.
    Args:
        min (int): The minimum value of the range (inclusive).
        max (int): The maximum value of the range (inclusive).
        quantity (int): The number of unique integers to generate.
    Returns:
        list: A list of unique random integers, or an empty list if the input is invalid.
    Examples:
        >>> get_numbers_ticket(1, 3, 3)
        [1, 2, 3]
        >>> get_numbers_ticket(1, 3, 4)
        []
        >>> get_numbers_ticket(3, 1, 2)
        []
        >>> get_numbers_ticket(1, 1000, 5)
        [2, 10, 42, 69, 333]
        >>> get_numbers_ticket(1, 1000, 0)
        []
        >>> get_numbers_ticket(1.0, 10, 1)
        []
    """

    # Validate input parameters
    if (not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int)) \
        or (min >= max) \
        or (quantity <= 0) \
        or (min < 1 or min > 1000) \
        or (max < 1 or max > 1000) \
        or (max < 1 or max > 1000) \
        or (quantity > (max - min + 1)):
        return []

    try:
        res = rand.sample(range(min, max + 1), k=quantity)
        res.sort()
        return res
    except Exception:
        # Ensure we dont raise any exceptions
        return []

def normalize_phone(phone_number):
    pass