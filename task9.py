def f(a, b):
    if b==0:
        return 0
    elif a>b:
        return f(a-1, b)+b
    else:
        return f(a, b-1) + a

print(f(1, 2))


# разложим на множетели 2097152

lst=[]
count=0
for i in range(1, 2097153):
    if 2097152%i==0:
        lst.append(i)
        count+=1
print(count)


