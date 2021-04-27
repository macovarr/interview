def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j -1
    return True

def is_palindrome_pythonic(s):
    return all(a == b for a, b in zip(
        map(str.lower, filter(str.isalnum, s)),
        map(str.lower, filter(str.isalnum, reversed(s)))
    ))

assert is_palindrome('A man, a plan, a canal, Panama') == True
assert is_palindrome_pythonic('Able was I, ere I saw Elba!') == True
assert is_palindrome('Ray a Ray') == False