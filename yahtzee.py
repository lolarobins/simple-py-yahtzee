import random
import time

dice = [0] * 5
score_round = [0] * 3
score_type = [""] * 3


# Run game
def start_game():
    for x in range(3):
        print(f"\nROUND {x + 1}")
        hold = [False] * 5
        for z in range(3):
            roll(hold)
            print("\nYou rolled:")
            for y in range(5):
                print(f"D{y + 1}:", end=" ")
                if hold[y]:
                    if y == 4:
                        print(f"[{dice[y]}]")
                    else:
                        print(f"[{dice[y]}]", end=" | ")
                else:
                    if y == 4:
                        print(f"{dice[y]}")
                    else:
                        print(f"{dice[y]}", end=" | ")

            if z != 2:
                ask_hold = input("\nWould you like to hold any dice? (Y/n): ")
                if ask_hold.lower() == "y":
                    specify_hold = input("Which dice would you like to hold? ")

                    print("Holding dice: ", end="")
                    for to_hold in specify_hold.split(" "):
                        try:
                            hold[int(to_hold) - 1] = True
                            print(f"{to_hold}", end=" ")
                        except ValueError:
                            print("\nFailed to hold: Invalid number entered.")
                        except IndexError:
                            print("\nFailed to hold: Number must be between 1-5.")
                    print("")

            all_hold = True
            for y in range(5):
                if not hold[y]:
                    all_hold = False

            if all_hold:
                break

        calculate_score(x)
        print(f"\nYou have scored {score_round[x]} points ({score_type[x]}) this round.")

    print("\nThe game has now finished.")
    print("\nGame Summary:")
    for x in range(3):
        print(f"Round {x+1}: {score_round[x]} ({score_type[x]})")
    print(f"Total Points: {total_pts()}")
    end_game()


# Calls at end for restarting
def end_game():
    play_again = input("\nWould you like to play a new game? (Y/n): ")
    if play_again.lower() == "y":
        start_game()


# Calculates score using each checking function, order matters.
def calculate_score(rnd):
    score = 0
    s_type = "None"
    ordered = sorted(dice, reverse=False)
    # Yahtzee
    if yahtzee(ordered):
        score = 50
        s_type = "Yahtzee"
    # 4 of a kind
    elif four_oac(ordered):
        for x in range(5):
            score += ordered[x]
        s_type = "Four of a Kind"
    # Full House
    elif full_house(ordered):
        score = 25
        s_type = "Full House"
    # 3 of a kind
    elif three_oac(ordered):
        for x in range(5):
            score += ordered[x]
        s_type = "Three of a Kind"
    # Large straight
    elif large_straight(ordered):
        score = 40
        s_type = "Large Straight"
    # Small straight
    elif small_straight(ordered):
        score = 30
        s_type = "Small Straight"
    score_round[rnd] = score
    score_type[rnd] = s_type


# Score calculation
def yahtzee(ordered):
    # X X X X X
    return ordered[0] == ordered[1] == ordered[2] == ordered[3] == ordered[4]


def four_oac(ordered):
    # X X X X Y
    for x in range(2):
        if ordered[x] == ordered[x+1] == ordered[x+2] == ordered[x+3]:
            return True
    return False


def full_house(ordered):
    # X X X Y Y
    return ((ordered[0] == ordered[1]) & (ordered[2] == ordered[3] == ordered[4])) | \
            ((ordered[0] == ordered[1] == ordered[2]) & (ordered[3] == ordered[4]))


def three_oac(ordered):
    # X X X Y Z
    for x in range(3):
        if ordered[x] == ordered[x+1] == ordered[x+2]:
            return True
    return False


def small_straight(ordered):
    # 1 2 3 4 X, 2 3 4 5 X, 3 4 5 6 X
    # X 1 2 3 4, X 2 3 4 5, X 3 4 5 6
    for x in range(2):
        if ordered[x] == (ordered[x+1]-1) == (ordered[x+2]-2) == (ordered[x+3]-3):
            return True
    return False


def large_straight(ordered):
    # 1 2 3 4 5, 2 3 4 5 6
    return ordered[0] == (ordered[1]-1) == (ordered[2]-2) == (ordered[3]-3) == (ordered[4]-4)


# Roll dice that are not held
def roll(hold):
    # Takes 3s to roll
    print("\nRolling", end=" ")
    time.sleep(1)
    print(".", end=" ")
    time.sleep(1)
    print(".", end=" ")
    time.sleep(1)
    print(".")

    # randomizes all but held
    for x in range(5):
        if hold[x]:
            continue
        dice[x] = random.randint(1, 6)


# easiest way.
def total_pts():
    total = 0
    for x in range(3):
        total += score_round[x]
    return total


# start
print("\nWelcome to text-based Yahtzee (simplified)!")
# noinspection SpellCheckingInspection
print("Written by Liam Robins for ICS 3U, Mr. Winsa.")
print("\nRULES:\nYou will be able to play 3 rounds.\nDuring each of these rounds, you will be given 3 chances to "
      "hold and roll dice.\nDice that are held will have square brackets surrounding their value.\nWhen specifying "
      "dice to hold, separate their numbers with spaces. Ex: '1 4 5'.\nAt the end of your "
      "game, your points will be totalled.")
print("\nPOINTS:\nFull House     | 25 pts     | 3 dice of one value, 2 dice of another\nSmall Straight | 30 pts     | "
      "5 dice in ascending order\nLarge Straight | 40 pts     | 5 dice in ascending order\nYahtzee        | 50 pts    "
      " | 5 dice of the same value\n3 of a kind    | Dice total | 3 dice of the same value\n4 of a kind    | Dice "
      "total | 4 dice of the same value")
start = input("\nStart the game? (Y/n): ")

if start.lower() == "y":
    start_game()
else:
    quit(0)
