
@app.on_message(filters.command(["bandiera","bandiera@NFTlittlebot"]) & ~filters.user(bannati))
def gloria(client, message):
    username = message.from_user.username  
    if player[username]["team"] != None and player[username]["team"] != "nessuno":
        team = player[username]["team"]
        if "Bandiera" in clan[team]:
            testo = "Sventoli con felicità la bandiera del tuo clan davanti a tutti!\n\n\n"
            for riga in  clan[team]["Bandiera"]:
                testo += listToString(riga) + "\n"
                
            message.reply(testo)
        else:
            message.reply("Nessuno ha mai disegnato la vostra bandiera!")
    else:
        message.reply("Non hai un team!")

        
        
@app.on_message(filters.command(["disegna","disegna@NFTlittlebot"]) & ~filters.user(bannati))
def gloria(client, message):
    username = message.from_user.username  
    if player[username]["team"] != None and player[username]["team"] != "nessuno":
        team = player[username]["team"]
        if clan[team]["Sarto"] == username:
            if len(message.command) == 1:
                message.reply("Usa /disegna x y emoji per sostituire una casella!")
            x = int(message.command[1]) - 1
            y = int(message.command[2]) - 1
            emoji = message.command[3][0]
            try:
                clan[team]["Bandiera"][x][y] = emoji
                message.reply("Fatto")
            except:
                message.reply("Mmmm, non credo vada bene così...")
        else:
            message.reply("Non sei il sarto del clan!")
    else:
        message.reply("Non sei in un clan!")
  
