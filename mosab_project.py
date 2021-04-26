import os
from alltasks import *



def menu():
    

    print("Welcome to my Program, Please enter No. from the menu below to run the task: \n \n1.Print Hello World. \n2.Enter your info. \n3.Change the console color.\n4.Print the date of today. \n5.Enter 2 values and check whois grater. \n6.Guess the number between 1 - 100. \n7.Write your note in a file. \n8.Check your note in your file. \n9.Enter a decimal number and get (Root, Power to 2, Power to 10). \n10.Print the multiplaction table from 1 to 10. \n11.Print a two lists of numbers one randome and the other sorted. \n12.Enter a text and check the palindorme words. \n13.Enter 2 collections of numbers and get them as one collection. \n14.Enter collection of number and get them sorted as even and odd \n15.Enter collections of number and get their addition result. \n16. . \n0.Exit the program.\n")

    select = input("Enter No: ")
    if select == "0":
        print("Thanks for using my program and GoodBye!")
    if select == "1":
        os.system("cls")
        task1()
        menu()
    if select == "2":
        task2()
        print("\n")
        menu()
    if select == "3":
        os.system("cls")
        task3()
        print("\n")
        menu()
    if select == "4":
        os.system("cls")
        task4()
        print("\n")
        menu()
    if select == "5":
        task5()
        print("\n")
        menu()
    if select == "6":
        task6()
        print("\n")
        menu()
    if select == "7":
        task7()
        print("\n")
        menu()
    if select == "8":
        task8()
        print("\n")
        menu()
    if select == "9":
        task9()
        print("\n")
        menu()
    if select == "10":
        task10()
        print("\n")
        menu()
    if select == "11":
        task11()
        print("\n")
        menu()
    if select == "12":
        task12()
        print("\n")
        menu()
    if select == "13":
        task13()
        print("\n")
        menu()
    if select == "14":
        task14()
        print("\n")
        menu()
    if select == "15":
        task15()
        print("\n")
        menu()
    


menu()




