
# def minRefuelStops(target, startFuel, stations):
#     dp = [startFuel] + [0] * len(stations)
#     for i,location in enumerate(stations):
#         for t in range(i, -1, -1):
#             if dp[t] >= location:
#                 dp[t+1] = max(dp[t+1], dp[t] + capacity)

#     for i, d in enumerate(dp):
#         if d >= target: return i950
#     return -1

def car_fueling(dist,miles,n,gas_stations):
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:  # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank 
        curr_refill += 1
    return num_refill

if __name__ == '__main__':
    d=int(input())
    m=int(input())
    n=int(input())
    stops=list(map(int,input().split()))
    print(car_fueling(d, m,n,stops))
