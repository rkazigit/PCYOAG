import random
from backbone import * #custom mod

player_state = {
    "name": "",
    "money": 100,
    "health": 100,
    "won_blackjack": False,
    "crashed_car": False,
    "met_celebrity": False,
    "backstage_pass": False,
    "invited_to_concert": False,
    "ending": None,
    "secret": False
}

#intro - flight layover, welcome to vegas,
def introduction():
    clear_console()
    vegas_art()
    typewriter("Your flight was supposed to be a short layover.")
    typewriter("Five days later, you are standing in Las Vegas with no real plan.")
    typewriter("The airline says sorry. Vegas says welcome.")
    typewriter("You feel like this might change your life. Probably not for the better.")
    pause(3)
    
#day 1 - f1 race
def day_one():
    clear_console()
    f1_art()
    typewriter("Day 1: The Vegas strip shakes as F1 engines fly past you.")
    typewriter("A promoter mistakes your confidence for experience.")
    choice = input("Test drive a supercar? (yes/no): ").lower()
    
    if choice == "yes":
        crash = random.randint(1, 10)
        if crash > 6:
            typewriter("You floor it. Pedal to the metal. The crowd gasps.")
            typewriter("CRASH. You realize you are NOT a professional by any means and apologize to the palm tree you just hit.")
            player_state["health"] -= 40 #this can lead to hospital ending too
            player_state["crashed_car"] = True
        else:
            typewriter("You drive like a professional. You WISH your Honda Civic could maneuver like this...")
    else:
        typewriter("You decide to admire the cars from the viewing deck like everyone else.")
        
    pause(3)
    
#day 2 - casino, blackjack
def day_two():
    clear_console()
    casino_art()
    typewriter("Day 2: The casino lights blink like they are judging you.")
    choice = input("Sit at the blackjack table? (yes/no): ").lower()
    
    if choice == "yes":
        net_change = blackjack_game(player_state["name"], player_state["money"])
        player_state["money"] += net_change
        
        if net_change > 0:
            player_state["won_blackjack"] = True
        elif net_change < 0:
            typewriter("You step away from the table lighter than before.")
        else:
            typewriter("You walk away even. Rare Vegas moment.")
    else:
        typewriter("You walk past the tables like someone who knows their limits.")
        typewriter("This character development will not last buddy.")
    
    pause(3)
    
#day 3 - food
def day_three():
    clear_console()
    typewriter("Day 3: Your stomach and your wallet have a serious meeting.")
    
    if player_state["won_blackjack"]:
        typewriter("You book a table at Carbone. The lighting is warm and expensive 🤑 .")
        pause(2)
        #little extra food allergy random chance but leads to hospital ending
        allergy = random.randint(1, 10)
        if allergy > 8:
            typewriter("One bite in, your body decides luxury is a mistake 🤢 .")
            player_state["health"] -= 60
            player_state["health"] = max(player_state["health"], 0)
        else:
            typewriter("The food is phenomenal. So much so that you consider becoming a food influencer.")
            typewriter("Across the room, you spot your favourite singer 👀 .")
            typewriter("You lock eyes. They awkwardly wave. You feel embarrassed.")
            typewriter("They slowly start walking over to you.")
            typewriter("You strike up a conversation and secure an invite to their concert tomorrow.")
            player_state["invited_to_concert"] = True

    else: 
        typewriter("You pick a modest place to eat.")
        typewriter("They hand you a physical menu and not a QR code. You respect that.")
        typewriter("You hear tourists arguing about directions and see a pigeon stealing someone's fries.")
        typewriter("You mind your business and enjoy your food.")
        player_state["invited_to_concert"] = False
        
    pause(3)
    
#day 4 - concert
def day_four():
    clear_console()
    concert_art()
    typewriter("Day 4: The concert lights up the night.")
    
    if player_state["invited_to_concert"]:
        typewriter("You arrive with a private invite. Security treats you like you matter.")
        typewriter("Backstage is chaos, but the good kind.")
        typewriter("Your favourite singer remembers you and thanks you for coming.")
        player_state["met_celebrity"] = True
    else:
        find_pass = random.choice([True, False]) #tool - a backstage pass
        
        if find_pass:
            typewriter("You spot a backstage pass on the floor near the entrance.")
            take = input("Pick it up? (yes/no): ").lower()
            if take == "yes":
                typewriter("You walk backstage with undeserved confidence.")
                typewriter("Somehow, it works. Vegas respects boldness.")
                typewriter("You meet your favourite singer and get an autograph.")
                player_state["met_celebrity"] = True
                player_state["backstage_pass"] = True
            else:
                typewriter("You leave it there. You enjoy the concert from the crowd.")
        else:
            typewriter("No backstage pass today.")
            typewriter("You scream the lyrics from the crowd like everyone else.")
    
    pause(3)
    
#day 5 - topgolf and heli ride
def day_five():
    clear_console()
    helicopter_art()
    typewriter("Day 5: You meet some strangers at a Topgolf overlooking the city.")
    typewriter("You become good friends with them while playing together.")
    typewriter("As the sun starts to set, someone offers you a helicopter ride since it's your last day.")
    typewriter("This feels like a bad idea. You do it anyway.")
    
    #randomness
    malfunction = random.randint(1, 12)
    secret_roll = random.randint(1, 10)

    if player_state["health"] <= 0:
        player_state["ending"] = "hospital"

    elif malfunction > 9:
        player_state["ending"] = "crash"

    elif (
        player_state["won_blackjack"]
        and player_state["met_celebrity"]
        and secret_roll >= 8
    ):
        player_state["ending"] = "secret"

    elif player_state["met_celebrity"]:
        player_state["ending"] = "celebrity"

    elif player_state["money"] >= 400:
        player_state["ending"] = "wealthy"

    else:
        player_state["ending"] = "safe"

    pause(3)

#final endings/outcomes
def ending():
    clear_console()
    name = player_state["name"]
    
    typewriter("FINAL OUTCOME\n", delay=0.02, line_pause=0.5)
    pause(2)
    
    ending_type = player_state.get("ending")

    if ending_type is None:
        ending_type = "safe"
    
    #secret ending (10% chance)
    if player_state["ending"] == "secret":
        typewriter(color_text(f"{name}, your helicopter takes off from a nearby helipad.", Colors.MAGENTA))
        typewriter("Below you, the neon lights of Vegas flicker on one by one.")
        pause(1.5)
        typewriter("As you float over the Vegas Strip, your phone buzzes.")
        typewriter("It's a notification from your airline!")
        typewriter("Your delayed flight will be boarding early due to a schedule change...")
        pause(1.5)
        typewriter("Your heart drops. Of course Vegas gave you everything... then takes your timing.")
        typewriter("The pilot overhears this and offers you to ride along in his private jet flight tomorrow.")
        typewriter("You breathe a sigh of relief and head back to your hotel while watching the city fade beneath you.")
        typewriter("You realize how fast this accidental adventure passed.")
        pause(1.5)
        typewriter(color_text("Secret ending unlocked!", Colors.GREEN))
    
    #heli crash ending    
    elif player_state["ending"] == "crash":
        typewriter(color_text("The helicopter shakes violently as the city spins below.", Colors.RED))
        typewriter("You close your eyes and think about how all of this happened during a layover.")
        typewriter("Everything fades to black. TO BE CONTINUED...")

    #hospital ending
    elif player_state["health"] <= 0:
        typewriter(color_text(f"{name}, you wake up in a hospital bed.", Colors.RED))
        typewriter("Haha sucker. Vegas got the last laugh. The nurse reminds you that your flight leaves tomorrow.")
        
    #celebrity ending
    elif player_state["met_celebrity"]:
        typewriter(color_text(f"{name}, you return to your hotel with stories NOBODY will believe. Make sure to keep the stories to yourself buddy.", Colors.GREEN))
        typewriter("You remember your flight is tomorrow and think about how all of this happened during a layover.")
    
    #wealthy ending
    elif player_state["money"] >= 400 and not player_state["met_celebrity"]:
        typewriter(color_text(f"{name}, you leave Vegas richer and slightly wiser.", Colors.GREEN))
        typewriter("You remember your flight is tomorrow and think about how all of this happened during a layover.")
    
    #default ending
    else:
        typewriter(color_text(f"{name}, you limp back to your hotel with memories and regret.", Colors.YELLOW))
        typewriter("You check your phone. You remember your flight leaves tomorrow and that all of this happened during a layover.")
        
    pause(2)
    typewriter("\nThanks for playing. Vegas will remember you. 🎰")


def main():
    clear_console()
    vegas_art()
    player_state["name"] = input("Enter your name, traveler: ")

    skip = input("Skip introduction? (yes/no): ").lower()
    if skip != "yes":
        introduction()

    day_one()
    day_two()
    day_three()
    day_four()
    day_five()
    ending()


if __name__ == "__main__":
    main()
