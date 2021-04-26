#Filtering Between Even and Odd Numbers and add them into sorted list.

def odd_even():
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

odd_even()





"""a = input("Enter numbers separated with comma \nFor Example: 1,2,44,224 : ") #string

b = a.split(",") # Converting string from user input and split it and add it to a list.

c = []
c.extend(b)
c = list(map(int, c)) # Converting List elements to inegers.
f = []
g = []
for h in c: # For loop to pickup the the numbers from c list.
    if (h % 2) ==0: # Condition to sort between even and odd number.
        f.append(h) # Adding the even numbers after picked up by for loop after condition into a list.
        

    else:
        g.append(h) # Adding the odd numbers after picked up by foor loop after condition into a list.
       
print("Even Numbers", f)
print("Odd Numbers", g)"""






'''tal = int(input("Enter a number to check if even or odd: "))
if (tal % 2) == 0:
    print("{0} is Even number".format(tal))
else:
    print("{0} is Odd number".format(tal))'''




