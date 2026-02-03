n = int(input().strip())

for _ in range(n):
    arr = list(map(int, input().strip().split()))
    
    lst = arr[:]
    res1 = []
    res1.append(lst.pop(0))
    possible1 = True
    while lst:
        left = lst[0]
        right = lst[-1]
        last = res1[-1]
        if left <= last and right <= last:
            if left >= right:
                res1.append(lst.pop(0))
            else:
                res1.append(lst.pop())
        elif left <= last:
            res1.append(lst.pop(0))
        elif right <= last:
            res1.append(lst.pop())
        else:
            possible1 = False
            break
    
    lst = arr[:]
    res2 = []
    res2.append(lst.pop())
    possible2 = True
    while lst:
        left = lst[0]
        right = lst[-1]
        last = res2[-1]
        if left <= last and right <= last:
            if left >= right:
                res2.append(lst.pop(0))
            else:
                res2.append(lst.pop())
        elif left <= last:
            res2.append(lst.pop(0))
        elif right <= last:
            res2.append(lst.pop())
        else:
            possible2 = False
            break
    
    if possible1:
        print(' '.join(map(str, res1)))
    elif possible2:
        print(' '.join(map(str, res2)))
    else:
        print('НЕТ')