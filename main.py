def sumFormula(array1, lengthArray):
    total = int(((lengthArray + 1) * (lengthArray + 2)) / 2) # The sum of all the numbers
    for i in range(0, lengthArray):
        total = total - array1[i] # Find the missing number by subtracting
    print("The missing number is " + str(total))


def sum2(array2, lengthArray, min, max):
    totalOfArray = 0
    total = 0
    for i in range(0, lengthArray): # The sum of numbers from the passed array
        totalOfArray += array2[i]
    for i in range(min, max + 1):
        total = total + min # The sum of number from min to max
        min += 1
    print("The missing number is " + str(total - totalOfArray)) # Find the missing number by subtracting


def search(array3, min, max): # Search and iterate
    for j in range(min, max + 1):
        if j in array3:
            continue
        else:
            return j


def XOR(array4, lengthArray, min, max):
    array_complete = [] # Initialise array
    x1 = 0 # Store the XOR number

    for q in range(min, max + 1): # The sum of all the number from min to max
        array_complete.append(q)
    for j in range(lengthArray): # XOR the number and store it
        x1 = x1 ^ array4[j]
    # XOR again to find the number this is because a ^ a =0
    # which mean the same number XOR with the same number will become 0 (None or Null)
    for g in range(lengthArray + 1):
        x1 = x1 ^ array_complete[g]

    return x1 # Result


print("Which approach?")
print("1) Approach 1(The number must start from 1)")
print("2) Approach 2(All the number must come from the range)")
print("3) Approach 3(Slow)")
print("4) Approach 4(Fast and Efficient)")
print("5) Exit")

# Menu
while True:
    choice = int(input("Choice: "))
    if choice == 1:
        array = [4, 2, 3, 5, 6, 7, 8, 9]
        sumFormula(array, len(array))
    elif choice == 2:
        array = [14, 15, 13, 11]
        min = 11
        max = 15
        sum2(array, len(array), min, max)
    elif choice == 3:
        array = [11, 12, 13, 14]
        min = 11
        max = 15
        print("The missing number is " + str(search(array, min, max)))
    elif choice == 4:
        array = [99, 101, 102, 100, 104, 105]
        min = 99
        max = 105
        print("The missing number is " + str(XOR(array, len(array), min, max)))
    elif choice == 5:
        break
