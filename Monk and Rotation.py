for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = list(map(int,input().split()))
    k%=n
    mod_arr=arr[n-k:]+arr[:n-k]
    for _ in mod_arr:
        print(_,end=' ')
    print()
