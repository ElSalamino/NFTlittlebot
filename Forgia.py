@app.on_message(filters.command(["forgia","forgia@NFTlittlebot"]) & ~filters.user(bannati))
def forgia(client, message):
    username = message.from_user.username

    if len(message.command) == 1:
        message.reply_text("La forgia è un luogo mistico, pieno di fiamme e cose così.\nQui dentro puoi offrire al grande fabbro con sicuramente un nome 2 armi o protezioni UGUALI per farle salir di livello!\nL'azione non richiede attese e in beta è completamente GRATIS! (Aka offre avis)\nPer iniziare a forgiare devi essere almeno lv1, inoltre non devi indossare il pezzo che desideri riforgiare.\n\nInizia quando vuoi con /forgia nomeoggetto")
    else:
        user = player[username]
        zaino = user["zaino"]
            
        list_oggetto = listToString(message.command[1:])
        if list_oggetto in zaino:
            risultati = [list_oggetto]
        else:
            
            risultati = search(zaino,list_oggetto)
        if 1 == 1:
            
            if len(list(risultati)) > 1:
                message.reply_text("Sii più preciso!")
            elif len(list(risultati)) == 0:
                message.reply_text("Non ci sono oggetti così chiamati nel tuo zaino!")
            elif len(list(risultati)) == 1:
                item = risultati[0]
                if item == player[username]["scheda"]["arma"] or item == player[username]["scheda"]["protezione"]:
                    message.reply("L'azione è impossibile, hai ancora equipaggiato quell'oggetto")
                elif item in armi or item in protezioni and item != "armatura sakuretsu LV0":
                    listina = item.split("LV")
                    
                    lv = listina[1]
                    coso = listina[0]
                    if player[username]["zaino"][item] > 1:
                        player[username]["zaino"][item] -= 2
                        if player[username]["zaino"][item] == 0:
                            player[username]["zaino"].pop(item)
                        lv = int(lv) + 1
                        new_it = f"{coso}LV{lv}"
                        try:
                            player[username]["zaino"][new_it] += 1
                        except:
                            player[username]["zaino"][new_it] = 1
                        message.reply(f"Il fabbro che ha sicuramente un nome prende {coso}e dopo diverse martellate lo potenzia!\nOra ha il 10% aggiuntivo di tutte le stats!\nTi è costato 0 Gloria!")
                        
                    else:
                        message.reply("Ti servono 2 copie di questo item")
                else:
                    message.reply("Questo oggetto non è forgiabile")
