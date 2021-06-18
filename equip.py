def equiA(user,arma,cosa):
    
    stats = ['hp','def','atk','agi']
    if user[cosa] == None:
        user[cosa] = arma
        for st in stats:
            user[st] += armi[arma][st]
        text = f"Equipaggiata con successo {arma}!"
    else:
        text = "Hai già una arma addosso!"
    
    return text
    

def classe(user,classe):
    
    stats = ['hp','def','atk','agi']
    for st in stats:
        
        user[st] +=  bonus[classe][st]
        
