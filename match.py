
def match(sorters,nome):
    
    sortes = [a[0] for a in sorters]
    posizione = sortes.index(nome)
    

    if posizione < 5:
        oppo = posizione + random.randint(-posizione,6)
    
    else:
        oppo = posizione + random.randint(-6,6)

    if oppo == posizione:
        oppo += 1
    while True:
        
        if oppo > len(sortes):
            oppo -= 2
        else:
            break
            
    if oppo == posizione:
        oppo += 1
    
    sfidante = sortes[int(oppo)]

    return sfidante
