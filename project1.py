import random
def player_game():
    choices=["snake","water","gun"]
    computer_choice=random.choice(choices)
    player_choice=input("Enter your choice(snake/water/gun)")
    if player_choice not in choices:
        print("please enter either!'snake','water'.'gun'.")
        return
    print(f"computer choose{computer_choice}")
    print(f"you choice{player_choice}")
    if player_choice==computer_choice:
        print("game tie:")
    elif(player_choice=='snake' and computer_choice=='water') or\
        (player_choice=='water' and computer_choice=='gun') or\
        (player_choice=='gun' and computer_choice=='snake'):
        print("you win:")
    else:
        print("computer win") 
player_game()
    