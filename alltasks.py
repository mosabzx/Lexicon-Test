from colorama import Fore,init
init()
x = 1
z = 2


def task1():

    print("Hello World")

#task1 ()



def task2():
    fname = input("Please enter your first name: ")
    aname = input("Please enter your second name: ")
    age = input("Please enter your age: ")
    print("Hello " + fname + ", Your family name is: " + aname + " , Your age is: " + age + ".")


#task2()



def task3():
    global x,z
    
    c = Fore.RESET
    c1 = Fore.CYAN
    c2 = Fore.LIGHTRED_EX
    c3 = Fore.YELLOW
    c4 = Fore.LIGHTMAGENTA_EX
    if x < z :
        print(c3)
        x += 1
    elif z == x :
        print(c)
        x -= 1

    
    
    
    


#task3()



def task4():
    import datetime
    datum = datetime.datetime.now()
    print(datum.date())

#task4()



def task5():
    val1 = float(input("Please insert first value: "))
    val2 = float(input("Please insert second value: "))
    if val1 > val2:
        print("The grater value is: " , val1)
    else:
        print("The grater value is: " , val2)


#task5()



def task6():
    import random

    num = (random.randint(1, 100))
    user = " "

    while num != user:
      user = int(input("Try to Guess my number: "))
      if num > user:
        print("The number you have been enterd is smaller than the value, try again !")
      elif num < user:
        print("The number you have been entered is bigger than the value, try again !")
      else:   
        print("Correct Number Finally!")
        break


#task6()



def task7():
    f = open("task7.txt", "w")

    f.write(input("Write your text line: " + " \n"))

    
    f.close()

#task7()



def task8():
    f = open("task7.txt", "r")

    print("Read your text line:" + "\n",f.read())

    f.close()

#task8()



def task9():
    import math

    user = float(input("Enter a decimal number: "))
    print(math.sqrt(user)," (√)")
    print(math.pow(user, 2)," (^2)")
    print(math.pow(user, 10)," (^10)")


#task9()




def task10():
    
    for i in range(1, 11):
        for j in range(i, (i*11), i):
            print(j, end="\t")
        print()



#task10() 





def task11():
    from random import sample
    rang = [ar for ar in range(1,21)]
    rand = sample(rang,20)
    print(rand , ("Random Arry"))
    print(rang , ("Ascending Arry"))


#task11()




def task12():

    user_palin = input(" ")

    user_palin = user_palin.casefold() #in case user write in uppercase.

    if user_palin == user_palin[::-1]:
        print("Palindorme")
    else:
        print("No Palindorme")

#task12()




def task13():
    sif = input("Enter the first collection numbers: ")
    sif1 = input("Enter the second collection  numbers: ")
    collect = sif + " " + sif1
    print(collect)


#task13()



def task14():
    a = input("Enter numbers separated with comma \nFor Example: 1,2,44,224 : ") 

    b = a.split(",") 

    c = []
    c.extend(b)
    c = list(map(int, c)) 
    f = []
    g = []
    for h in c: 
        if (h % 2) ==0: 
            f.append(h)
        else:
            g.append(h)
    print("Even Numbers", f)
    print("Odd Numbers", g)

#task14()



def task15():

    a = input("Enter numbers separated with comma to get the addition result\nFor Example: 1,2,44,224 : ") 

    b = a.split(",") 

    c =[]
    c.extend(b)
    c = list(map(int, c))
    d = []
    for e in c:
        d.append(e)
    h = sum(d)
    print("The Result: ", h)


#task15()
















































  






















