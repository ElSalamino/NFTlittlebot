
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

    @app.on_message(filters.command(["wikiboss","wikiboss@NFTlittlebot"]) & ~filters.user(bannati))
def wiki(client, message): 
    
    BossAbi = {"Franco est":"Difficile ma potrebbe valerne la pena","Fantasma del rimorso":"Un fantasma intangibile, che vuoi che sia?","IL FOLLE":"COSE SUCCEDONO MA E' UNO SCONTRO NORMALE E FOOOLLE","Leviatano delle sabbie":"Un leviatano in grado di controllare la sabbia, fate attenzione a non prolungare troppo lo scontro","Cerbero":"Un agglomerato di odio e morte, spesso serve ucciderlo diverse volte prima di morire","Demone spezza-ossa":"Presta attenzione a lui, un colpo solo potrebbe esserti fatale!","Carl":"Non è molto spaventoso più che tutto è molto sfuggevole","Orrore della palude" :"Un tuttuno con la palude, difficile da abbattere senza i giusti mezzi!","IppoSciamano":"Piccolo ed indifeso, piccolo e pieno di antichi fantasmi del passato"}
    text = "Ecco una wiki dei boss conosciuti:\n"
    for b in Boss:
        
        abi = BossAbi[b]
        stat = Boss[b]
        vita = stat["hp"]
        at = stat["atk"]
        dif = stat["def"]
        agi = stat["agi"]
        
        text += f"{b}, un terribile boss!\n❤️Vita: {vita}\n🪓Attacco: {at}\n🥋Difesa: {dif}\n🌪️Agilità: {agi}\n⭐️Abilità: {abi}\n\n"
    text += "Perdere contro un boss ti inabiliterà per molto tempo, fai attenzione!"
    message.reply(text)

