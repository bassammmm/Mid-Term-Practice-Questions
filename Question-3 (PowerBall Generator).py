import random
import time

list_first_num = []
list_powerball= []

while len(list_first_num)!=53:
    x=random.randint(1,53)
    if x not in list_first_num:
        list_first_num.append(x)
while len(list_powerball)!=42:
    x=random.randint(1,42)
    if x not in list_powerball:
        list_powerball.append(x)
print("\nLottery Number = ",end="")
for x in range(5):
    print("{0:3}".format(random.choice(list_first_num)),end="")
print("{0:3}".format(random.choice(list_powerball)))

no_of_sets = int(input("How many number of sets do you want to generate? :"))
for row in range(no_of_sets):
    print("\n")
    for col in range(8):
        if col==0:
            print("Your Numbers :",end="")
        elif col==6:
            print("  POWERBALL    :",end="")
        elif col==7:
            time.sleep(0.5)
            print("{0:3}".format(random.choice(list_powerball)),end=" ")
        else:
            time.sleep(0.5)
            print("{0:3}".format(random.choice(list_first_num)),end=" ")


