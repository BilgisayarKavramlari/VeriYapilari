import random

computer_count = random.randint(1, 100)
number_of_attempts = 0

while True:
    try:
        user_guess = int(input("Please guess the number: "))
        
        if computer_count == user_guess:
            number_of_attempts += 1
            print(f"You won in {number_of_attempts} attempts.")
            break
        
        elif computer_count > user_guess:
            print("Too Low")
            number_of_attempts += 1
        
        else:
            print("Too High")
            number_of_attempts += 1
    
    except:
        print("Choose number between 1 to 100!..")
