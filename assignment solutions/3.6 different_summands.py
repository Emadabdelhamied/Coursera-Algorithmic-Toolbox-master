def optimal_summands(n):
    summands = []
    x=n
    for i in range(1,n+1):
        if x>2*i:
            summands.append(i)
            x-=i
        else:
            summands.append(x)
            break
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
