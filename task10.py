
def task10():
    for i in range(1, 11):
        for j in range(i, (i*11), i):
            print(j, end="\t")
        print()


task10()





def task10_4():

    x = [1,2,3,4,5,6,7,8,9,10]
    for z in x:
        print(*("{:2}" .format (z*col) for col in x)) 
    

#task10_4()




# Multiplication tables from 1 till 10.

def task10_3():
     nlist0 = [1,2,3,4,5,6,7,8,9,10]
     nlist1 = [1,2,3,4,5,6,7,8,9,10]

     for x in nlist0:
         for z in nlist1:
             print(" ")
             print(x,"X", z,"=", x*z)
    
#task10_3() 




# Multiplication table for choosen number by user.

def task10_1():
    digit = int(input("Enter a number to get multiplication table for it: "))
    for x in range(1,11):
        print(digit, "X", x, "=", x*digit)


#task10_1()












# Multiplication tables from 1 till 10.

def multy():
     nlist0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,0]
     nlist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     for x in nlist0:
         for y in nlist1:
             if x == 0:
                 continue
             print(" ")
             print(x * y)

#multy()






#Another code
def task10_2():

    a = [1,2,3,4,5,6,7,8,9,10]

    for i in a:
        print(*("{:3}" .format (i*col) for col in a))

#task10_2()



"""for i in range(1, 10+1):
    for j in range(i, (i*10)+1, i):
            print(j, end="\t")
    print()"""