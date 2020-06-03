if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    b=0
    c=max(arr)
    for i in arr:
        a=i
        if a>b and a!=c:
            b=a 
    print(b) 
