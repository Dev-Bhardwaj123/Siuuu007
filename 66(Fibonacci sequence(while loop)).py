num1,num2=0,1
n=int(input("Enter a no."))
i=1
print("Fibbonaci sequence")
while i<=n:
    print(num1,end='')
    res=num1 +num2
    num1= num2
    num2=res
    i=i+1
    break

