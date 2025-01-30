def shift_sentence(txt):
    txt = txt.split(" ")
    txt.reverse()
    for i in range(len(txt)):
        txt[i] = list(txt[i])
    for i in range(len(txt)-1):
        txt[i][0], txt[i+1][0] = txt[i+1][0], txt[i][0]
        txt[i] = "".join(txt[i])
    txt.reverse()
    txt[0] = "".join(txt[0])
    return " ".join(txt)
