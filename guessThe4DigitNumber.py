import random
from collections import Counter

computerNo = random.randint(1000, 9999)
# print(computerNo)

def correctNumbers(computerNo_list,guessNo_list):# to count correct digits
    correct_digit = 0
    counter1 = Counter(computerNo_list)
    counter2 = Counter(guessNo_list)
        
    for element, count in counter1.items():
        if element in counter2:
            correct_digit += min(count, counter2[element])
    return correct_digit

def correctPositions(computerNo_list,guessNo_list):
    position = 0
    for i in range(len(computerNo_list)):
        if computerNo_list[i] == guessNo_list[i]:
            position += 1
    return position

print("# Guess the four digit number #")
count = 0
while True:
    guessNo = input("Enter your guess: ")

    if  type(guessNo) == int:
        print("Enter a four digit number")
        break

    elif guessNo == 0:
        print("Enter 4 digit number: ")
        break

    # guessNo = int(guessNo1)
    guessNo_list = [int(digit) for digit in str(guessNo)]
    # print(guessNo_list)

    # computerNo = 4567
    computerNo_list = [int(digit) for digit in str(computerNo)]
    # print(computerNo_list)
    
    x = correctNumbers(computerNo_list,guessNo_list)
    y = correctPositions(computerNo_list,guessNo_list)
    print("Number of correct digits: ",x)
    print("Number of correct positions: ",y)

    count = count+1

    if x == 4 and y == 4:
        print("You Win !!!!!!!")
        print(f"You took", count , "number of guesses ")
        break
