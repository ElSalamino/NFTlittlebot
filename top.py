@app.on_message(filters.command(["top","top@NFTlittlebot"]) & ~filters.user(bannati))
def top(client, message):
    if len(message.command) == 1:
        v = "Top picchiatori!\n"
        d = dict()
        for tipo in player:
            if player[tipo]["punti"] == 1000 and tipo not in battaglieri:
                pass
            else:
                
                  d[tipo] = player[tipo]["punti"]
        
        
        
        sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
        addd = dict()
        for i in sort_orders:
            
            addd[i[0]] = i[1]
        x = 1
        for tipo in addd:
            
            v += f"{x}° {tipo} - {addd[tipo]} punti!\n"
            x += 1
            if x > 50:
                break
        message.reply(v)
        
    else:
        ricerca = message.command[1]
        if ricerca == "perdenti":
            v = "Top dei migliori a perdere!\n"
            d = dict()
            for tipo in player:
                
                d[tipo] = player[tipo]["punti"]
            
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=False)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - punti {addd[tipo]}!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
            
        if ricerca == "livello":
            v = "Top livelli!\n"
            d = dict()
            for tipo in player:
                
                d[tipo] = player[tipo]["livello"]
            
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - lv {addd[tipo]}!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
            
        if ricerca == "inviti":
            v = "Top invitati!\n"
            d = dict()
            for tipo in player:
                
                d[tipo] = player[tipo]["inviti"]['numero']
            
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} inviti!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
            
        if ricerca == "zaino":
            v = "Top zaino differenti!\n"
            d = dict()
            for tipo in player:
                
                d[tipo] = len(player[tipo]["zaino"])
            
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} item differenti!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
        if ricerca == "gloria":
            v = "Top gloria!\n"
            d = dict()
            for tipo in player:
                try:

                    d[tipo] = player[tipo]["gloria"]
                except:
                    d[tipo] = 0
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} punti!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
        
        if ricerca == "win":
            
            v = "Top vinte!\n"
            d = dict()
            for tipo in player:
                try:

                    d[tipo] = player[tipo]["w"]
                except:
                    d[tipo] = 0
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} vinte!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
            
        if ricerca == "lose":
            
            v = "Top perse!\n"
            d = dict()
            for tipo in player:
                try:

                    d[tipo] = player[tipo]["l"]
                except:
                    d[tipo] = 0
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} perse!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
        if ricerca == "boss":
            
            
            v = "Top vittorie vs Boss!\n"
            d = dict()
            for tipo in player:
                value = 0
                if "boss" in player[tipo]:
                    
                    for bossin in player[tipo]["boss"]:
                        value += player[tipo]["boss"][bossin]
                    
                d[tipo] = value
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} vinte!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
                 
        if ricerca == "clan":
            
            v = "Top clan!\n"
            d = dict()
            for tipo in clan:
                
                try:

                    d[tipo] = clan[tipo]["punti"]
                except:
                    d[tipo] = 0
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} punti!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)
            
        if ricerca == "oggi":
            
            v = "Top sfide oggi!\n"
            d = dict()
            for tipo in player:
                
                try:

                    d[tipo] = player[tipo]["oggi"]
                except:
                    d[tipo] = 0
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} sfide!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v)   
            
        if ricerca == "sfide":
            
            v = "Top sfide fatte!\n"
            d = dict()
            for tipo in player:
                
                try:

                    d[tipo] = player[tipo]["totali"]
                except:
                    d[tipo] = 0
            
            
            sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
            addd = dict()
            for i in sort_orders:
                
                addd[i[0]] = i[1]
            x = 1
            for tipo in addd:
                
                v += f"{x}° {tipo} - {addd[tipo]} sfide complessive!\n"
                x += 1
                if x > 50:
                    break
            message.reply(v) 
            
        else:
            message.reply("/top accetta solo `livello`,`zaino`,`oggi,`sfide`,`win`,`lose`,`boss`,`clan`,`inviti`, `perdenti` o `gloria`")
