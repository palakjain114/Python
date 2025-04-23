s=str(input('enter a string: '))
a=str(input('enter another string to be removed in string: '))
r=s.split(a)
rs=""
for i in r:
    rs+=i
print(rs)
