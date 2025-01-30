import math, random, sys, time
poketutorlist = [["Andrew", 98, 0.4], ["Linda", 106, 0.4], ["Graham", 101, 0.8], ["Phil", 304, 0.4], ["Nigel", 416, 0.3], ["Serban", 414, 0.5], ["Andy", 708, 0.1], ["Dominic", 803, 0.5]]
pokeballs = [3, 0, 0]
credits = 0
class PokeTutor:
    def __init__(self, data):
        self.name, self.flee_rate, self.cp = data[0].strip(), data[1], random.uniform(data[2]*10, 100)/10



      
while True:
    total = pokeballs[0]+pokeballs[1]+pokeballs[2]
    if total == 0 and credits < 5:
        pokeballs[0] = 1
        print("__________\n"
              "Oh no! You ran out of pokeballs.\n"
              "Here is a complimentary pokeball.\n"
              "STANDARD Pokeball +1!"
              "\n"
              "__________")
    print("__________\n"
          "Menu\n"
          "\n"
          "Search for a PokeTutor\n"
          "Visit a PokeStop\n"
          "Exit\n"
          "\n"
          "__________")
    X = False
    while X == False:
        if X == True:
            continue
        user = input()
        if user == ("Search for a PokeTutor" or "PokeTutor"):
            tutor = PokeTutor(random.choice(poketutorlist))
            total = pokeballs[0]+pokeballs[1]+pokeballs[2]
            if total == 0:
                print("__________\n"
                      "You do not have any Pokeballs!\n"
                      "Buy some more from the PokeStop\n"
                      "__________")
                continue
            print("__________\n"
                  "Tutor found: "+tutor.name+", CP: "+str(math.ceil(tutor.cp))+"\n"
                  "\n"
                  "__________")
            while True:
                total = pokeballs[0]+pokeballs[1]+pokeballs[2]
                if total == 0:
                    print("__________\n"
                          "You have ran out of pokeballs to throw!\n"
                          "\n"
                          "__________")
                    X = True
                    break
                user = input("__________\n"
                             "Choose a ball to throw:\n"
                             "STANDARD ("+str(pokeballs[0])+")\n"
                             "GREAT ("+str(pokeballs[1])+")\n"
                             "ULTRA ("+str(pokeballs[2])+")\n"
                             "__________\n").strip()
                escape_chance, capture_base = tutor.flee_rate / 10.0, tutor.cp * 10.0
                if user == "STANDARD" and pokeballs[0] != 0:
                    ball = "STANDARD"
                    pokeballs[0] -= 1
                elif user == "GREAT" and pokeballs[1] != 0:
                    ball = "GREAT"
                    pokeballs[1] -= 1
                    escape_chance *= 0.66666667
                    capture_base *= 0.916666667
                elif user == "ULTRA" and pokeballs[2] != 0:
                    ball = "ULTRA"
                    pokeballs[2] -= 1
                    escape_chance *= 0.33333334
                    capture_base *= 0.83333333
                elif user == "Exit":
                    X = True
                    break
                else:
                    print("__________\n"
                          "You do not possess that pokeball!\n"
                          "\n"
                          "__________")
                    continue
                guess = random.uniform(0, 100)
                if guess <= escape_chance:
                    print("__________\n"
                          "The tutor has fled!\n"
                          "\n"
                          "__________")
                    X = True
                    break
                elif (100-capture_base)<=guess:
                    award = math.ceil(escape_chance+capture_base)
                    credits += award
                    print("__________\n"
                          "You caught "+tutor.name+"! Earned "+str(award)+"cr!\n"
                          "\n"
                          "__________")
                    x = True
                    break
                else:
                    print("__________\n"
                          "You missed!\n"
                          "\n"
                          "__________")
            X = True
            continue
        elif user == ("Visit a PokeStop" or "PokeStop"):
            print("__________\n"
                  "PokeStop\n"
                  "You have "+str(credits)+"cr.\n"
                  "\n"
                  "STANDARD ("+str(pokeballs[0])+"): 5cr\n"
                  "GREAT ("+str(pokeballs[1])+"): 15cr\n"
                  "ULTRA ("+str(pokeballs[2])+"): 30cr\n"
                  "\n"
                  "__________")
            while True:
                user = input()
                if user == "STANDARD":
                    if credits >= 5:
                        credits -= 5
                        pokeballs[0] += 1
                        print("__________\n"
                              "Thank you for your purchase\n"
                              "STANDARD Pokeball +1!\n"
                              "\n"
                              "__________")
                    else:
                        print("__________\n"
                              "You do not have enough credits to make this purchase\n"
                              "\n"
                              "__________")
                elif user == "GREAT":
                    if credits >= 15:
                        credits -= 15
                        pokeballs[1] += 1
                        print("__________\n"
                              "Thank you for your purchase\n"
                              "GREAT Pokeball +1!\n"
                              "\n"
                              "__________")
                    else:
                        print("__________\n"
                              "You do not have enough credits to make this purchase\n"
                              "\n"
                              "__________")
                elif user == "ULTRA":
                    if credits >= 30:
                        credits -= 30
                        pokeballs[2] += 1
                        print("__________\n"
                              "Thank you for your purchase\n"
                              "ULTRA Pokeball +1!\n"
                              "\n"
                              "__________")
                    else:
                        print("__________\n"
                              "You do not have enough credits to make this purchase\n"
                              "\n"
                              "__________")
                elif user == "Exit":
                    X = True
                    break
                else:
                    print("__________\n"
                          "That item is not available\n"
                          "\n"
                          "_________")
        elif user == "Exit":
            sys.exit()
        continue
