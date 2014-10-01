from random import randint

print('come-out')
randomNumber1 = randint(1, 6)
randomNumber2 = randint(1, 6)
randomNumberSum1 = randomNumber1 + randomNumber2
print(randomNumberSum1)
if randomNumberSum1 == 7 or randomNumberSum1 == 11:
    print('You win!')
elif randomNumberSum1 == 2 or randomNumberSum1 == 3 or randomNumberSum1 == 12:
    print('Craps, you lose.')
else:
    print('The point is', randomNumberSum1)
    randomNumber1 = randint(1, 6)
    randomNumber2 = randint(1, 6)
    randomNumberSum2 = randomNumber1 + randomNumber2   
    print(randomNumberSum2)
    while randomNumberSum2 != randomNumberSum1 and randomNumberSum2 != 7: 
        randomNumber1 = randint(1, 6)
        randomNumber2 = randint(1, 6)
        randomNumberSum2 = randomNumber1 + randomNumber2
        print(randomNumberSum2)
    if randomNumberSum2 == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
