def car_fueling(d, m, n, stops):
    stops.append(d)

    refills = 0
    last_stop = 0

    for i in range(n+1):
        current_stop = stops[i]

        if (current_stop - last_stop) <= m:
            continue
        else:
            if i == 0 or current_stop - stops[i-1] > m:
                refills = -1
                break
            else:
                last_stop = stops[i-1]
                refills += 1

    return refills


d = int(input())
m = int(input())
n = int(input())
stops = [int(x) for x in input().split(" ")]

print(car_fueling(d, m, n, stops))
