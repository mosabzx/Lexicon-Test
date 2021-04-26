import math

#print(math.sqrt(5.3))

user = float(input("Enter a decimal number: "))

#print(math.sqrt(user) + math.pow(user, 2) + math.pow(user, 10))

print(math.sqrt(user))
print(math.pow(user, 2))
print(math.pow(user, 10))

def task9():
    user = float(input("Enter a decimal number: "))
    print(math.sqrt(user))
    print(math.pow(user, 2))
    print(math.pow(user, 10))
task9()



def task9():
    import math

    user = float(input("Enter a decimal number: "))
    print(math.sqrt(user)," (√)")
    print(math.pow(user, 2)," (^2)")
    print(math.pow(user, 10)," (^10)")


#task9()