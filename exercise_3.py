def remove_all_after(numbers, n):
    if n in numbers:
        numbers = numbers[0:numbers.index(n) + 1]
    return numbers

    # if n in numbers:
    #     del numbers[numbers.index(n) + 1:]
    # return numbers
