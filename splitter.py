
def separatore(text):
    returner = list()
    
    contante = 0
    testo = ""
     
    righe = text.split("\n")
    for riga in righe:
        testo += f"{riga}\n" 
        contante += len(riga)
        if contante > 3800:
            returner.append(testo)
            testo = ""
            contante = 0
            
    returner.append(testo)
    return returner
