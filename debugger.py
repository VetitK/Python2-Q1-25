def greet():
    a = 2+2
    return "Hello"

def gcd_euclidean(a, b):
    while b != 0:
        print(greet())
        r = a % b
        a = b
        b = r
    return b

print(gcd_euclidean(16, 24))

[1,2].sort()