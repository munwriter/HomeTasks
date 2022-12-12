def chet_zamena(l):
    zero_counter = 0
    for elem in range(n):
        if l[elem] == 0:
            zero_counter += 1
        elif  zero_counter == 0:
            l[elem] = 4
        elif zero_counter == 1:
            l[elem] = 1
        else:
            l[elem] = 2
    return l

def nechet_zamena(l):
    zero_counter = 0
    for elem in range(n):
        if l[elem] == 0:
            zero_counter += 1
        elif  zero_counter == 0:
            l[elem] = 4
        elif zero_counter == 1:
            l[elem] = 1
        else:
            l[elem] = 2
    return l

n = int(input())
l = [1]*n
l[0], l[-1] = 0, 0
j = 1
print(*[0]+[1]*(n-2)+[0])
for i in range(n-2):
    l  = [1]*n
    l[j] = 0
    l[-j-1] = 0
    j += 1
    if i<n//2:
        if n%2 == 0:
            l = chet_zamena(l)
        else:
            l = nechet_zamena(l)
    else:
        for e in range(n):
            if l[e] == 1:
                l[e] = 3


    print(*l)

print(*[0]+[3]*(n-2)+[0])
