import random

def play_game():
    choices = ['snake', 'water', 'gun']
    computer_choice = random.choice(choices)
    
    player_choice = input("Enter your choice (snake/water/gun): ").lower()
    
    if player_choice not in choices:
        print("Invalid choice! Please enter either 'snake', 'water', or 'gun'.")
        return
    
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'snake' and computer_choice == 'water') or \
         (player_choice == 'water' and computer_choice == 'gun') or \
         (player_choice == 'gun' and computer_choice == 'snake'):
        print("Congratulations! You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_game()
