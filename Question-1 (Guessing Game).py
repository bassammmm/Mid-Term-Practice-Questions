import random

random_num = random.randint(1,100)
print("\n\nLets play a game! Guess the number I am thinking about!\n")
user_num = int(input("Please guess the number :"))
count = 0
while user_num!=random_num:
    if user_num>random_num:
        print("Your guess is greater than my number!\n")
        user_num = int(input("Please Guess again : "))
        count+=1
    elif user_num<random_num:
        print("Your guess is lower than my number!\n")
        user_num = int(input("Please Guess again : "))
        count+=1
else:
    print("\nYOU GUESSED IT!")
    print("You took",count+1,"times to guess!")    
