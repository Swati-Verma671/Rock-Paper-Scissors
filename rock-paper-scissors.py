#Another game rock-paper-scissors
import random

#welcoming the player
print("Welcome! To a game of rock-paper-scissors.")
name=input("May I know your good name?: ")
print("Hope you have a great time!",name)

#Rules
print("Rules---\n")
print("You will be given a total of 3 chances to pick any one of Rock, Paper or Scissors and play against a bot.\n")
print("Whether you win or lose the game will be decided by the total no. of the games you won in these 3 chances.\n")


#Initialising 
turns=3

#allowing the player to choose between rock, paper or scissors
def user():
    print("What would you choose? Rock, Paper or Scissors")
    user=input()
    temp=0
    if(user=='Rock'):
        print("You chose: Rock.")
        temp=1
    elif(user=='Paper'):
        print("You chose: Paper.")
        temp=2
    elif(user=='Scissors'):
        print("You chose: Scissors.")
        temp=3
    return(temp)

#Now the machine's response
def machine():
    lst=list()
    lst=['Rock','Paper','Scissors']
    guess=random.choice(lst)
    mech=0
    if(guess=='Rock'):
        print("Bot: Rock")
        mech=1
    elif(guess=='Paper'):
        print("Bot: Paper")
        mech=2
    elif(guess=='Scissors'):
        print("Bot: Scissors")
        mech=3
    return(mech)

# Comparing the user'choice to the machine's.
def Comparison(t,m):
    
    if(t==1 & m==3):
        
        return("You Won")
    elif(t==2 & m==1):
        
        return("You Won")
    elif(t==3 & m==2):
        
        return("You Won")
    elif(t==m):
        return("Tie")
    else:
        
        return("You lost")
loss=0
wins=0    
while(turns>0):
    first=user()
    second=machine()
    result=Comparison(first,second)
    turns-=1
    if(result=='You lost'):
        loss+=1
        print(result,"Total Wins:",wins,"Total loss:",loss)
    elif(result=='You Won'):
        wins+=1
        print(result,"Total Wins:",wins,"Total loss:",loss)
    else:
        print(result,"Total Wins:",wins,"Total loss:",loss)
        

if(turns==0):
    if(wins>loss):
        print("Congratulations!! You won the game!!")
    else:
        print("You lost the game :( better luck next time!")    
    
 



    


