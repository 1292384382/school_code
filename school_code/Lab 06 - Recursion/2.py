def get_sum_digits(number):
    number=str(number)
    if len(number)==0:
        return 0
    else:
        return int(number[0])+get_sum_digits(number[1:])