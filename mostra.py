
@app.on_message(filters.command(["mostra","mostra@NFTlittlebot"]) & ~filters.user(bannati))
def mostra(client, message):
    username = message.from_user.username

    if len(message.command) == 1:
        message.reply_text("/mosta oggetto")
    else:
        if 1 == 1:

            user = player[username]
            zaino = user["zaino"]
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
                qt = zaino[risultati[0]]
                if risultati[0] in armi:
                    
                    arma = risultati[0]
                    v = armi[arma]["hp"]
                    a = armi[arma]["atk"]
                    d = armi[arma]["def"]
                    ag = armi[arma]["agi"]
                    t = f"""{risultati[0]}
Vitalità : {v}
Attacco: {a}
Difesa: {d}
Agilità: {ag}
Questa pare essere un __Arma__
Ne possiedi {qt} copie.
                    """
                if risultati[0] in protezioni:
                    arma = risultati[0]
                    v = protezioni[arma]["hp"]
                    a = protezioni[arma]["atk"]
                    d = protezioni[arma]["def"]
                    ag = protezioni[arma]["agi"]
                    t = f"""{risultati[0]}
Vitalità : {v}
Attacco: {a}
Difesa: {d}
Agilità: {ag}
Questa pare essere una __Protezione__
Ne possiedi {qt} copie.
                    """
                if risultati[0] in anelli:
                    aa = anelli[risultati[0]]
                    t = f"{risultati[0]}\n__{aa}__\nNe possiedi {qt} copie."
                if risultati[0] in usabili:
                    aa = usabili[risultati[0]]
                    t = f"{risultati[0]}\n__{aa}__\nNe possiedi {qt} copie."
                if risultati[0] in decoro:
                    aa = decoro[risultati[0]]
                    t = f"{risultati[0]}\n__{aa}__\nNe possiedi {qt} copie."
                
            else:
                t = "Nessun risultato"
            
            try:
                
                if risultati[0][:-4] in eventi:
                        evento = eventi[risultati[0][:-4]]
                        t += f"\n**{evento}**"
                if risultati[0] in eventi:
                        evento = eventi[risultati[0]]
                        t += f"\n**{evento}**"
            except:
                pass
            try:
                
                    
                message.reply(t)
            except:
                pass
