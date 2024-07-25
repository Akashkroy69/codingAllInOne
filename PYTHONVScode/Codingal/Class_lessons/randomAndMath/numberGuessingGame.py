import random
print("number guessing game:")
target_num = random.randint(1,100)
guessed_num = 0
score = 1000
attempt = 0
while guessed_num != target_num:
  guessed_num = int(input("enter your guess: "))
  attempt += 1
  if target_num == guessed_num:
    score += 400
    print(f"you have guessed the number correctly, the number is {target_num}, in {attempt} turns, the score is {score} ")
  elif guessed_num > target_num:
    score -= 200
    print("number is greater than the target number") 
  elif guessed_num < target_num:
    score -=200
    print("number is less than the target number")

print("==============")
if score > 0 :
  print("you won")
elif score == 0:
  print("it a tie")
else:
  print("you lost")
print("==============")
  