
@app.on_message(filters.command(["dai","dai@NFTlittlebot"]) & ~filters.user(bannati))
def dai(client,message):
    username = message.from_user.username
    
    if len(message.command) == 1:
        message.reply_text("/dai nome_oggetto [username]")
    elif message.reply_to_message == None:
        target = message.command[-1].replace("@","")
        print(target)
        if target in player:
              
            if target == username:
                message.reply_text(f"Scegli un altra persona!")
            else:
                
                zaino = player[username]["zaino"]
                ricevente = player[target]["zaino"]
                list_oggetto = listToString(message.command[1:-1])
                risultati = search(zaino,list_oggetto)
                            
                if len(risultati) > 1:
                    message.reply_text("Sii più preciso!")
                elif len(risultati) == 0:
                    message.reply_text("Non ci sono oggetti così chiamati nel tuo zaino!")
                elif len(risultati) == 1:
                    if risultati[0] in usabili or risultati[0] in decoro or risultati[0] == "armatura sakuretsu LV0" :
                        message.reply("Questi item non sono scambiabili!")
                    else:

                        if risultati[0] in ricevente:
                            ricevente[risultati[0]] += 1
                        else:
                            ricevente[risultati[0]] = 1
                            
                        zaino[risultati[0]] -= 1
                        if zaino[risultati[0]] == 0:
                            del zaino[risultati[0]]
                                    
                        message.reply_text(f"{username} dà {risultati[0]} a {target}!")
                        try:
                            app.send_message(target,f"{username} ti dà {risultati[0]}!")
                        except:
                            pass
                        loggine.send_message(-1001414903628,f"{username} dà {risultati[0]} a {target}!")
        else:
            message.reply("Questo utente non gioca!")
    
    else:
        if 1 == 1:
            user = player[username]
            scheda = user["scheda"]
            arma = scheda["arma"]
            prot = scheda["protezione"]
            
            target = message.reply_to_message.from_user.username
            if target == "NFTlittlebot":
                target = "AvisSatyra"
                
            if target in player:
                
                if target == username:
                    message.reply_text(f"Scegli un altra persona!")
                else:
                    
                        zaino = player[username]["zaino"]
                        ricevente = player[target]["zaino"]
                        list_oggetto = listToString(message.command[1:])
                        risultati = search(zaino,list_oggetto)
                        
                        if len(risultati) > 1:
                            message.reply_text("Sii più preciso!")
                        elif len(risultati) == 0:
                            message.reply_text("Non ci sono oggetti così chiamati nel tuo zaino!")
                        elif len(risultati) == 1:
                            if risultati[0] in usabili or risultati[0] in decoro or risultati[0] == "armatura sakuretsu LV0":
                                message.reply("Questi item non sono scambiabili!")
                            else:
                                if risultati[0] == arma or risultati[0] == prot:
                                    message.reply("Devi prima posarlo!")
                                else:
                                      
                                    if risultati[0] in ricevente:
                                        ricevente[risultati[0]] += 1
                                    else:
                                        ricevente[risultati[0]] = 1
                                    zaino[risultati[0]] -= 1
                                    if zaino[risultati[0]] == 0:
                                        del zaino[risultati[0]]
                                    
                                    message.reply_text(f"{username} dà {risultati[0]} a {target}!")
                                    try:
                                        app.send_message(target,f"{username} ti dà {risultati[0]}!")
                                    except:
                                        pass
                                    loggine.send_message(-1001414903628,f"{username} dà {risultati[0]} a {target}!")
            else:
                message.reply("Questo utente non gioca!")
