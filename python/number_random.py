import random

#print(help(random)) # This function shows the documentation for the random module

#low = 1
#high = 100

#number = random.randint(low, high) # This generates a random integer between 1 and 100, inclusive
#number = random.random()   # This generates a random float between 0.0 and 1.0, exclusive of 1.0
#print(number)

options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#Choice = random.choice(options) # This randomly selects one of the options from the tuple

random.shuffle(cards) # This shuffles the list of cards in place


print(cards)