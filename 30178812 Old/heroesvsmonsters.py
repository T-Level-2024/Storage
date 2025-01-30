def battle(data):
    pATK, mATK = (data["pATT"]*2)-data["mDEF"], (data["mATT"]*2)-data["pDEF"]
    mATKh = mATK/2
    print("Player attack: "+str(pATK)+"\n"
          "Monster attack: "+str(mATK)+"\n"
          "Monster attack (heal): "+str(mATKh)+"\n")
    roundcounter = 0
    heal = False
    while data["pHP"]>0 and data["mHP"]>0:
        print("Round {}".format(roundcounter+1))
        if heal:
            heal = False
        if data["pHP"] < 10 and data["pPOT"] > 0:
            heal, data["pPOT"], data["pHP"] = True, data["pPOT"]-1, data["pHP"]+10
            print("Hero heals!")
        else:
            print("Hero deals {} damage!".format(pATK))
            data["mHP"] -= pATK
            print("Monster health: "+str(data["mHP"]))
        if heal:
            print("Monster deals {} damage!".format(mATKh))
            data["pHP"] -= mATKh
            print("Hero health: "+str(data["pHP"]))
        else:
            print("Monster deals {} damage!".format(mATK))
            data["pHP"] -= mATK
            print("Hero health: "+str(data["pHP"]))
        roundcounter += 1
        continue
    return "Victory in {} rounds".format(roundcounter) if data["mHP"] <= 0 else "Game Over in {} rounds".format(roundcounter)
