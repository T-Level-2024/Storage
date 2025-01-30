def tap_code(text):
    to = {"A":". .", "B":". ..", "C":". ...", "D":". ....", "E":". .....", "F":".. .", "G":".. ..", "H":".. ...", "I":".. ....", "J":".. .....", "K":". ...", "L":"... .", "M":"... ..", "N":"... ...", "O":"... ....", "P":"... .....", "Q":".... .", "R":".... ..", "S":".... ...", "T":".... ....", "U":".... .....", "V":"..... .", "W":"..... ..", "X":"..... ...", "Y":"..... ....", "Z":"..... ....."}
    fromv = {". .":"A", ". ..":"B", ". ...":"C", ". ....":"D", ". .....":"E", ".. .":"F", ".. ..":"G", ".. ...":"H", ".. ....":"I", ".. .....":"J", "... .":"L", "... ..":"M", "... ...":"N", "... ....":"O", "... .....":"P", ".... .":"Q", ".... ..":"R", ".... ...":"S", ".... ....":"T", ".... .....":"U", "..... .":"V", "..... ..":"W", "..... ...":"X", "..... ....":"Y", "..... .....":"Z"}
    if text[0] == ".":
        text, new = text.split(" "), []
        for i in range(0, len(text), 2):
            new.append(text[i]+" "+text[i+1])
        for i in range(len(new)):
            new[i] = fromv[new[i]]
        return "".join(new).lower()
    else:
        text = text.upper()
        text = list(text)
        for i in range(len(text)):
            text[i] = to[text[i]]
        return " ".join(text).lower()
