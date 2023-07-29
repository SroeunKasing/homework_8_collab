def replace_last(numbers):
    """list only"""
    if len(numbers) <= 1:
        return numbers
    numbers.insert(0, numbers.pop())
    return numbers
