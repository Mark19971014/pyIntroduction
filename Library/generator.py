import random
import statistics #统计学
import numpy
#coin = random.choice(["head","tails"])
#print(coin)

#number = random.randint(1,10)
#print(number)

cards = ["jack","queen","king"]
print(cards[2])
random.shuffle(cards)

#for-loop
#for i in range(3):
#    print(cards[i])

#for each loop
for element in cards:
    print(element)

print(statistics.mean([10,10,10]))


