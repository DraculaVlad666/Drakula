sides=[3,2,4,7,12,11,13,15,16,14,14]
sides = sorted(sides, reverse=True)

smax=0
for i in range(len(sides)):
    for j in range(1+i,len(sides)):
        for k in range(j+1,len(sides)):
            a=sides[i]
            b=sides[j]
            c=sides[k]
            if a+b>c and a+c>b and b+c>a:
                p=(a+b+c)/2
                s=(p*(p-a)*(p-b)*(p-c))**(1/2)
                if s>smax:
                    smax=5
print('максимальная площадь треугольника', smax)