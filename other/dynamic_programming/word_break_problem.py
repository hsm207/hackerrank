def segment_input(word, dictionary):
    if not word:
        return True
    else:
        can_break = False
        for w in dictionary:
            if word.startswith(w):
                print(w)
                can_break = can_break or segment_input(word[len(w):], dictionary)

        return can_break



dictionary = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
input_str ='ilikesamsung'
segment_input(input_str, dictionary)