from random import sample

def twolist():
    rang = [ar for ar in range(1,21)]
    rand = sample(rang,20)
    print(rand , ("Random Arry"))
    print(rang , ("Ascending Arry"))

twolist()






