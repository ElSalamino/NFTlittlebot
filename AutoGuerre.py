@sched.scheduled_job('cron', day_of_week='mon,thu', hour=12)
def Auto_inizio_guerra():
    print("Guerra iniziata!")
    x = 0
    tutto = dict()
    for x in clan:
        tutto[x] = clan[x]["punti"]
    dict1 = {k: v for k, v in sorted(tutto.items(), key=lambda item: item[1])}
    dicr2 = list()
    for i in dict1:
        dicr2.append(i)
                 
    for cl in clan:
        
        position = list(dicr2).index(cl)
    
        while True:
            mod = random.randint(-4,3)
            try:
                value = position-mod
                if value > -1:
                    oppo = dicr2[value]
                    if x != oppo:
                        break
            except:
                pass
            
        clan[cl]["inguerra"] = oppo
        clan[cl]["nemico"] = copy.deepcopy(clan[oppo]["villaggio"])
        app.send_message(clan[oppo]["Creatore"],f"Il vostro villaggio è in assalto da {cl}!")
        bandiera = ""
        if "Bandiera" in clan[oppo]:
            for riga in  clan[oppo]["Bandiera"]:
                bandiera += listToString(riga) + "\n"
                
        for membro in clan[cl]["membri"]:
            try:
                
                app.send_message(membro,f"All'orizzonte si erge la bandiera di {oppo}\n{bandiera}\nVEDETE BENE DI FARLA CADERE!\nSarete così ricompensati con la gloria ed il potere!")
            except:
                pass
    loggine.send_message("@NFTUpdates","Non per allertarvi ma la guerra è iniziata, avete 24 ore per assaltare tutto il villaggio avversario!")
