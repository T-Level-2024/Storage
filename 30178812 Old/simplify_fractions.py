def simplify(txt):
    old_txt = txt
    txt = txt.split("/")
    txt[0], txt[1] = int(txt[0]), int(txt[1])
    return old_txt if not (txt[1]/2).is_integer() or not ((txt[0]))
