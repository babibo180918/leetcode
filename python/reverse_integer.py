def reverse(n):
    result = 0
    minus = n / abs(n)
    n = abs(n)
    while n > 0:
        result = result * 10 + n % 10
        n /= 10
    return result * minus

print(reverse(123))
print(reverse(-123))
print(reverse(120))
