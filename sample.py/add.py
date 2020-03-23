def add(numbers):
    if numbers == "":
        return 0

    elif "," not in numbers:
        return int(numbers)