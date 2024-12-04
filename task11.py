def delit(n):
    count=0
    for i in range(2, n):
        if n%i==0:
            count+=1
    return count

cou=0
for num in range(174457, 174506):
    d=delit(num)
    if d==2:
        print(num)
