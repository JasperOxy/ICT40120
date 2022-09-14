import random

luck_number = random.randint(1,100)

fortune_number = random.randint(1,10)

fortune_text = ""

if fortune_number == 1:
  fortune_text = 'Today is your lucky day!'

if fortune_number == 2:
  fortune_text = 'Today will be tough, but worth it!'

if fortune_number == 3:
  fortune_text = 'You will be unlucky!'

print(f"{fortune_text} Your lucky number is: {luck_number}")

if fortune_number == 4:
  fortune_text = "This isn't your day!"

if fortune_number > 4:
  fortune_text = "This isn't your day!"
  print("This isn't your day!")