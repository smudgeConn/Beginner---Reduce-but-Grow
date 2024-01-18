def reverse_letter(string):
    res = ''
    for letter in string:
        if letter.isalpha():
            res += letter
    return res[::-1]
