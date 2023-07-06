# imporing needed package
import time
import random


def printwait(phase, s=1):
    print(phase)
    time.sleep(s)


want_to_play = True


# dublcated story lines
def searching_for_inn():
    printwait("*turning on car engine*")
    printwait("You: unlucky me i don't have a map for this town")
    printwait("10m later")
    printwait("You: i think im lost")
    printwait("You: There is no one in the streets i guess i cant ask anybody")
    printwait("*After looking for an hour You finaly found one*")
    printwait("You: Finally i found an old one but seems good for 2 nights")
    printwait("You: If i still alive utill tomorrow")


def talking_to_the_mayor():
    printwait("You: Well, i came here mainly to discover the legand")
    printwait("Mayor: What legand?")
    printwait("You: The wolfman")
    printwait("Mayor: Probably you won't belive me but this is not legand")
    printwait("Mayor: it's truth and i faced him before")
    printwait("Mayor: the legand says a cursed man turned into wolf")
    printwait("Mayor: He started to infect people around him")
    printwait("Mayor: every full moon all the infected men turn into wolfs")
    printwait("You: So it's true")
    printwait("You: Is there any way to heal them")
    printwait("Mayor: as far as i know there is no cure for this curse")
    printwait("Mayor: Once you are bitten there is no going back")
    printwait("You: Great i think i will explore the forest tomomorrow")
    printwait("You: Maybe if i'm luckey i will kill him")
    printwait("Mayor: Do whatever you want but i have to warn you")
    printwait("Mayor:  If you got infected i will kill you")
    printwait("You: Deal!")


def won():
    printwait("*The wolf is dying he is slowoly turning into human again*")
    if sec_choice == "girl":
        printwait("You: It's done mayor!!")
        printwait("You: Wait he doesn't look like the mayor!")
        printwait("You!!")
        printwait("The wolf is now dead and you discoverd his identety")
        printwait("The mayor's daughter")
    else:
        printwait("You: Now for the truth")
        printwait("You: Who are you!?")
        printwait("*the monestor slowoly turning into human*")
        printwait("You: So this is you!")
        printwait("The mayor's daughter")


# Boss fight
def boss_fight():
    win = random.randint(1, 100)
    print("You: (Seeing the monster for the first time):", end="")
    printwait(" Wow he looks so angry")
    if gear_choice in ["A", "a"]:
        printwait("You (Slowly getting out your gun): I just want a clear shot")
        printwait("You: I have to follow a strategy in order to shot him")
        if mushroom == 1:
            printwait("You: The hunter can help too")
            printwait("You: I have 2 ideas I can")
            printwait("""
            Choice (A): Face the monster in the face and shot
            Choice (B): Give the gun to the hunter and make distraction
                        to let the hunter have a clear shot
                      """)
            printwait("Note: Every strategy has diffrent win rate")
            strategy = input("so what is Your choice (A-B): ")

            while strategy not in ["A", "a", "B", "b"]:
                print("Your choice is invaild please choose vaild option")
                strategy = input("so what is Your choice (A-B): ")

            if strategy in ["A", "a"]:
                printwait("You: Okay hunter I think I Will face him")
                printwait("You: I think I have a chance of 30% this way")
                printwait("Hunter: Okay I will watch you from a distance")
                printwait("You: Wish me luck")
                printwait("*seeing the monster coming*")
                printwait("*You shoot him while he is running*")
                printwait("*You missed A shot! 2 shots*")
                printwait("He is getting closer!")

                if win <= 30:
                    printwait("*That final shot killed him*")
                    printwait("Hunter: You did it!")
                    won()
                    return True
                else:
                    print("*A big jump from the wolf he is now in ", end="")
                    printwait("front of you*")
                    return False

            if strategy in ["B", "b"]:
                printwait("you: Here is the gun... take it")
                printwait("Hunter: And what will you do?")
                printwait("You: I will distract him while you get a clear shot")
                printwait("I think I have a chance of 80% this way")
                printwait("Hunter: Okay Good luck")
                printwait("*The hunter get a little far waiting for you*")
                printwait("*You start run near the hunter to give him chance*")

                if win <= 80:
                    printwait("*The monster get close enough to the hunter*")
                    printwait("*The hunter shot him*")
                    printwait("You: You did it!")
                    printwait("Hunter: That was easy")
                    won()
                    return True
                else:
                    printwait("*The wolf notices the hunter*")
                    print("*He changed his direction to avoid ", end="")
                    printwait("the shot from the hunter*")
                    print("*A big jump from the wolf he is now in ", end="")
                    printwait("front of you*")
                    return False
        else:
            printwait("You: I have 2 ideas I can")
            printwait("""
            Choice (A): Face the monster in the face and shot
            Choice (B): Run and try to shot from a distance
                      """)
            printwait("Note: Every strategy has diffrent win rate")
            strategy = input("so what is Your choice (A-B): ")

            while strategy not in ["A", "a", "B", "b"]:
                print("Your choice is invaild please choose vaild option")
                strategy = input("so what is Your choice (A-B): ")

            if strategy in ["A", "a"]:
                printwait("You: I think I Will face him")
                printwait("You: I think I have a chance of 30% this way")
                printwait("*seeing the monster coming*")
                printwait("*You shoot him while he is running*")
                printwait("*You missed A shot! 2 shots*")
                printwait("*He is getting closer!*")

                if win <= 30:
                    printwait("*That final shot killed him*")
                    printwait("You: I did it!")
                    won()
                    return True
                else:
                    print("*A big jump from the wolf he is now in ", end="")
                    printwait("front of you*")
                    return False

            if strategy in ["B", "b"]:
                printwait("You: I think I will run untill I get a clear shot")
                printwait("I think I have a chance of 65% this way")
                printwait("*You start run in the oposite way to get a chance*")

                win = random.randint(1, 100)
                if win <= 80:
                    print("*You find a big tree and had the idea ", end="")
                    print("to get around it and shot from the ", end="")
                    printwait("other edge of the tree*")
                    printwait("*You did it you are now behind the tree*")
                    printwait("you: He is close enough I think it's time")
                    printwait("*You left the tree from the other side*")
                    printwait("*2 shots and its over*")
                    won()
                    return True
                else:
                    printwait("*The wolf notices the gun in your hand*")
                    printwait("*The wolf run in a crooked way*")
                    print("*A big jump from the wolf he is now in ", end="")
                    printwait("front of you*")
                    return False

    elif gear_choice in ["B", "b"]:
        printwait("You (getting out your sword): I have to face him")
        printwait("You: There is only way to do this")
        printwait("You: Facing him and stab him")

        if mushroom == 1:
            printwait("Hunter: But how?")
            printwait("You: I have a plan")
            printwait("You: I will face him and you will throw rocks at him")
            printwait("You: This will annoy him enough to give me uppper hand")
            printwait("I think I have a chance of 85% this way")
            printwait("Hunter: Okay good luck")
            printwait("*You drink that energy potion and get your sword ready*")
            printwait("*The wolf is running towards you*")
            printwait("*He didn't notice the hunter*")
            if win <= 85:
                printwait("*You avoid his jump*")
                printwait("*The hunter start trowing rocks*")
                printwait("*He is now distracted*")
                printwait("*With a big jump you are in front of him and...*")
                printwait("*You stabbed him*")
                printwait("Hunter: You did it")
                won()
                return True
            else:
                printwait("*You tried to avoid his jump but you couldn't*")
                printwait("*You got hurt*")
                printwait("You (Eating the mushroom): Not a big deal!")
                print("*A big jump from the wolf he is now in ", end="")
                printwait("front of you*")
                printwait("*You could't avoid his jump beacuase you are hurt*")
                return False
        else:
            printwait("I think I have a chance of 75% this way")
            printwait("*You drink that energy potion and get your sword ready*")
            printwait("*The wolf is running towards you*")
            if win <= 75:
                printwait("*You avoid his jump*")
                printwait("*With a big jump you are in front of him and...*")
                printwait("*You stabbed him*")
                printwait("You: I did it")
                won()
                return True
            else:
                printwait("*You tried to avoid his jump but you couldn't*")
                printwait("*You got hurt*")
                printwait("You: I'm infected now")
                printwait("You: I wil try to kill him at least")
                print("*Because of your wounds you couldn't avoid ", end="")
                printwait("his next attake*")
                return False


# legand_of_wolfman (only at first game)
printwait("In the dark forest of Ravenwood")
printwait("a legend has been passed down for generations")
printwait("It is said that on nights when the moon is full")
printwait("a man transforms into a wolf, cursed by an ancient magic")
printwait("This creature, known as the Wolf Man, roams the woods")
printwait("hunting for prey and howling at the moon")
printwait("Many have tried to capture or kill the Wolf Man")
printwait("but none have succeeded")
printwait("You can't help but wonder if the legend is true")
printwait("and if you'll encounter the Wolf Man on your journey")
print("=================================================================")


# Main Game
while want_to_play is True:
    # Reseting varuables
    sec_choice = None
    mushroom = None
    first_choice = None
    gear_choice = None
    kill_hunter = None

    # Night before the full moon
    printwait("*You reached Ravenwood in the night before the full moon*")
    printwait("You: Hmmmmm so what should I do tonight")
    printwait("I have 3 choices you can")
    print("""
              Choice (A): Go and find an inn to sleep and rest
              Choice (B): Ask the village's mayor about the wolfman legand
              Choice (C): Explore the forest now
              """)
    printwait("Note: Your choice may change the results of the story")

    first_choice = input("so what is Your choice (A-B-C): ")

    while first_choice not in ["A", "a", "B", "b", "C", "c"]:
        print("Your choice is invaild please choose vaild option")
        first_choice = input("so what is Your choice (A-B-C): ")

    if first_choice in ["A", "a"]:
        print("You: I guess I will find an inn to sleep", end="")
        printwait(" i will talk to the mayour later")

        searching_for_inn()
        printwait("*Next day.......*")
        printwait("You: I guess I will talk to the mayor of the town")
        printwait("*reaching the townhall*")
        printwait("You: Hello sir honor to meet you")
        printwait("Mayor: Hello son")
        printwait("Mayor: Is there any way I can help you")
        talking_to_the_mayor()

    elif first_choice in ["B", "b"]:
        printwait("You: I guess I will talk to the mayor of the town")
        printwait("*reaching the townhall*")
        printwait("You: Hello sir honor to meet you")
        printwait("Mayor: Hello son")
        printwait("Mayor: Is there any way I can help you")
        talking_to_the_mayor()
        printwait("You: I guess I will find an inn to sleep")
        printwait("You: I will talk to the mayour later")
        searching_for_inn()
        printwait("*Next day.......*")

    elif first_choice in ["C", "c"]:
        printwait("You: I guess I will check the forest now")
        printwait("You: maybe its safe tonight for me")
        printwait("You: I will grab my flash light anyway")
        printwait("*Driving the car to the edge of the forest*")
        printwait("You: Doesn't seem that spooky")
        printwait("*Entering the Forest.......*")
        mushroom = random.randint(0, 1)

        if mushroom == 1:
            printwait("while exploring you found a glowing mushroom")
            printwait("You: Is that even possible")
            printwait("You: How does that mushroom glow?")
            printwait("You: Anyway seems not harmfull i will check it later")
            printwait("*puts it in your bag*")
        choices = ["girl", "hunters"]
        sec_choice = random.choice(choices)

        if sec_choice == "girl":
            printwait("*a branch crashs*")
            print("You: (pointg your flash light", end="")
            printwait(" to the sound source) who is there?")
            printwait("Girl: Don't shoot please i'm not harmful")
            printwait("You: Shoot?")
            printwait("You: Why would i shoot you?")
            printwait("Girl: I thought you are one of the hunters")
            printwait("You: Hunters?")
            print("You: What are the hunters doing here", end="")
            printwait(" i thought it is not safe in the foerst")
            printwait("Girl: Why you think its not safe?")
            printwait("You: I heard about the legand of the wolfman")
            printwait("You: In fact thats why i'm here")
            printwait("You: you haven't told me yet")
            printwait("You: What are you doing in the forest by this time")
            printwait("Girl: I got lost and i need help")
            printwait("You: *thinking for a moment*")
            printwait("You: okay let's get u home my car isn't far from here")
            print("*in the way to her home", end="")
            printwait(" you knew she is the mayor's daughter*")
            print("You to yourself: good chance to", end="")
            printwait(" ask the mayor about the legand now")
            printwait("*After a while......*")
            printwait("Mayor: thanks for saving my daughter son")
            printwait("Mayor: I owe you a favor")
            talking_to_the_mayor()
            searching_for_inn()
            printwait("*Next day.......*")

        elif sec_choice == "hunters":
            printwait("*Hear a near noise*")
            printwait("You: Who is there!")
            printwait("*A weird gang come to check that noise*")
            print("You: Who are you and what are you", end="")
            printwait(" doing in this dangerous night?")
            printwait("Stange man: Out of your business")
            print("Strange man: And it's better", end="")
            printwait(" for you to get out from this forest")
            printwait("You: Why?")
            printwait("Strange man: none of your business not get out of here")
            printwait("Strange man: before i force u do leave")
            printwait("*You turning around to get back to your car*")
            printwait("You to your self: I guess they are hunters")
            printwait("You: Maybe they are setting some traps for the wolf")
            printwait("You: it's enough for today")
            print("", end="You: I guess I will find an inn")
            printwait(" to sleep i will talk to the mayour later")
            searching_for_inn()
            printwait("*Next day.......*")
            printwait("You: I guess I will talk to the mayor of the town")
            printwait("*reaching the townhall*")
            printwait("You: Hello sir honor to meet you")
            printwait("Mayor: Hello son")
            printwait("Mayor: Is there any way I can help you")
            talking_to_the_mayor()

    printwait("You: I think it's time to get ready")
    printwait("You: I saw a gun shop in my way here")
    printwait("*Driving Your car to the gun shop*")
    printwait("You: Hello sir")
    printwait("Seller: How can i help?")
    printwait("You: i want to buy some gear")
    printwait("Seller: pick whatever you want and meet me in the cashier")
    printwait("You to your self: My money is limited i think i will buy armor")
    printwait("You: But what else?")
    printwait("""
              Choice (A): Gun (Seems good if you have a clear shot)
              Choice (B): Sword & potions (Good for direct attaks)
              """)

    gear_choice = input("So what should i buy (A-B): ")

    while gear_choice not in ["A", "a", "B", "b"]:
        print("Your choice is invaild please choose vaild option")
        gear_choice = input("So what should i buy (A-B): ")
    if gear_choice in ["A", "a"]:
        printwait("You: I guess I will buy this gun too")
    elif gear_choice in ["B", "b"]:
        printwait("You: I guess I will buy this sword with this energy potion")

    printwait("You: I think i'm ready now")
    printwait("?: Hey sir!")
    printwait("*Turns back to see who is calling*")

    if sec_choice == "girl":
        printwait("You: ohh nice to see you again")
        printwait("You: What brings u here?")
        printwait("Girl: I knew u would be here bying some gears")
        printwait("Girl: I want to thank you about last night")
        printwait("Girl: Also I want to tell you something")
        printwait("Girl: Something may help you tonight")
        printwait("You: what is that?")
        printwait("Girl: I know who is the wolf")
        printwait("Girl: It's my dad")
        printwait("You: Are you sure?")
        printwait("Girl: Yes i'm and i hope this helps you")

    else:
        printwait("You: Hello?")
        printwait("Girl: I'm the mayor's daughter i heard you yesterday")
        printwait("Girl: I know you will explore the forest tonight")
        printwait("Girl: In order too find the monester")
        printwait("You: Yes that's right")
        printwait("Girl: Okay sorry for bothering you be carefull")
    printwait("Girl: good luck")
    printwait("You: Okay bye")
    # Entering The Forest
    printwait("*In the night you went to the forest*")
    printwait("You: I didn't thinked about that will I fight him if I met him?")
    printwait("You: I guess I will although it seems difficult")
    printwait("*You hear screams and gunshot far away*")
    printwait("*You head for the direction of the screams*")
    printwait("You: maybe i should hurry beofore an......")
    printwait("You: What happend here??!")
    print("*You found the place coverd in blood", end="")
    printwait(" and a dead dismembered corpse*")
    printwait("You: Looks like i'm too late")
    printwait("?: Help!")
    print("You(looking for the caller):", end="")
    printwait(" thanks god there are alives here")
    printwait("You: You are bleeding!")

    if sec_choice == "hunters":
        printwait("You: Wait aren't you that hunter i met yesterday")
    printwait("You: What happend?")
    printwait("Hunter: The monster attaked us")
    printwait("Hunter: I think I got infected")
    printwait("Hunter: I wish i have one of these mushrooms")

    if mushroom == 1:
        printwait("You: Are you talking about these glowing mushrooms")
        printwait("Hunter: Yes Yes!")
        printwait("Hunter: Do you have one of them?")
        printwait("You: Yes i do what do you use them for")
        print("Hunter: If you eat it directly after you got hurt by th", end="")
        printwait("is monster you will heal your self from this eternal curse")
        printwait("You: Lucky me I have one here you are")
        printwait("Hunter: Thank you now let's find this monster and kill him")
        printwait("*After a while.....")
        printwait("Hunter: I don't feel well")
        printwait("Hunter: I've already lost a lot of blood")
        printwait("Hunter: Better to hurry or leave it for the next month")
        printwait("You: Hold on the night is almost over")
        printwait("*The monster heard your argument and now ruuning to you*")
        printwait("You: Get ready he is here")

        if boss_fight():
            printwait("YOU WON")
            printwait("Game over")
            printwait("""
            Your Score:
                You killed the original monster                      --->  1
                You healed the hunter                                --->  1
                collaborated with the hunter to fight the monster    --->  1
                You discovered the identety of the original monster  --->  1
                Now you are sure the legand is True                  --->  1
                ------------------------------------------------------------
                Total Score                                          --->  5
                      """)

        else:
            printwait("YOU DIEAD")
            printwait("Game over")
            printwait("""
            Your Score:
                Didn't kill the original monste                      ---> -1
                You healed the hunter                                --->  1
                collaborated with the hunter to fight the monster    --->  1
                Didn't discover the identety of the original monster ---> -1
                Now you are sure the legand is True                  --->  1
                ------------------------------------------------------------
                Total Score                                          --->  1
                      """)

    else:
        printwait("You: What mushrooms?")
        printwait("Hunter: A glowing mysterious mushroom")
        print("Hunter: That plant have the ablity to ", end="")
        printwait("instantly heal you from this eternal curse")
        printwait("*Thinking for a while*")
        printwait("You to yourself: This man is cursed he can kill us all")
        printwait("You: I think i have two choices")
        printwait("""
                     Choice (A): Kill the hunter Immediately
                     Choice (B): Search for the monestor and deal with
                                 the hunter without killing him
                  """)

        kill_hunter = input("What should i do? (A-B): ")

        while kill_hunter not in ["A", "a", "B", "b"]:
            print("Your choice is invaild please choose vaild option")
            kill_hunter = input("What should i do? (A-B): ")

        if kill_hunter in ["A", "a"]:
            printwait("You to your self: I have to kill this guy Immediately")
            printwait("You: Sorry for doing that")
            printwait("Hunter: Wait!!")
            printwait("Hunter seeing you pulling your gun: Please no!")
            printwait("hunter: I won't hurt anyone I promise")
            printwait("You: I'm sorry")
            printwait("*Shoot him in the head*")
            printwait("You: I hope I made the right choice")
            printwait("*The monster heard your gunshot and now ruuning to you*")
            printwait("You: I think I'm ready for you now")
            if boss_fight():
                printwait("YOU WON")
                printwait("Game over")
                printwait("""
                Your Score:
                    You killed the original monster                      --->  1
                    You killed the hunter                                --->  1
                    You discovered the identety of the original monster  --->  1
                    Now you are sure the legand is True                  --->  1
                    ------------------------------------------------------------
                    Total Score                                          --->  4
                          """)
            else:
                printwait("YOU DIEAD")
                printwait("Game over")
                printwait("""
                Your Score:
                    You killed the hunter                                --->  1
                    Didn't kill the original monster                     ---> -1
                    Didn't discover the identety of the original monster ---> -1
                    Now you are sure the legand is True                  --->  1
                    ------------------------------------------------------------
                    Total Score                                          --->  0
                          """)

        elif kill_hunter in ["B", "b"]:
            printwait("You to your self: Seems stupid idea")
            printwait("You: Come on Let's find That monster")
            printwait("Hunter: Yes let's do it!")
            printwait("*After a while...*")
            printwait("Hunter: I don't feel well")
            printwait("You: No No hold on!")
            printwait("Hunter: I can't control it!")
            printwait("*Hunter slowoly getting taller and hairy*")
            printwait("You: I have to run I can't help him!")
            printwait("*The hunter becomes full wolf he looks scary*")
            printwait("*A big jump from the wolf he is now in front of you*")
            printwait("YOU DIEAD")
            printwait("Game over")
            printwait("""
            Your Score:
                Died from the new wolf                               ---> -1
                Didn't kill the original monster                     ---> -1
                Didn't discover the identety of the original monster ---> -1
                Now you are sure the legand is True                  --->  1
                ------------------------------------------------------------
                Total Score                                          ---> -2
                      """)

    # Check if the player want to play again
    want_to_play_again_choice = input("Do you want to play again (y-n): ")
    while want_to_play_again_choice not in ["Y", "y", "N", "n"]:
        print("Your choice is invaild please choose vaild option")
        want_to_play_again_choice = input("Do you want to play again (y-n): ")
    if want_to_play_again_choice in ["y", "Y"]:
        want_to_play = True
    elif want_to_play_again_choice in ["n", "N"]:
        want_to_play = False
