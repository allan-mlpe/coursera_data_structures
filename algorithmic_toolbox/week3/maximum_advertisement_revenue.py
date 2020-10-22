def max_revenue(profits, clicks):
    profits.sort(reverse=True)
    clicks.sort(reverse=True)

    revenue = 0
    for i in range(len(profits)):
        revenue += profits[i]*clicks[i]

    print(revenue)


input()
p = [int(p) for p in input().split(" ")]
c = [int(c) for c in input().split(" ")]

max_revenue(p, c)
