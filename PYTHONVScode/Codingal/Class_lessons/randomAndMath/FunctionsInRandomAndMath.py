
import random
import math

#help(math)

# random method generates value bet 0 and 1
print(random.random())
print(random.randint(1,100))
print(random.choice("Alsan"))
list = ["a","b","c","d","e",1,2,3,4,5]
print("list items: ",list)
random.shuffle(list)
print("shuffled list items: ",list)
print(f"random choice: {random.choice(list)}")
print("=================================================")
#help(math)
print(math.pi)
print(math.sin(math.radians(90)))
print(math.cos(math.radians(0)))
print(math.tan(math.radians(45)))



# activity 1: number guessing game.
# activity 2: calculator for trigonometrical functions