import random
animals = ['fox', 'goats', 'rabbits', 'birds', 'cows', 'cats', 'dogs', 'fishes']
fruits = ['apple', 'banana', 'pear', 'pomegranate']
stationery = ['pencil', 'pen', 'copy', 'ruler']
#word can be any from the list so concate
while 1:
    word = animals + fruits + stationery
    random_word = random.choice(word)
    print("word Guessing Game")

    #msg if it is animal/fruit/stationery
    if random_word in animals:
        print("Hint:It is an animal")
    elif random_word in fruits:
        print("Hint:It is a fruit")
    else:
        print("Hint:It is a stationery")

    user_guesses = '' #string variable
    chances = 5 #integer variable

    while chances >0:
        wrong_guess = 0 #initialized variable
        for ch in random_word:
            if ch in user_guesses:
                print(ch, end = '')
                #break
            else:
                wrong_guess += 1
                print('_', end = '')

                if wrong_guess == 0:
                    print("\n Congratulations!!", random_word)
                    break

                guess = input("\nMake a guess")
                user_guesses += guess
                if guess not in random_word:
                    chances -= 1
                    print(f'wrong.You Have {chances} more chances')
                if chances == 0:
                    print("Game Over", "the word is", random_word)


