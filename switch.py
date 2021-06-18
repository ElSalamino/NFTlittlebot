@app.on_message(filters.command(["switch","switch@NFTlittlebot"]))
def sfida(client, message): 
    togliere = list()
    for x in inabilitati:
        if inabilitati[x] == "Una copia dell'arte della guerra autografata":
            pass
        else:
            oldtime = inabilitati[x]
            if time.time() - oldtime > 900:
                try:
                    app.send_message(x,"Ok ti dovresti essere ripreso")
                except:
                    pass
                togliere.append(x)
                    
    for x in togliere:
        inabilitati.pop(x)
    username = message.from_user.username
    if username in battaglieri:
        battaglieri.remove(username)
        message.reply("Sfide chiuse!")
    else:
        battaglieri.append(username)
        message.reply("Sfide aperte!")
        
