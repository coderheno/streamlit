import mymat
add = lambda x,y: x+y
print("Simple calc:")
a = float(input("Enter a:"))
b = float(input("Enter b:"))
print("Choice(1/2/3)")
print("1.Add")
print("2.Sub")
print("3.Mul")
choice = input("Enter your choice:")
if choice=="1":
    print("result=",add(a,b))
else: print("wrong")
if choice=="1":
    print("result=",mymat.add(a,b))
else: print("wrong")