def ls():
   a= float(input("Enter first number: "))
   b= float(input("Enter second number: "))
   if a>b:
       print("largest: ",a)
       print("smallest: ", b)
   elif b>a:
       print("largest: ",b)
       print("smallest: ", a)
   else:
       print("The numbers are equal.")
ls()
