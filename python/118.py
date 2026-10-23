# Find the Second Smallest Distinct Number

def second_smallest(numbers):
    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[1]


numbers = [15, 3, 8, 1, 12, 3, 1]

result = second_smallest(numbers)

if result is None:
    print("Second smallest number does not exist")
else:
    print("Second smallest number:", result)