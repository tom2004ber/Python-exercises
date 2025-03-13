count = 0
massimo = 0
while(True):
    n = input("Digita un numero, digitare 'exit' per uscire: ")
    
    if(count == 0 and n == "exit"):
        print("Ciclo terminato. Impossibile trovare il massimo")
        break
    elif(n == "exit"):
        print("Il massimo rilevato è: ", massimo)
        break
    elif(count == 0):
        massimo = int(n)
    elif(int(n) > massimo):
        massimo = int(n)
    
    count += 1