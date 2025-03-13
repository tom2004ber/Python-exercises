n = int(input("Digita un numero: "))
if(n == 0):
    print("Numero non valido.")

else:
    divisore = n
    if(n < 0):
        n*=-1
        divisore*=-1
    while(divisore > 0):
        if(n%divisore == 0):
            print(divisore, "è un suo divisore")
        divisore -= 1
