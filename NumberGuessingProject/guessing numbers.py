import random
import math
#taking inputs
lower = int(input("Enter the lower integer value"))
upper = int(input("Enter upper integer value"))
#generationg random number between lower and upper
x = random.randint(lower, upper)
print("you've only",
      round(math.log(upper-lower+1,2)),
      "chances to guess the interger number.\n")
#initializing the number of guessing
count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("guess the number"))

    #condition testing
    if x == guess:
        print("congratulations!", count, "try")
        break

    elif x > guess:
        print("number is too small")
    elif x < guess:
        print("number is too high")

        if count >= math.log(upper - lower + 1, 2):
            print("\nThe number is %d" % x)
            print("\tBetter Luck Next time!")