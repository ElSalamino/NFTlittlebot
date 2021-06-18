def take_boss(lista,numero):
    copi = copy.deepcopy(list(lista))
    out = list()
    for x in range(numero):
        a = random.choice(copi)
        out.append(a)
        copi.remove(a)
    return(out)

