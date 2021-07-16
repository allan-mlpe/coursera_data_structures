def read_input():
    n, W = [int(x) for x in input().split(" ")]
    items = {}
    for i in range(n):
        value, weight = [int(x) for x in input().split(" ")]
        items[value] = weight

    print(items)
    print(max(items, key=int))

