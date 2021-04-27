def multiply(x: int, y: int) -> int:
    def add(a, b):
        while b:
            carry = a & b
            a, b = a ^ b, carry << 1
        return a

    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

assert multiply(5, 4) == 20
assert multiply(8, 5) == 40