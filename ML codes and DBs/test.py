def isPrime(l):
    if l > 1:
        for i in range(2, l):
            if (l % i) == 0:
                return 0
        else:
            return 1

    else:
        return 0

for _ in range(int(input())):
    l,r = map(int,input().split())
    m,mx = 0,0
    for i in range(l,r+1):
        if isPrime(i):
            m = i
            break
        else:
            continue
    for i in range(l,r+1):
        j = r-i + l
        if isPrime(j):
            mx = j
            break
        else:
            continue
    print(m,mx)
    if m == 0:
        print(-1)
        continue
    elif m == mx:
        print(0)
        continue
    print(mx-m)