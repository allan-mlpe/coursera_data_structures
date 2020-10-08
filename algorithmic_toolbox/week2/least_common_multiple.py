def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, (a % b))


def least_common_multiple(a, b):
    return int((a * b) / greatest_common_divisor(a, b))


x, y = [int(i) for i in input().split(" ")]
print(least_common_multiple(x, y))
