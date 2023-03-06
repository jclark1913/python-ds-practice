def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # make a set/list of days of the week
    # return day based on index
    # Check for correct range
    # Subtract 1 from input

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday"]

    if day_of_week < 8 and day_of_week > 0:
        return weekdays[day_of_week - 1]

    return None


