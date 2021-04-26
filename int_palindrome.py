def int_palindrome(n):
    parts = []
    if n < 0:
        return False
    while n > 0:
        parts.append(n % 10)
        n //= 10
    return parts == list(reversed(parts))

assert int_palindrome(121) == True
assert int_palindrome(-121) == False
assert int_palindrome(12344321) == True
assert int_palindrome(12332111) == False