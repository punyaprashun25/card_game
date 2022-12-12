import random
from os import system, name
from time import sleep
def grettings():
    print("\t    Welcome! In this mini game of war\n----------------------------------------------------------------")
    print("Instructions: the first person to win five cards is declared the victor.\nAfter each round you will have the chance to type “cheat” to automatically win the round.\nYou can only cheat once so use it wisely.")
    print("----------------------------------------------------------------")

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def card_value(card):
    if card=='K':
        return 13
    elif card=='Q':
        return 12
    elif card=='J':
        return 11
    elif card=='A':
        return 14
    else:
        return card

def start_game():
    # Variables start
    user = computer = [2,3,4,5,6,7,8,9,10,'K','Q','J','A']
    cheat = True
    user_score = 0
    computer_score = 0
    double_cheat = True
    round = 1
    # Variables end
    while (1):
        if round > 1:
            while 1:
                cheat_response = input("\nDo you like to cheat? (yes/no): ")
                if cheat_response == 'yes':
                    break
                elif cheat_response == 'no':
                    break
                else:
                    print("Please enter 'yes' or 'no'")
            if cheat_response.lower() == "yes":
                if cheat:
                    user_score += 1
                    cheat = False
                    user_card = user[random.randint(0, len(user)-1)]
                    computer_card = computer[random.randint(0, len(computer)-1)]
                    print("Suffling the Card.......")
                    sleep(1.5)
                    print(f"\nYour Card is {user_card}, the computers Card is {computer_card}")
                    s = "You won this round"
                    if card_value(user_card)>card_value(computer_card):
                        print(s,"but you wasted your cheat!!")
                    else:
                        print(s,"with this amazing Cheat move!!")
                    print(f"User - {user_score} | Computer - {computer_score}\n")

                    if user_score == 5:
                        print("\nCongratulations!! You won the game.\n")
                        break
                    elif computer_score == 5:
                        print("\nUnfortunately, Computer won the game.\n")
                        break
                    else:
                        round+=1
                        continue
                else:
                    print(
                        "You are a dirty cheater who cannot cheat any more and you have play the round like normal")
        # -------------round start------------------------
        user_card = user[random.randint(0, len(user)-1)]
        computer_card = computer[random.randint(0, len(computer)-1)]
        print("Suffling the Card...")
        sleep(1.5)
        print(f"\nYour Card is {user_card}, the computers Card is {computer_card}")
        if card_value(user_card) > card_value(computer_card):
            diff = abs(card_value(user_card)-card_value(computer_card))
            if 10<=diff<13:
                print("You won this round with Domination")
            elif diff==1:
                print("You won this round but that was too close")
            else:
                print("You won this round")
            user_score += 1
            user.append(computer_card)
            computer.remove(computer_card)
        elif card_value(user_card) < card_value(computer_card):
            print("Computer won this round.")
            computer_score += 1
            computer.append(user_card)
            user.remove(user_card)
        else:
            print("This round is tied.")
        print(f"User - {user_score} | Computer - {computer_score}")

        # ------------Round End --------------------------

        if user_score == 5:
            print("\nCongratulations!! You won the game.\n")
            break
        elif computer_score == 5:
            print("\nUnfortunately, Computer won the game.\n")
            break
        else:
            round += 1


if __name__ == "__main__":
    grettings()
    while (1):
        print("1. start --> For starting the game\n2. quit --> For quitting the game\n3. clear --> For clearing the screen\n")
        while 1:
            response = input()
            if response =='start':
                break
            elif response =='quit':
                break
            elif response =='clear':
                break
            else:
                print("Please enter'start' or 'q'\n")
        if response == "start":
            start_game()
        elif response == "quit":
            break
        elif response == "clear":
            clear()
    print("Exiting the game......")
