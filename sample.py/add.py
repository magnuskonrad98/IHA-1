def add(numbers):
    if numbers == "":
        return 0

    elif "," not in numbers:
        return int(numbers)

    else:
        num_list = numbers.split(",")
        num_sum = 0
        for num in num_list:
            num_sum += int(num)
        return num_sum