a = (6, 5, 2006)
b = (14, 8, 2006)

l1 = list(a)
l2 = list(b)
if l1[2] == l2[2]:
    yearsum = 0
elif l1[2] > l2[2]:
    yearsum = l1[2] - l2[2]
else:
    yearsum = l2[2] - l1[2]
if l1[1] == l2[1]:
    monthsum = 0
elif l1[1] > l2[1]:
    monthsum = l1[1] - l2[1]
else:
    monthsum = l2[1] - l1[1]
if l1[0] == l2[0]:
    daysum = 0
elif l1[0] > l2[0]:
    daysum = l1[0] - l2[0]
else:
    daysum = l2[0] - l1[0]
wholesum = [daysum, monthsum, yearsum]
print(wholesum)
sumday = daysum + monthsum*30 + yearsum*365
print(sumday)
