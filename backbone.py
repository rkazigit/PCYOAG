# imports
import os
import time
import sys
import random

# console and text
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

# was going too fast for the player to read so added delay and line pause
def typewriter(text, delay=0.02, line_pause=0.4):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if ord(char) > 0xFFFF:  # emojis print instantly
            time.sleep(0)
        else:
            time.sleep(delay)
    print()
    time.sleep(line_pause)

def pause(seconds=2.0):
    time.sleep(seconds)

# colours!
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

def color_text(text, color):
    return f"{color}{text}{Colors.RESET}"

# ascii art
def vegas_art():
    print(color_text(r"""
    _                                        
   ' )       )                               
    /      _/                                
   /    _/~____     ____     ____     ____   
  /  _/~ /'    )  /'    )  /'    )  /'    )
 /_/~  /(___,/' /'    /' /'    /'  '---,     
/~    (________(___,/(__(___,/(__(___,/      
                  /'                         
          /     /'                           
         (___,/'                             
            
       🎰  FIVE DAYS IN VEGAS 🎲
""", Colors.MAGENTA))

def f1_art():
    print(color_text(r"""
                                  
░██████████  ░██   
░██        ░████   
░██          ░██   
░█████████   ░██   
░██          ░██   
░██          ░██   
░██        ░██████ 
                       
 🏎️   VROOOOM
""", Colors.RED))

def casino_art():
    print(color_text(r"""
♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠
╔═══════════════╗
║   BLACKJACK   ║
╚═══════════════╝
♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠
""", Colors.YELLOW))

def concert_art():
    print(color_text(r"""
♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫
🎤  CONCERT TIME 🎤
♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫
""", Colors.MAGENTA))

def helicopter_art():
    print(color_text(r"""
---------------+---------------
          ___ /^^[___              _
         /|^+----+   |#___________//
       ( -+ |____|    ______-----+/
        ==_________--'            \
          ~_|___|__
""", Colors.CYAN))

# full blackjack game
def blackjack_game(player_name, player_money):
    casino_art()
    typewriter("You step into the casino. The air smells like perfume and bad decisions.")
    pause(1.5)

    # exchange money for chips
    while True:
        try:
            buy_in = int(input(f"How much do you want to exchange for chips? (You have ${player_money}): "))
            if 10 <= buy_in <= player_money:
                break
            else:
                typewriter("Enter a valid amount (minimum $10).")
        except ValueError:
            typewriter("Enter a number.")

    typewriter(f"You exchange ${buy_in} for chips and sit at the table.")
    pause(1.5)

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)

    def hand_value(hand):
        value = 0
        aces = 0
        for rank, suit in hand:
            if rank in ["J", "Q", "K"]:
                value += 10
            elif rank == "A":
                value += 11
                aces += 1
            else:
                value += int(rank)

        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def display_hand(hand, owner):
        cards = ", ".join([f"{r} of {s}" for r, s in hand])
        typewriter(f"{owner}'s hand: {cards} (value: {hand_value(hand)})")

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    display_hand(player_hand, player_name)
    typewriter(f"Dealer shows: {dealer_hand[0][0]} of {dealer_hand[0][1]}")
    pause(1.5)

    while hand_value(player_hand) < 21:
        choice = input("Hit or stand? (hit/stand): ").strip().lower()

        if choice not in ["hit", "stand"]:
            typewriter("Type exactly: hit or stand.")
            continue

        if choice == "hit":
            player_hand.append(deck.pop())
            display_hand(player_hand, player_name)
            pause(1)

            if hand_value(player_hand) > 21:
                typewriter(color_text("Bust! You went over 21.", Colors.RED))
                return -buy_in
        else:
            break

    typewriter("Dealer reveals their hand...")
    display_hand(dealer_hand, "Dealer")
    pause(1.5)

    while hand_value(dealer_hand) < 17:
        typewriter("Dealer hits.")
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand, "Dealer")
        pause(1.5)

    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    if dealer_total > 21 or player_total > dealer_total:
        typewriter(color_text("You win the hand! Chips slide your way.", Colors.GREEN))
        return buy_in
    elif player_total == dealer_total:
        typewriter(color_text("Push. You get your chips back.", Colors.YELLOW))
        return 0
    else:
        typewriter(color_text("Dealer wins. Your chips are gone.", Colors.RED))
        return -buy_in
