#Need to get code to loop so then the user can keep putting in numbers
#Need to get code to stop looping once -1 has been added as a number

fortune_number = int(input("please enter your number!"))
try:
    
    for x in fortune_number:
        if x == "100":
            continue
        print(x)

    if fortune_number <= 49:
        print('please try again!')

    elif fortune_number <= 79: 
        print('Come on, you can do better than that')

    elif fortune_number  <= 100:
        print('excellent job!!!')
except:
    print("This wasn't successful, Please try again!")

if fortune_number <= 101: 
    print("You have entered a number that is too high, please enter a number between 1 and 100")