from random import randint
from time import sleep
print('------------JOKEN PO----------------:')
print('make your move:')
print('[1] Rock')
print('[2] Paper')
print('[3] Scissor')
print('-------------------------------------:')
Playerchoice = int(input('-> '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
Cpuchoice = randint(1,3)
if Playerchoice == 1:
    print('You choose Rock')
    if Cpuchoice == 1:
        print('Your opponent chose Rock')
        print('It a TIE!!')
    elif Cpuchoice == 2:
        print('Your opponent chose Paper')
        print('YOU LOSE!!')
    elif Cpuchoice == 3:
        print('Your opponent chose Scissor')
        print('YOU WIN!!')
elif Playerchoice == 2:
    print('You choose Paper')
    if Cpuchoice == 1:
        print('Your opponent chose Rock')
        print('YOU WIN!!')
    elif Cpuchoice == 2:
        print('Your opponent chose Paper')
        print('It a TIE!!')
    elif Cpuchoice == 3:
        print('Your opponent chose Scissor')
        print('YOU LOSE!!')
elif Playerchoice == 3:
    print('You choose Scissor')
    if Cpuchoice == 1:
        print('Your opponent chose Rock')
        print('YOU LOSE!!')
    elif Cpuchoice == 2:
        print('Your opponent chose Paper')
        print('YOU WIN!!')
    elif Cpuchoice == 3:
        print('Your opponent chose Scissor')
        print('It a TIE!!')
else:
    print('INVALID MOVE')