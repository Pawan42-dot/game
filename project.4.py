import random

def user_choice():
    userinput=input("enter: stone,paper,sessior :")

    if userinput not in ("stone","paper","sessior"):
        print("invalid input")
        return None
    return userinput

def computer_choice():
    computerinput=["stone","paper","sessior"]
    return random.choice(computerinput)

def game():

    userinput=user_choice()
    if userinput is None:
        return

    
    computerinput = computer_choice()
    print(f"computer choose :{computerinput}")

    if (userinput==computerinput):
        print("its tie !")

    elif (userinput=="stone" and computerinput=="sessior") or\
         (userinput=="paper" and computerinput=="stone") or\
         (userinput=="sessior" and computerinput=="paper"):
         print("you win")
        
    else:
        print("computer win")


game()




         

          
    
    
    
 