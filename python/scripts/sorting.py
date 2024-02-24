# Interactive Sorting

import sys 
from random import randint


def print_menu():
    print("*" * 50)
    print(" Interactive Python Sorting ")
    print(" 1. Selection Sort")
    print(" 2. Bubble Sort")
    print(" 3. Insertion Sort")
    print(" 4. Merge Sort")
    print(" 5. Quick Sort")
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
    print(f"Random List: {randomList}")
    
    for i in range(len(randomList)):
        smallestIndex = i
        print(f"Pass {i+1}")
        for j in range(i + 1, len(randomList)):
            if randomList[j] < randomList[smallestIndex]: 
                smallestIndex = j
        #swap
        randomList[i], randomList[smallestIndex] = randomList[smallestIndex], randomList[i]
        print(randomList)

    print(f"FINAL: {randomList}")

def BubbleSort():
    print("Bubble Sorting")
    listSize = get_listSize()
    randomList = generate_randomList(listSize)
    print(f"Random List: {randomList}")

    swap = True
    passthru = 1
    while (swap):
        swap = False
        for i in range(len(randomList) - 1):
            print(i)
            if (randomList[i+1] < randomList[i]): 
                randomList[i], randomList[i+1] = randomList[i+1], randomList[i]
                print(f"Bubble swap: {randomList}")
                swap = True
        print(f"Pass {passthru}:  {randomList}")
        passthru += 1

def InsertionSort():
    print("Insertion Sorting")
    listSize = get_listSize()
    randomList = generate_randomList(listSize)
    print(f"Random List: {randomList}")

    for i in range(len(randomList)):
        j = i
        while j > 0:
            if randomList[j] < randomList[j-1]:
                randomList[j], randomList[j-1] = randomList[j-1], randomList[j]
                print(f"Insertion swap: {randomList}" )
            j-=1
        print(f"Pass {i + 1}")
    print(randomList)

def MergeSort():
    print("Merge Sorting")
    listSize = get_listSize()
    randomList = generate_randomList(listSize)
    print(f"Random List: {randomList}")

    finalList = mergesort(randomList)
    print(finalList)

def mergesort(arr):
    if len(arr) == 1: return arr

    arr1 = []
    arr2 = []
    
    i = 0
    while(i < int(len(arr)/2)):
        arr1.append(arr[i])
        i += 1
    
    j = int(len(arr)/2)
    while(j < len(arr)):
        arr2.append(arr[j])
        j += 1

    arr1 = mergesort(arr1)
    arr2 = mergesort(arr2)

    return merge(arr1, arr2)

def merge(arr1, arr2):
    temparr = []

    while( arr1 and arr2):
        if arr1[0] > arr2[0]:
            temparr.append(arr2.pop(0))
        else:
            temparr.append(arr1.pop(0))

    while (arr1): 
        temparr.append(arr1.pop(0))
    while (arr2):
        temparr.append(arr2.pop(0))

    return temparr
    
def QuickSort():
    print("Quick Sorting")
    listSize = get_listSize()
    randomList = generate_randomList(listSize)
    print(f"Random List: {randomList}")



def main():

    sortOption = 1      
    while(sortOption != 'q'):
        print_menu()
        sortOption = get_menuInput()
        
        if (sortOption == 1 ): SelectionSort()
        elif (sortOption == 2): BubbleSort()
        elif (sortOption == 3): InsertionSort()
        elif (sortOption == 4): MergeSort()
        elif (sortOption == 5): QuickSort()
        
    
    

if __name__ == "__main__":
    main()
