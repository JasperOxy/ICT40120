import random

fortune_number = random.randint(1,100)

if fortune_number < 49:
  fortune_text = "You need to put in more work!"

if fortune_number  > 50:
  fortune_text = "Could you do better?"

if fortune_number >= 79:
  fortune_text = "Could you do better?"

if fortune_number >= 80:
  fortune_text = "Well done!"
  

print(fortune_number)  
print(fortune_text)