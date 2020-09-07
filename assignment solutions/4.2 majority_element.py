# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     for i in a:
#         if a.count(i)>n/2:
#             return 1
#     return -1

# if __name__ == '__main__':
#     n=int(input())
#     a = list(map(int, input().split()))
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)
def divide_func(seq, l, r):
    if l+1==r:
        return seq[l]
    elif l+2==r:
        return seq[l]
    m = (l+r)//2
    left = divide_func(seq, l, m)
    right = divide_func(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else: 
        return -1


n = int(input())
seq = [int(i) for i in input().split()]

if divide_func(seq, 0, n) != -1:
    print(1)
else:
    print(0)