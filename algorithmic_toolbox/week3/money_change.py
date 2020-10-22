def money_change(n):
    coins = [10, 5, 1]
    change_coins = 0
    pointer = 0

    while pointer < len(coins) or n > 0:
        coin = coins[pointer]
        if n >= coin:
            n -= coin
            change_coins += 1
        else:
            pointer += 1

    return change_coins


n = int(input())
print(money_change(n))
