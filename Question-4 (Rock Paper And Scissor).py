print("\t\tWelcome to Rock Paper And Scissors")
import random
import time
name = input("\nWhat's your name Loser? :")
time.sleep(0.5)
print("I dont really care if people call you",name,",I'm still gonna call you LOSER!")
time.sleep(0.5)
score = int(input("\nHow many points are required to win? :"))

choices = ["r","p","s"]
human_score=0
computer_score=0
insults_hw = ["I let you win this time or else you'd say I cheated!","You will always be a loser, don't lie to yourself that you'll win!","If laughter is the best medicine, your face must be curing the world","You're so ugly, you scared the crap out of the toilet","Your family tree must be a cactus because everybody on it is a prick","I guess you prove that even god makes mistakes sometimes"]
insults_cw = ["Woops, see I knew you were a born loser!","I bet you look like you were drawn with my left hand. HAHAHA!","Where were you when they were distributing brains?","AND THAT IS WHY ONE DAY WE WILL TAKE OVER THE WORLD","It's better to let someone think you are an Idiot than to play against me and prove it","Your birth certificate is an apology letter from the condom factory","I don't know what makes you so stupid, but it really works"]
while human_score!=score and computer_score!=score:
    user_choice= input("\n\nChoose (r)ock, (p)aper or (s)cissors :")
    user_choice = user_choice.lower()
    while user_choice not in choices:
        print("Are you retarded? Press only 'r' for Rock, 'p' for Paper or 's' for Scissor!")
        user_choice= input("\n\nChoose (r)ock, (p)aper or (s)cissors :")
    
    if user_choice=='r':
        print(name.title()," : Rock",end="     ")
    elif user_choice=='p':
        print(name.title()," : Paper",end="     ")
    elif user_choice=='s':
        print(name.title()," : Scissor",end="     ")
    computer = random.choice(choices)
    if computer=='r':
        computer_p = 'Rock'
    if computer=='p':
        computer_p = 'Paper'
    if computer=='s':
        computer_p = 'Scissor'
    print("Computer : ",computer_p,end="    ")
    
    if user_choice==computer:
        print("Its a Draw!")
        
    elif user_choice=='r' and computer=='s':
        print(name.title()," Wins")
        human_score+=1
        time.sleep(0.5)
        print(random.choice(insults_hw))
    elif user_choice=='r' and computer=='p':
        print("Computer Wins")
        computer_score+=1
        time.sleep(0.5)
        print(random.choice(insults_cw))
    elif user_choice=='p' and computer=='r':
        print(name.title()," Wins")
        human_score+=1
        time.sleep(0.5)
        print(random.choice(insults_hw))
    elif user_choice=='p' and computer=='s':
        print("Computer Wins")
        computer_score+=1
        time.sleep(0.5)
        print(random.choice(insults_cw))
    elif user_choice=='s' and computer=='r':
        print("Computer Wins")
        computer_score+=1
        time.sleep(0.5)
        print(random.choice(insults_cw))
    elif user_choice=='s' and computer=='p':
        print(name.title()," Wins")
        human_score+=1
        time.sleep(0.5)
        print(random.choice(insults_hw))
    
    
    

print("\n\nHuman :",human_score,"    Computer:",computer_score)
if human_score>computer_score:
    print("Human Wins!")
else:
    print("Computer Wins!")
    
