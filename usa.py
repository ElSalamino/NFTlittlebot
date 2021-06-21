
@app.on_message(filters.command(["usa"]) & ~filters.user(bannati))
def usa(client, message):
    if len(message.command) == 1:
        message.reply("/usa nomeoggetto\nPer usi multipli: /usa cosa : quanto\nPer erranti: /usa cosa , chi")
    else:
        
        
        username = message.from_user.username        
        zaino = player[username]["zaino"]
        tipo = None
        argomento = listToString(message.command[1:])
        
        if "," in argomento:
            tipo = "errante"
        elif ":" in argomento:
            tipo = "multiplo"
        else:
            tipo = "classico"
        
        if tipo == None:
            message.reply("Errore!\nContatta @ElSalamino dando come codice errore 709!")
        else:
            
            if tipo == "errante":
                chi = argomento.split(",")[-1].replace(" ","").replace("@","")
                cosa = argomento.split(",")[0]
                
            if tipo == "multiplo":
                quanto = argomento.split(" ")[-1]
                cosa = argomento.split(":")[0]
                
            if tipo == "classico":
                cosa = argomento
                
            if cosa in zaino:
                risultati = [cosa]
            else:
                risultati = search(zaino,cosa)
            if len(risultati) == 0:
                risultati = search(player[username]["pozioni"],cosa)
            if len(list(risultati)) > 1:
                message.reply_text("Sii più preciso!")
            elif len(list(risultati)) == 0:
                message.reply_text("Non ci sono oggetti così chiamati nel tuo zaino!")
            elif len(list(risultati)) == 1:
                if risultati[0] in usabili or risultati[0] in pozioni:
                    ricercato = risultati[0]
                    
                    if tipo == "classico" or tipo == "multiplo":
                        if ricercato == "Dell'acqua fresca":
                            
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:

                                    zaino[ricercato] -= 1
                                    if zaino[ricercato] <= 0:
                                        zaino.pop(ricercato)
                                    try:
                                                
                                        player[username]["scheda"]["boost"]["sfida"]["Idratato"]["dur"] += 2
                                    except:
                                                
                                        player[username]["scheda"]["boost"]["sfida"]["Idratato"] = {"lv":1,"dur":2}
                                    message.reply("Dissetante e fresca.")
                                else:

                                    message.reply("Non ne hai!")
                                    break
                            
                        elif ricercato == "Un hp extra":
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:

                                    zaino[ricercato] -= 1
                                    if zaino[ricercato] <= 0:
                                        zaino.pop(ricercato)
                                    player[username]["scheda"]["hp"] += 1
                                    
                                    
                                else:

                                    message.reply("Sono finiti prima!")
                                    break
                            message.reply(f"+{rep}up")

                        elif ricercato == "Un punto attacco":
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:

                                    zaino[ricercato] -= 1
                                    if zaino[ricercato] <= 0:
                                        zaino.pop(ricercato)
                                    player[username]["scheda"]["atk"] += 1
                                    
                                else:

                                    message.reply("Sono finiti prima!")
                                    break
                            message.reply(f"{rep} danno extra approvato")

                        elif ricercato == "Un punto difesa":
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:

                                    zaino[ricercato] -= 1
                                    if zaino[ricercato] <= 0:
                                        zaino.pop(ricercato)
                                    player[username]["scheda"]["def"] += 1
                                    
                                else:

                                    message.reply("Sono finiti prima!")
                                    break
                            message.reply(f"Ecco a te {rep} scudino extra")
                                    
                        elif ricercato == "Un punto agilità":
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:

                                    zaino[ricercato] -= 1
                                    if zaino[ricercato] <= 0:
                                        zaino.pop(ricercato)
                                    player[username]["scheda"]["agi"] += 1
                                    
                                else:

                                    message.reply("Sono finiti prima!")
                                    break
                            message.reply(f"Aumentata l'abilità di salto dello {rep * 0.42069}%")
                            
                        elif ricercato == "Una licenza per animali domestici":
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:

                                    zaino[ricercato] -= 1
                                    if zaino[ricercato] <= 0:
                                        zaino.pop(ricercato)
                                    pet = random.choice(animaletti)
                                    message.reply(f"Un aereoscafo dal cielo lancia una cassa, che cadendo a terra rimbalza una quindicina di volte.\nDa dentro esce un bellissimo {pet}, che figo!")
                                    player[username]["pet"] = pet
                                    time.sleep(0.1)
                                    try:
                                        player[username]["varie"]["cambi"] += 1
                                    except:
                                        player[username]["varie"]["cambi"] = 1
                                else:

                                    message.reply("Sono finiti prima!")
                                    break
                            
                                    
                        elif ricercato == "Del latte in sacchetto":
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:
                                    if username in inabilitati:
                                        if inabilitati[username] != "Una copia dell'arte della guerra autografata":
                                            zaino[ricercato] -= 1
                                            if zaino[ricercato] <= 0:
                                                zaino.pop(ricercato)
                                            message.reply("Bevi tutto il latte e ti senti subito meglio, che comodo!")
                                            inabilitati.pop(username)
                                        else:
                                            message.reply("Non puoi riprenderti così!")
                                            break
                                    else:
                                        message.reply("Sei già in forza")
                                        break
                                else:

                                    message.reply("Sono finiti prima!")
                                    break
                                        
                                                
                        elif ricercato == "Un oggetto incartato":
                            rep = 1
                            if tipo == "multiplo":
                                rep = int(quanto)
                            for x in range(rep):

                                if ricercato in zaino:

                                    zaino[ricercato] -= 1
                                    if zaino[ricercato] <= 0:
                                        zaino.pop(ricercato)
                                    contentino = random.choice(tutto)
                                    try:
                                        player[username]["zaino"][contentino] += 1
                                    except:
                                        player[username]["zaino"][contentino] = 1 
                                    
                                    try:
                                        app.send_message(username,f"Apri l'oggetto con molto stupore e scopri essere; {contentino}, speravi in una bici ma vabbè su!")
                                    except:
                                        pass 
                                    time.sleep(0.1)

                                else:

                                    message.reply("Sono finiti prima!")
                                    break
                        
                    if tipo == "errante":
                        elapsed = time.time() - attese[ricercato]
                        
                        if elapsed < 1800:
                            ty_res = time.gmtime(1800 - elapsed)
                                    
                            tempo = time.strftime("%H:%M:%S",ty_res)
                            if ricercato == "Una mail di spam con anche qualche pene":
                                message.reply(f"Forse mancano ancora più maiuscole a caso...\nLo sbagliatore automatico dovrebbe finire in {tempo} minuti!")  

                            if ricercato == "Una copia dell'arte della guerra autografata":
                                message.reply(f"Serve leggere di più!\nIl capitolo finirà tra {tempo} pagine!")  
                            if ricercato == 'un castoro cattivissimo':
                                message.reply(f"Il castoro cattivissimo si sta ancora scaldando!\nFinirà il suo riscaldamento tra {tempo} minuti!")
                            if ricercato == 'Un megafono megaenorme':
                                message.reply(f"Batteria scarica!\nRicarica stimanta:{tempo} minuti!")
                            
                        else:
                            if chi not in list(player):
                                message.reply("Quell'utente non esiste!")
                            else:
                                if ricercato == "Una mail di spam con anche qualche pene":
                                    attese["Una mail di spam con anche qualche pene"] = time.time()
                                    
                                    zaino.pop("Una mail di spam con anche qualche pene")
                                    acui = random.choice(list(player))
                                    proprietari["Una mail di spam con anche qualche pene"] = acui
                                    pool = player[acui]["zaino"]
                                    pool["Una mail di spam con anche qualche pene"] = 1
                                                        
                                    player[chi]["punti"] -= 100
                                    player[username]["punti"] += 100
                                            
                                    try:
                                                            
                                        app.send_message(chi,f"Cliccando a caso /sfida ti si apre un link altamente non voluto.\nCercando di uscire spendi 100 tuoi punti sfida in vibratori e cose simili.\nForse non l'hai fatto totalmente per sbaglio.")

                                    except:
                                        pass
                                    try:
                                        app.send_message(acui,f"Ricevi una mail truffa, ovviamente sei troppo furbo per cascarci, ma un inoltro è sicuramente una buona idea!")
                                    except:
                                        pass
                                    try:
                                        app.send_message(username,f"E taaac, 100 punti sfida gratis!\n\n\nHey aspetta un attimo, ci sta anche l'indirizzo di {acui} tra i destinatari...")
                                    except:
                                        pass

                                if ricercato == "Una copia dell'arte della guerra autografata":
                                    attese["Una copia dell'arte della guerra autografata"] = time.time()

                                    zaino.pop("Una copia dell'arte della guerra autografata")
                                    acui = random.choice(list(player))
                                    proprietari["Una copia dell'arte della guerra autografata"] = acui
                                    pool = player[acui]["zaino"]
                                    pool["Una copia dell'arte della guerra autografata"] = 1
                                                        
                                    inabilitati[chi] = "Una copia dell'arte della guerra autografata"
                                            
                                    try:
                                                            
                                        app.send_message(chi,f"Eri totalmente intento a farti i fatti tuoi quando BONK!\nVieni colpito fortissimo da un libro di un certo spessore, ci vorrà un attimo a riprendersi...")
                                    except:
                                        pass
                                    try:
                                        app.send_message(acui,f"In una libreria ci sta in sconto una copia dell'arte della guerra, perchè non comprarla!")
                                    except:
                                        pass
                                    try:
                                        app.send_message(username,f"Prendi la copia del libro, e dopo averlo letto per diverso tempo, colpisci fortissimo in testa {chi}!\nLa copia si rompe all'impatto, ma vabbè è solo una ristampa")
                                    except:
                                        pass   

                                if ricercato == 'un castoro cattivissimo':
                                    pool = player[chi]["zaino"]
                                    if len(list(pool)) > 4:
                                        mas = 0
                                        while True:
                                            preso = random.choice(list(pool))
                                            if "Anello" in preso or "1" in preso or "2" in preso or "3" in preso or "0" in preso or mas == 5:
                                                break
                                            mas += 1
                                            try:
                                                zaino[preso] += 1
                                            except:
                                                zaino[preso] = 1
                                            try:                                                    
                                                pool[preso] -= 1
                                            except:
                                                pass
                                                
                                            if pool[preso] == 0:
                                                pool.pop(preso)

                                            pool["un castoro cattivissimo"] = 1
                                                
                                            zaino.pop("un castoro cattivissimo")
                                            try:

                                                app.send_message(chi,f"Dai su, a cosa ti serve un {preso} quando puoi avere un bellissimo castoro?")
                                            except:
                                                pass
                                            try:

                                                app.send_message(username,f"Mandi il tuo castoro cattivissimo dritto verso {chi}, lo vedi tornare con {preso}!\nPeccato che un aquila rubi il castoro cattivissimo esattamente prima di poterlo riprendere in mano!")
                                            except:
                                                pass
                                            attese["un castoro cattivissimo"] = time.time()
                                            proprietari["un castoro cattivissimo"] = chi
                                    else:
                                        message.reply("Quel giocatore non ha nulla di interessante...")
                                else:
                                    message.reply("Non ho capito cosa stai cercando di usare, codice errore 115742!")
                    else:
                        message.reply("Non ho capito cosa stai usando.")
                else:
                    message.reply("Questo item non è usabile!")
