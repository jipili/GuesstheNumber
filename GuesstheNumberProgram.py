import random
print("Hello. What is your name?")
name=input()
print('Hi, ' + name +  '. Can you give me a maximum number?')
maxint=int(float(input()))

print('Well, ' + name + ' ,I am thinking of a number between 1 and ' + str(maxint) + '.')
print("Take a guess.")
compnum=random.randint(1,maxint)
humnumber=int(input())
while humnumber>compnum:
        print("Your guess is too high.")
        print ("Take a guess.")
        humnumber=int(input())
while humnumber<compnum:
        print ("Your guess is too low.")
        print ("Take a guess.")
        humnumber=int(input())
else:
        print("Your guess is correct!")
        print("Congrats!")
