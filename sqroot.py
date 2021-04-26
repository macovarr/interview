def sqroot(n):
    if n == 0:
        return 0

    x_mid = n / 2.0
    upper = x_mid + 1
    while x_mid != upper:
        delta = n / x_mid
        upper = x_mid
        x_mid = (x_mid + delta) / 2
    return round(x_mid, 3)

assert sqroot(0) == 0
assert sqroot(160.4) == 12.665
assert sqroot(16) == 4.0
assert sqroot(17) == 4.123
assert sqroot(25) == 5.0
assert sqroot(46.67) == 6.832