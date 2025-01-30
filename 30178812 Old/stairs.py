def stair(steps):
    if steps == 0:
        return "___"
    staircase = ["_|"]
    prior = "  "
    for i in range(steps-1):
        staircase.insert(0, prior + "_|\n")
        prior = "  " + prior
    staircase.insert(0, prior + "_\n")
    staircase = "".join(staircase)
    return staircase
