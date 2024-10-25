def get_min_odd(numbers):
    if len(numbers)==0:
        return 9999
    elif numbers[0]%2==0:
        odd_number=get_min_odd(numbers[1:])
        return odd_number
    elif numbers[0]%2==1:
        odd_number1 = get_min_odd(numbers[1:])
        if odd_number1 > numbers[0]:
            return numbers[0]
        else:
            return odd_number1

