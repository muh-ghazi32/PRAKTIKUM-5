def reverse(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    return reversed_number

A, B = input("").split()
A = int(A)
B = int(B)
A = reverse(A)
B = reverse(B)

C = A + B
print("", reverse(C))