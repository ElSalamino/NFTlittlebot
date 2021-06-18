
@app.on_message(filters.command(["negozio"]) & filters.private & ~filters.user(bannati))
def negozio(client, message):   
    username = message.from_user.username

    txt = "Benvenuto al negozio!\nQui potrai spendere la tua gloria per ottenere potenziamenti e simili!\nIl negozio è in beta, non odiarci\n"
    for cose in shop:
        prezzo = shop[cose]
        txt += f"{cose} - {prezzo} gloria 🏆\n"
    bottoni = list()
    for appz in shop:
        bottoni.append([InlineKeyboardButton(appz, callback_data = appz)])
        
    reply_markup = InlineKeyboardMarkup(bottoni)
    
    message.reply_text(txt, reply_markup = reply_markup)
        

@app.on_message(filters.command(["approccio"]) & filters.private & ~filters.user(bannati))
def approccio(client, message):   
    username = message.from_user.username

    txt = "Ecco una serie di approcci che potrebbero piacerti, questo menù è in beta!\nPer ora l'approccio scelto viene applicato a tutte le scelte:"
    bottoni = list()
    for appz in Approcci:
        bottoni.append([InlineKeyboardButton(appz, callback_data = appz)])
        
    reply_markup = InlineKeyboardMarkup(bottoni)
    
    message.reply_text(txt, reply_markup = reply_markup)
