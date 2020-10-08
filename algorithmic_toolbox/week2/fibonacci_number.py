def nth_fib_number(n):
    arr = [0, 1]

    for i in range(1, n):
        arr.append(arr[i] + arr[i-1])

    return arr[n]


nth_number = int(input())
print(nth_fib_number(nth_number))

