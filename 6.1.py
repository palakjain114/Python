a = [('Manav', 'ramesh', 'pappu', 'kaaludon'), ('Laalu', ), 'Munni', 'keya', 'rami']

boys = 0
girls = 0

for i in a:
   if isinstance(i, tuple):
       boys += 1

   else:
       girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)
