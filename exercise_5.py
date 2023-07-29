# def reverse_ascending(numbers):
#     result = []
#     ascending_sequence = []
#     previous_comparison_ascending = False

#     for index, current_value in enumerate(list(numbers)):
#         if index - 1 < 0:
#             print("1")
#             continue

#         if current_value > numbers[index - 1]:
#             if ascending_sequence:
#                 ascending_sequence.append(current_value)
#             else
#                 ascending_sequence.append(numbers[index - 1])
#                 ascending_sequence.append(current_value)

#         else:
#             if ascending_sequence:
#             result.extend(ascending_sequence[::-1])
#             ascending_sequence.clear()

#         elif current_value == numbers[index - 1]:
#             result.append(numbers[index - 1])
#             print("5")
#         # else:


#     return result

# def reverse_ascending(numbers):
#     result = []
#     ascending_sequence = []
#     for index, current_value in enumerate(numbers):
#         if index == 0:
#             continue

#         if current_value > numbers[index - 1]:
#             if ascending_sequence:
#                 ascending_sequence.append(current_value)
#             else:
#                 ascending_sequence.extend([numbers[index - 1], current_value])
#         else:
#             if ascending_sequence:
#                 ascending_sequence.append(numbers[index - 1])
#                 result.extend(ascending_sequence[::-1])
#                 ascending_sequence.clear()
#             result.append(numbers[index - 1])

#     if ascending_sequence:
#         # ascending_sequence.append(numbers[-1])
#         result.extend(ascending_sequence[::-1])

#     return result


# print(reverse_ascending([1, 2, 2, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 6, 7]))

# numbers = [ 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 9, 10, 15]

# def reverse_ascending(numbers):
#     result = []
#     ascending_sequence = []

#     for index, current_value in enumerate(numbers):
#         if index - 1 < 0:
#             continue

#         if current_value > numbers[index - 1]:
#             if ascending_sequence:
#                 ascending_sequence.append(current_value)
#             else:
#                 ascending_sequence.extend([numbers[index - 1], current_value])
#         else:
#             if ascending_sequence:
#                 # ascending_sequence.append(numbers[current_value])
#                 result.extend(ascending_sequence[::-1])
#                 ascending_sequence.clear()

#             result.append(numbers[index - 1])
#     if ascending_sequence:
#         # ascending_sequence.append(numbers[-1])
#         result.extend(ascending_sequence[::-1])
#     return result

# print(reverse_ascending([1, 2, 2, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 6, 7]))


def reverse_ascending(numbers):
    result = []
    ascending_sequence = []

    for index, current_value in enumerate(numbers):
        if index - 1 < 0:
            continue

        if current_value > numbers[index - 1]:
            if ascending_sequence:
                ascending_sequence.append(current_value)
            else:
                ascending_sequence.extend([numbers[index - 1], current_value])
        else:
            if ascending_sequence:
                result.extend(ascending_sequence[::-1])
                ascending_sequence.clear()
            else:
                result.append(numbers[index - 1])

    if ascending_sequence:
        result.extend(ascending_sequence[::-1])
    if len(result) != len(numbers):
        result.append(numbers[-1])

    return result

# print(reverse_ascending([1, 2, 2, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7]))