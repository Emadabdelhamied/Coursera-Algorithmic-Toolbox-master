# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    while left<=right:
        mid = (left+right)//2
        if a[mid]==x:
            return mid
        if a[mid]>x:
            right=mid-1
        else:
            left=mid+1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    seq = [int(i) for i in input().split()]
    search_seq = [int(i) for i in input().split()]
    n = seq[0]
    seq = seq[1:]
    output = list()
    for i in search_seq[1:]:
        ans = binary_search(seq, i)
        output.append(ans)
    print(' '.join([str(i) for i in output]))