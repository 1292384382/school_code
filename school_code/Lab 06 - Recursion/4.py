def get_odds_list(numbers):
    if len(numbers) == 0:
        return []
    elif numbers[0] % 2 == 0:
        odd_number = get_odds_list(numbers[1:])
        return odd_number
    elif numbers[0] % 2 == 1:
        odd_number1 = get_odds_list(numbers[1:])
        return [numbers[0]]+odd_number1
