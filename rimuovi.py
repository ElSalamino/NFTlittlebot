@app.on_message(filters.command(["rimuovi","rimuovi@NFTlittlebot"]) & ~filters.user(bannati))
def rimuovi(client, message): 
    username = message.from_user.username
    user = player[username]
    scheda = user["scheda"]
    arma = scheda["arma"]
    prot = scheda["protezione"]
    
    if "set" in scheda:
        unequiclassi(scheda,scheda["set"])
        
    if len(message.command) == 1:
        unequiP1(scheda,prot)
        unequiA(scheda,arma)
        message.reply("Ora sei nudo!")
    else:
        
        if message.command[1].lower() in posA:
            
            unequiA(scheda,arma)
            message.reply("Arma riposta!")
        if message.command[1].lower() in posB:
            unequiP1(scheda,prot)
            message.reply("Protezione riposta!")
