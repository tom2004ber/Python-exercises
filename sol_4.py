n = int(input("Digita un numero: "))
if(n < 2):
    print("Non primo")
else:
    sol = True
    divisore = int(n/2) 
    while(divisore > 1):
        if(n%divisore == 0):
            sol = False
            break
        divisore-=1
    if(sol == False):
        print("Non primo")
    else:
        print("Primo!")