
@app.on_message(filters.command(["info"]) & ~filters.user(bannati))
def eenfo(client, message):   
    iscritti = len(player)
    trovabili = len(tutto)
    strutturs = len(strutture)
    set = len(classi)
    animali = len(animaletti)
    clans = len(clan)
    attivi = 0
    pescis = len(pesci)
    diffe = len(ingredienti)
    draghi = len(draghi)
    animalati = 0  
    ora = 0
    for p in last_sms:
        if time.time() - last_sms[p] < 3600:
            ora += 1
    for ass in player:
        if "pet" in player[ass]:
            animalati += 1 
        if player[ass]['prima'] == True:
            attivi += 1
    
    message.reply(f"""**Menù info del bot:**
Iscritti: {iscritti}
Clan: {clans}
Oggetti trovabili in sfida: {trovabili}                  
Strutture inventate nel villaggio: {strutturs}                  
Animaletti possibili: {animali}                  
Persone con un animaletto: {animalati}
Set disponibili: {set}
Pesci differenti: {pescis}
Ingredienti differenti: {diffe}
Draghi: {draghi}
Cose rotte: __si__

__Attivi oggi: {attivi}__
__Dei quali attivi nell'ultima ora: {ora}__

Abbiamo un gruppo ot; https://t.me/joinchat/3H0yl932lSwyNTY0
Abbiamo un gruppo mercato; https://t.me/joinchat/h-zcLkBUOL8zYTc0""")
