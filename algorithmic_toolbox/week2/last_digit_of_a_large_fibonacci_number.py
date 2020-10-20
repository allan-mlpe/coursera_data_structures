def last_digit_of_nth_fib_number(n):
    x, y = 0, 1
    aux = 0
    for i in range(1, n):
        aux = (x + y) % 10
        x = y
        y = aux

    return aux % 10


nth_number = int(input())
print(last_digit_of_nth_fib_number(nth_number))
