n = int(input("Inserire numero: "))
if(n < 0):
    n*=-1
if(n == 0):
    print("Pari")
while(n > 0):
    n-= 2
    if(n == 1):
        print("Dispari")
    elif(n == 2):
        print("Pari")
