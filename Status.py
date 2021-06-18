@app.on_message(filters.command(["status","status@NFTlittlebot"]) & ~filters.user(bannati))
def status(client, message):
    username = message.from_user.username
    t = "Ecco l'elenco degli status attivi:\nSfide:\n"
    finder = player[username]["scheda"]["boost"]["sfida"]
    for eff in finder:
        nome = eff
        forza = finder[eff]["lv"]
        durata = finder[eff]["dur"]
        
        t += f"- {nome} {forza} ⏱ {durata}\n"
    t += "\nAssalto:\n"
    finder = player[username]["scheda"]["boost"]["assalto"]
    for eff in finder:
        nome = eff
        forza = finder[eff]["lv"]
        durata = finder[eff]["dur"]
        
        t += f"- {nome} {forza} ⏱ {durata}\n"
    
    message.reply(t)
