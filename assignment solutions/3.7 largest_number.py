def largest_number(a):
    #write your code here
    res = ""
    while a!=[]:
        max_digit=0
        for digit in a:
            if int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit)):
                max_digit=digit
        res += str(max_digit)
        a.remove(max_digit)
    return res

if __name__ == '__main__':
    n=int(input())
    data = list(map(int,input().split()))
    print(largest_number(data))
