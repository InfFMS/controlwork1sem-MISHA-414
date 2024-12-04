def delit(n):
    count=0
    answer=[]
    for i in range(2, n):
        if n%i==0:
            count+=1
            answer.append(i)
    return [count, answer]

cou=0
for num in range(174457, 174506):
    d=delit(num)
    if d[0]==2:
        print(num, d[1])

