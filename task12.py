
def task12():
 user_palin = input(" ")

 user_palin = user_palin.casefold() #in case user write in uppercase.

 if user_palin == user_palin[::-1]:
   print("Palindorme")
 else:
    print("No Palindorme")

task12()














"""user_palin = input(" ")

user_palin = user_palin.casefold()

user_rev = reversed(user_palin)


if user_palin == user_rev:
    print("Palindorme in your text")
else:
    print("No Palindorme in your text")"""
