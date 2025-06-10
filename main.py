from datetime import datetime, timedelta
import random as rand
import re

def get_days_from_today(date_str: str, today: datetime = datetime.now()) -> int:
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
    if not isinstance(today, datetime):
        raise ValueError("Today must be a datetime object")
    
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("String must be in 'YYYY-MM-DD' format")

    return int((today.replace(hour=0, minute=0, second=0, microsecond=0) - date).days)

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

def normalize_phone(phone_number: str) -> str:
    """Normalizes a phone number to a standard format.
    Args:
        phone_number (str): The phone number to normalize.
    Returns:
        str: The normalized phone number in the format '+380XXXXXXXXX'.
    Examples:
        >>> normalize_phone("    +38(050)123-32-34")
        '+380501233234'
    """

    if not isinstance(phone_number, str):
        raise ValueError("Input must be a string")
    if not phone_number.strip():
        raise ValueError("Input cannot be empty")

    country_code = "+380"
    digits = ''.join(re.findall(r'\d+', phone_number))

    if not digits:
        raise ValueError("Input must contain digits")
    
    res = country_code + digits.lstrip(country_code)

    return res

def get_upcoming_birthdays(users: list, today: datetime = datetime.now()) -> list:
    """Finds upcoming birthdays within the next 7 days from today.
    Args:
        users (list): A list of dictionaries with user information, each containing 'name' and 'birthday' keys.
        today (datetime): The current date to compare against. Defaults to the current date and time.
    Returns:
        list: A list of dictionaries with names and congratulation dates of users whose birthdays are within the next 7 days.
    Raises:
        ValueError: If the input is not a list of dictionaries with 'name' and 'birthday' keys, or if the birthday format is incorrect.
    Examples:
        >>> users = [{"name": "John Doe", "birthday": "1985.01.23"}, {"name": "Jane Smith", "birthday": "1990.01.27"}]
        >>> get_upcoming_birthdays(users, datetime(1985, 1, 20))
        [{'name': 'John Doe', 'congratulation_date': '1985.01.23'}]
    """

    if not isinstance(users, list) or len(users) == 0:
        raise ValueError("Input must be a list of dictionaries with 'name' and 'birthday' keys")
    if not isinstance(today, datetime):
        raise ValueError("Today must be a datetime object")
    
    for user in users:
        if not isinstance(user, dict) or 'name' not in user or 'birthday' not in user:
            raise ValueError("Each user must be a dictionary with 'name' and 'birthday' keys")

    upcoming_date = today.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=7)

    upcoming_birthdays = []
    
    for user in users:
        try:
            days_diff = (upcoming_date - datetime.strptime(user['birthday'], "%Y.%m.%d")).days
        except ValueError:
            raise ValueError("Birthday must be in 'YYYY.MM.DD' format")
        
        if 0 <= days_diff <= 7:
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': user['birthday']})

    return upcoming_birthdays

today = datetime.strptime("2025-10-11", "%Y-%m-%d")

d = get_days_from_today("2025-10-6", today) 