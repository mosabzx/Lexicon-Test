#Funktion som genererar att slumpmässigt tal mellan 1 och 100. Användaren ska sedan gissa talet. Gissar användaren rätt så ska ett meddelande säga detta, samt hur många försök det tog. Gissar användaren fel ska ett meddelande visas som informerar ifall talet var för stort eller för litet

import random



"""num = (random.randint(1, 100))
user = " "

while num != user:
    user = int(input("Try to Guess my number:" + " "))
    if num > user:
        print("The number you have been enterd is smaller than the value, try again !")

    elif num < user:
        print("The number you have been entered is bigger than the value, try again !")
    else:
        print("Correct Number WowOwoW !")
        break """
        



#Här som Funkion 

def guess():

  num = (random.randint(1, 10))
  user = " "

  while num != user:
      user = int(input("Try to Guess my number:" + " "))
      if num > user:
        print("The number you have been enterd is smaller than the value, try again !")
      elif num < user:
        print("The number you have been entered is bigger than the value, try again !")
      else:   
        print("Correct Number Finally!")
        break


guess() 

       
   

    
    
    
  
  
  
    


    

    
        
    

        
        