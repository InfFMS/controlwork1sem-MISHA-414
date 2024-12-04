
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if  (  not( (x==y)==1 and (not(y) and w)==0) == ((w==1 and z==0) or (x==1 and y==0))   )== 0:
                    print(x, y, z, w)