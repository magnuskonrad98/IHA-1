import re

def add(numbers):
    if numbers == "":
        return 0

    else:
        num_list = re.split(",|\n", numbers)
        num_sum = 0
        for num in num_list:
            if int(num) <= 1000:
                num_sum += int(num)
        return num_sum
