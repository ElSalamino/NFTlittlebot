def search(test_list,subs):
    rep = list()
    for a in test_list:
        parts = subs.split(" ")
        check = len(parts)
        value = 0
        for part in parts:
            if part.lower() in a.lower():
                value += 1
        if value >= check:
            rep.append(a)
    return rep
