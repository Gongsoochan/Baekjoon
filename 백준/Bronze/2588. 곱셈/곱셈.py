a=int(input())
b=int(input())
b1=int(str(b)[-1])
b2=(int(str(b)[-2]))*10
b3=(int(str(b)[-3]))*100
c=a*b1
d=a*b2
e=a*b3
f=c+d+e
print(c)
print(int(d/10))
print(int(e/100))
print(f)