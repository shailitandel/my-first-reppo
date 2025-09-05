import random
            
def SPS():
    user = input("Enter choice stone, paper or scissors: ")

    # element={1:'stone',2:'paper',3:'scissors'}
    element=['stone','paper','scissors']
    computer = random.choice(element)

    print("User chooses: "+user)
    print("Computer chooses: "+computer)

    if user == computer:
        print("Its a Draw!!")
    elif user =='stone' and computer =='paper':
        print("Computer Wins")
    elif user =='stone' and computer =='scissor':
        print("User Wins")
    elif user =='paper' and computer =='scissors':
        print("Computer Wins")
    elif user =='paper' and computer =='stone':
        print("User Wins")
    elif user =='scissors' and computer =='paper':
        print("User Wins")
    elif user =='scissors' and computer =='stone':
        print("Computer Wins")
    else:
        print("choose the right option")


while True:
    x = input("play[P] or quit[Q] \n")
    if x == 'Q' or x=='q' or x=='quit':
        break
    elif x=='play' or x=='p' or x=='P':
        SPS()
    else:
        break
