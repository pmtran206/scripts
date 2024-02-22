# Interactive Sorting

import sys 
from random import randint


def print_menu():
    print("*" * 50)
    print(" Interactive Python Sorting ")
    print(" 1. Selection Sort")
    print(" 2. Bubble Sort")
    print(" q to quit")
    print("*" * 50)

def get_listSize():
    try:
        listSize = int(input("Enter number of List items:"))
    except ValueError:
        print("Please input Number > 0")
        sys.exit()
    validInput = check_input(listSize)
    if (validInput):
        return listSize
    else: print("not valid input")

def check_input(userinput):
    if (userinput > 0):
        return True
    else: return False

def get_menuInput():
    option = input("Select Sorting Method: ")
    if (option == 'q'): return option
    try: 
        option = int(option)
        if(0 < option <= 10): return option
        else: print("Number out of Range")
    except ValueError:
        print("Enter valid number")

def list_to_set(alist):
    return list(set(alist))

def generate_randomList(listSize):
    randomList = [None] * listSize
    for i in range(listSize):
        randomList[i] = randint(0, 999)
    uniqueList = list_to_set(randomList)
    return uniqueList

def SelectionSort():
    print("Selection Sorting")
    listSize = get_listSize()
    randomList = generate_randomList(listSize)
    print(randomList)

def main():

    sortOption = 1      
    while(sortOption != 'q'):
        print_menu()
        sortOption = get_menuInput()
        
        if (sortOption == 1 ): SelectionSort()
        elif (sortOption == 2): print("Bubble Sort")
        elif (sortOption == 3): print("Insertion Sort")
        elif (sortOption == 4): print("Merge Sort")
        elif (sortOption == 5): print("Quick Sort")
        
    
    

if __name__ == "__main__":
    main()
