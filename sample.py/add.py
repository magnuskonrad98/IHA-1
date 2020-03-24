import re

class NegativeException(Exception):
    pass

def add(numbers):
    if numbers == "":
        return 0

    else:
        num_list = re.split(",|\n", numbers)
        num_sum = 0
        negative_list = []
        for num in num_list:
            if int(num) < 0:
                negative_list.append(num)
            elif int(num) <= 1000:
                num_sum += int(num)
        if negative_list == []:
            return num_sum

        else:
            neg_str = ",".join(negative_list)
            raise NegativeException("Negatives not allowed:{}".format(neg_str))

