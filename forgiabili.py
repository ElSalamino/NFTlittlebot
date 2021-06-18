                    
@app.on_message(filters.command(["forgiabili","forgiabili@NFTlittlebot"]) & ~filters.user(bannati))
def forgiabili(client, message):
    if len(message.command) == 1:

        username = message.from_user.username
        zaino = player[username]["zaino"]
        numero = len(player[username]["zaino"])
        text = f"Potresti forgiare:"
        for figura in zaino:
            qt = zaino[figura]
            if figura in list(armi) and qt > 1:
                
                tipo = armi[figura]["type"]
                text += f"\n - `{figura}` x {qt} {tipo}"
            elif figura in protezioni and qt > 1:
                
                tipo = protezioni[figura]["type"]
            
            
                text += f"\n - `{figura}` x {qt} {tipo}"
        
        chunk = separatore(text)
        for t in chunk:
            message.reply_text(t)
            
