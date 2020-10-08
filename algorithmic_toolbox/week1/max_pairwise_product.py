def max_pairwise_product(numbers):
    x1, x2 = 0, 0
    for i in numbers:
        if i >= x1:
            x2 = x1
            x1 = i
        else:
            if i >= x2:
                x2 = i
    return x1*x2


n = int(input())
numbers = [int(x) for x in input().split(" ")]

print(max_pairwise_product(numbers))