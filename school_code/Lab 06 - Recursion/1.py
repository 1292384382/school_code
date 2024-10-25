def get_sum_ascii(word):
    n=len(word)
    if n==0:
        return 0
    else:
        return ord(word[0])+get_sum_ascii(word[1:])