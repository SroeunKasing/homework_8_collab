def reverse_ascending(numbers):
    # result = []
    new = []
    previous_comparison = False
    for index, current_value in enumerate(numbers):
        previous_index = index - 1
        previous_value = numbers[previous_index]
        
        if previous_index >= 0:
            if 
            if current_value > previous_value and not previous_comparison:
                new.append(previous_index)
                previous_comparison = True
                print(new, previous_comparison)
            else: 
                new.append(previous_index)
                previous_comparison = False
                numbers = numbers[new[0]:new[-1]].reverse()
                print(numbers)
                new.clear()
    return numbers


print(reverse_ascending([1, 2, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 9, 10, 15]))
