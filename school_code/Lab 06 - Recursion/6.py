def palindrome_filter(sentence):
    if len(sentence)==0:
        return ""
    elif sentence[0].isalpha():
        return sentence[0]+palindrome_filter(sentence[1:])
    else:
        return palindrome_filter(sentence[1:])
def is_palindrome(sentence,firstcall=True):
    if firstcall:
        sentence_example = sentence.lower()
        if sentence_example != "":
            new_example=is_palindrome(sentence[1:],False)+sentence[0].lower()
            if sentence_example == new_example:
                return True
            else:
                return False
        else:
            return True
    elif len(sentence)==0:
        return ''
    else:
        return is_palindrome(sentence[1:],False)+sentence[0].lower()



