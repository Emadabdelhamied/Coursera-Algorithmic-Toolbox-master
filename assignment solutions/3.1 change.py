def get_change(m):
    coins=[10,5,1]
    num_of_coins=0
    for coin in coins:
        num_of_coins+=int(m/coin)
        m=m%coin
    return num_of_coins
import time
if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
