sentence = 'ablewasiereisawelba'


def is_palindrome(word):
    # a word with a single character is always a palindrome
    if len(word) == 1:
        return True

    # two character word is easy to check
    elif len(word) == 2:
        if word[0] == word[1]:
            return True
        else:
            return False
    # check the opposite ends of a word, if they are equal,
    # then can proceed to checking the middle
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


is_palindrome(sentence)
is_palindrome('racecar')
is_palindrome('tattarrattat')
is_palindrome('saippuakivikauppias')