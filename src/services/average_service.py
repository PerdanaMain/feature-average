def find_average_value(indicates: list) -> float:
    """
    Find the average value of a list of numbers.

    Args:
    indicates (list): List of numbers.

    Returns:
    float: The average value of the list.
    """

    average = sum(indicates) / len(indicates)
    # average += 5
    return average
