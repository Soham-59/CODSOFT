import random
# ROCK PAPER SCISSOR GAME


def game():
    # list for randomly choose by computer
    list1=['rock','paper','scissor']
    # user input
    user=input("Enter your choice from(rock,scissor,paper) :")
    print("user=",user)
    comp=random.choice(list1)
    print("computer=",comp)
    # score counts of computer and user
    comp_count=0
    user_count=0
    
    if comp=="rock"and  user=="scissor":
        print("computer win the match!")
        comp_count=comp_count+1
        
    elif(comp=="paper"and user=="scissor"):
        print("the user win the match!")
        user_count=user_count+1
        
    elif(comp=="scissor"and user=="paper"):
        print("computer win the match!")
        comp_count=comp_count+1

    elif comp=="rock"and user=="paper":
        print("user win the game!")
        user_count=user_count+1

    elif comp=="rock"and user=="rock":
        print("match is tie !")

    elif(comp=="scissor"and user=="rock"):
        print("the user win the match!")
        user_count=user_count+1

    elif(comp=="scissor"and user=="scissor"):
        print("match is tie !")

    elif comp=="paper"and user=="paper":
        print("match is tie !")

    elif comp=="paper"and user=="rock":
        print("the computer win the match!")
        comp_count=comp_count+1
    else:
        print("Invalid choice of user!")
    print("Computer Score=",comp_count)
    print("User Score=",user_count)

game()
print("*********If you want to play New Round*********")
string=input("Enter Yes Or No=")
if string=="Yes":
    game()
else:
    pass