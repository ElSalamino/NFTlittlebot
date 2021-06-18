
@app.on_message(filters.command(["pat","pat@NFTlittlebot"]) & ~filters.user(bannati))
def pat(client, message):
    username = message.from_user.username
    if "pet" in player[username]:
        if 'ricerca' not in player[username] or player[username]["ricerca"] == None:
            if message.chat.id == -1001476172565:
                pass
            else:
                
                pet = player[username]["pet"]
                try:
                    other_time = last_pat[username]
                except:
                    other_time = 1
                                            
                now = time.time()
                                        
                elapsed = now - other_time
                
                if elapsed > 10:
                    if "NomePet" in player[username]:
                        nome = player[username]["NomePet"] + ", "
                    else:
                        nome = ""
                    last_pat[username] = now
                    message.reply(f"Fai pat pat a {nome}{pet.lower()}, lui si che è un bravo animaletto!\n__Il tuo animaletto si sente più amato__")
                    try:
                        player[username]["varie"]["pat"] += 1
                    except:
                        player[username]["varie"]["pat"] = 1
                        
                    if player[username]["varie"]["pat"] == 666:
                        tipo = random.choice(["leddissima","velocissima"])
                        player[username]["zaino"][f"Una ventolina {tipo}"] = 1
                        message.reply("Wow!\nGrazie a te il server è forse 1° più caldo!")
                else:
                    message.reply("Piano piano!\nSennò lo rompi!")
        else:
            tipo = random.choice(list(player))
            message.reply(f"Vorresti fare pat pat al tuo animaletto, ma non c'è più...\nSe vuoi puoi pattare {tipo} al suo posto!")

    else:
        message.reply(f"Non hai un animaletto da coccolare")
