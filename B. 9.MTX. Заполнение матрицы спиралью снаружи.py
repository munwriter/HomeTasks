n = int(input())

l = [[0]*n for i in range(n)]

if n==0:
    print(0)
else:
    elem = 1
    for count in range(n-1):

        #верхняя строка круга спирали
        for j in range(0 + count, n - count):
            l[count][j] = elem
            elem += 1

        #правая строка круга спирали   
        for j in range(1 + count, n - count):
            l[j][-1-count] = elem
            elem += 1

        #левая строка круга спирали
        for j in range(0 + count+1, n - count):
            l[-1-count][-1-j] = elem
            elem += 1
        
        #нижняя строка круга спирали
        for j in range(0 + count+1, n-1 - count):
            l[-1-j][count] = elem
            elem += 1


    for i in range(n):
        print(*l[i])