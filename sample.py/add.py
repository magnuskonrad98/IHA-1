def add(numbers):
    if numbers == "":
        return 0

    elif "," not in numbers:
        return int(numbers)

    else:
        num_a, num_b = numbers.split(",")
        return int(num_a) + int(num_b)