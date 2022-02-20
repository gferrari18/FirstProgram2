print("Welcome to Rock, Paper, Scissors!")
print("Rock = 1, Paper = 2, Scissors = 3")
usr = int(input("Enter your number: "))
from multiprocessing import RLock
import random
bot = random.randrange(1,3)



if usr == 1:
    print("You chose rock")
elif usr == 2:
    print('You chose paper')
elif usr == 3:
    print('You chose scissors')

if bot == 1:
    print("Bot chose rock")
elif bot == 2:
    print('Bot chose paper')
elif bot == 3:
    print('Bot chose scissors')



if usr == bot:
    print("Draw")
elif usr == 1 and bot == 2: print("You lose!")
elif usr == 1 and bot == 3: print("You win!")
elif usr == 2 and bot == 1: print('You win!')
elif usr == 2 and bot == 3: print('You lose!')
elif usr == 3 and bot == 1: print('You lose!')
elif usr == 3 and bot == 2: print('You win!')


