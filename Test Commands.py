import os

from colorama import init,Fore, Back, Style
init()

'''print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')'''
'''from colorama import init
from termcolor import colored

#use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))

init(autoreset=True)
print(Fore.RED + 'some red text')
print('automatically back to default color again')'''






'''import os
color = [os.system('color 09'),os.system('color 0F')]

for x in range(len(color)):
    print(x)'''



def color1():
    
    os.system('color 0F')







def reset():
    print(Fore.WHITE)
    
x = 1
z = 2


#color = [os.system('color 0F'),os.system('color 09'),os.system('color 06')]




def task33():
    global z,x
    
    c = Fore.RESET
    c0 = Fore.WHITE
    c1 = Fore.CYAN
    c2 = Fore.LIGHTRED_EX
    c3 = Fore.YELLOW
    c4 = Fore.LIGHTMAGENTA_EX
    
    if x < z :
        print(c4)
        x += 1
        
    elif z == x :
        print(c)
        x -= 1

    


 #task33()



def men():
    global z,x
    print("Welcome To My Test Program!.\n1. Enter 3 to change to console text color.\n2.To Rest The Color\n0. to Exit.")
    
   
  
    
    choice = input("Enter Number: ")
    
    if choice == "3":
        task33()
        men()
        
    
        

    if choice == "2":
        reset()
        men()
        
    if choice == "0":
        print("GoodBye!")

    


men()



#os.system("cls")


 #blueColor = ("\u001b[34m")
 #resetColor = ("\u001b[0m")

        

            

    
         


''' if user_palin == user_palin[::-1]:
        print("Palindorme")
    else:
        print("No Palindorme")'''

#task12()

