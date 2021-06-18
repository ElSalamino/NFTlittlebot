
@app.on_message(filters.command(["zaino","zaino@NFTlittlebot"]) & ~filters.user(bannati))
def zainoC(client, message):
    if len(message.command) == 1:

        username = message.from_user.username
        zaino = player[username]["zaino"]
        numero = len(player[username]["zaino"])
        text = f"Al momento possiedi ben {numero} item:"
        for figura in zaino:
            qt = zaino[figura]
            if figura in list(armi):
                
                tipo = armi[figura]["type"]
            elif figura in protezioni:
                
                tipo = protezioni[figura]["type"]
            elif figura in decoro:
                tipo = "✨"
            elif figura in usabili:
                tipo = "👝"
            
            else:
                tipo = "💍"
            
            text += f"\n - `{figura}` x {qt} {tipo}"
        text += "\nPuoi vedere categorie simili con /zaino armi, protezioni, anelli, decoro o usabili!"
        chunk = separatore(text)
        for t in chunk:
            message.reply_text(t)
    else:
        categoria = listToString(message.command[1:])
        username = message.from_user.username
        zaino = player[username]["zaino"]
        numero = len(player[username]["zaino"])
        text = f"Ecco a te un elenco più specifico:"
        for figura in zaino:
            qt = zaino[figura]
            if figura in list(armi):
                
                tipo = armi[figura]["type"]
                if categoria == "armi":
                    text += f"\n - `{figura}` x {qt} {tipo}"
            elif figura in protezioni:
                
                tipo = protezioni[figura]["type"]
                if categoria == "protezioni":
                    text += f"\n - `{figura}` x {qt} {tipo}"
            elif figura in decoro:
                tipo = "✨"
                if categoria == "decoro":
                    text += f"\n - `{figura}` x {qt} {tipo}"
                    
                     
            elif figura in usabili:
                tipo = "👝"
                if categoria == "usabili":
                    text += f"\n - `{figura}` x {qt} {tipo}"
            else:
                tipo = "💍"
                if categoria == "anelli":
                    text += f"\n - `{figura}` x {qt} {tipo}"
            
            if text == "Ecco a te un elenco più specifico:":
                possibili = search(zaino, categoria)
                for asd in possibili:
                    
                    qt = zaino[asd]
                    if asd in armi:
                        tipo = "🗡"
                    if asd in protezioni:
                        tipo = "🛡"
                    if asd in usabili:
                        
                        tipo = "👝"
                    if asd in anelli:
                        tipo = "💍"
                    if asd in decoro:
                        tipo = "✨"
                        
                    
                    text += f"\n - `{asd}` x {qt} {tipo}"
                    
            
            
        
        chunk = separatore(text)
        for t in chunk:
            message.reply_text(t)
