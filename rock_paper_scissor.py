import random

print("Welcome to Rock-Paper-Scissor Game!")

user_score = 0
comp_score = 0

play_again = "yes"

while play_again == "yes":
    print("\nChoose Rock, Paper, or Scissor")
    user = input("Your choice: ").lower()
    comp = random.choice(["rock", "paper", "scissor"])

    if user not in ["rock", "paper", "scissor"]:
        print("Invalid input! Please choose Rock, Paper, or Scissor only....")
    else:
        print(f"You chose: {user}")
        print(f"Computer chose: {comp}")

        if user == comp:
            print("Result: It's a Tie")
        elif user == "rock":
            if comp == "scissor":
                print("Result: You win")
                user_score += 1
            else:
                print("Result: Computer wins")
                comp_score += 1
        elif user == "paper":
            if comp == "rock":
                print("Result: You win")
                user_score += 1
            else:
                print("Result: Computer wins")
                comp_score += 1
        elif user == "scissor":
            if comp == "paper":
                print("Result: You win")
                user_score += 1
            else:
                print("Result: Computer wins")
                comp_score += 1

        print(f"Score => You: {user_score} | Computer: {comp_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
print("\nGame over! Thanks for playing...")