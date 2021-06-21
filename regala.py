
last_gift = dict()
@app.on_message(filters.command(["regala","regala@NFTlittlebot"]) & ~filters.user(bannati))
def regala(client, message):
    username = message.from_user.username
    if message.chat.id == -1001476172565:
        try:
            other_time = last_gift[username]
        except:
             other_time = 1
                                            
        now = time.time()
                                        
        elapsed = now - other_time
                
        if elapsed > 60:
            user = player[username]
            zaino = user["zaino"]
            if len(message.command) > 1:
                
                list_oggetto = listToString(message.command[1:])
                if list_oggetto in tutto:
                    risultati = [list_oggetto]
                else:
                    risultati = search(zaino,list_oggetto)
                    
                if len(list(risultati)) > 1:
                    message.reply_text("Sii più preciso!")
                elif len(list(risultati)) == 0:
                    message.reply_text("Non ci sono oggetti così chiamati nel tuo zaino!")
                elif len(list(risultati)) == 1:
                    to_give = risultati[0]
                    if to_give not in usabili and to_give not in decoro:
                        player[username]["zaino"][to_give] -= 1
                        if player[username]["zaino"][to_give] <= 0:
                            player[username]["zaino"].pop(to_give)
                        bottoni = [InlineKeyboardButton(text="Mio", callback_data = "mio " + str(to_give))]
                        reply_markup = InlineKeyboardMarkup(bottoni)
                        txt = f"{username} lancia in aria {to_give}!\nChi lo prenderà?"
                        message.reply_text(txt, reply_markup = reply_markup)
            else:
                message.reply("/regala oggetto")
                
                
        else:
            pass
    else:
        pass

@app.on_callback_query(filters.regex('^mio'))
def pesca_callback(client, message):
    username = message.from_user.username
    info = message.data
    need = info.split(" ")
    dato = listToString(need[2:])
    try:
        player[username]["zaino"][dato] += 1
    except:
        pass
    esito = f"{username} prende per primo al volo {dato}!"
    app.edit_message_text(chat_id = message.message.chat.id,
                    message_id = message.message.message_id,
                    text = esito
                    )
    
