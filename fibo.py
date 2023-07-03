num=int(input("enter your number: "))

if num==0:
    print(0)
    
elif num==1:
    print(1)
    
else:
    Fibonacciseries=[1,0]
    for i in range(1,num):
        Fibonacciseries.append((Fibonacciseries[i-1])+Fibonacciseries[i])

print(Fibonacciseries)