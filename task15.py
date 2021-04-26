
def add_result():

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


add_result()
