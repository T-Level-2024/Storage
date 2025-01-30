def can_see_stage(seats):
    row_len = len(seats[0])
    for i in range(0, row_len):
        vlist = []
        for item in seats:
            vlist.append(item[i])
        print(vlist)
        for x in range(len(vlist)-1):
            print(vlist[x], vlist[x+1])
            if vlist[x] >= vlist[x+1]:
                return False
    else:
        return True
