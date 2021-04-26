#Funktion som tar in input från användaren (Förnamn, Efternamn, Ålder) och sedan skriver ut dessa i konsolen

"""fname = input("Please enter your first name: ")
aname = input("Please enter your after name: ")
age = input("Please enter your age: ")

print("Hello " + fname + ", Your family name is: " + aname + " , Your age is: " + age + ".")"""

#Nu Som funkion utan välkommen.

"""def info():
    fname = input("Please enter your first name: ")
    aname = input("Please enter your second name: ")
    age = input("Please enter your age: ")

info()"""


#Nu Som funkion med välkommen

def info():
    fname = input("Please enter your first name: ")
    aname = input("Please enter your second name: ")
    age = input("Please enter your age: ")

    print("Hello " + fname + ", Your family name is: " + aname + " , Your age is: " + age + ".")

info()
