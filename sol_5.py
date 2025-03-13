n = int(input("Digita un numero: "))
if(n == 0):
    print(0)
else:
    somma = 0
    if(n < 0):
        n*=-1
    while(n!= 0):
        if(n%10 == 0):
            n/= 10
        else:
            n-=1
            somma+=1
    print(somma)
        