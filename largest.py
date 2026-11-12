a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if a>b and a>c:
    print("a is largest")
elif b>c and b>a:
    print("b is the largest")
else:
    print("c is the largest")