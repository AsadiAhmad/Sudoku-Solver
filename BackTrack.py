import numpy as np

rows = 9
cols = 9
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

def checkList(myList):
    numList = [1,2,3,4,5,6,7,8,9]
    for element in myList:
        for num in numList:
            if element == num:
                numList.remove(num)
    if numList == []:
        return True, numList
    else:
        return False, numList

def checkAllRow(matrix2D):
    for i in range(rows):
        row = matrix2D[:,i]
        checked, _ = checkList(row)
        if checked == False:
            return False
    return True
        
def checkAllColumn(matrix2D):
    for i in range(cols):
        col = matrix2D[i,:]
        checked, _ = checkList(col)
        if checked == False:
            return False
    return True

def checkSquare(matrix2D):
    for m in range(3):
        for n in range(3):
            i = 3*m + 1
            j = 3*n + 1
            newList = []
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    newList.append(matrix2D[x,y])
            checked, _ = checkList(newList)
            if checked == False:
                return False
    return True

def checkStability(myList):
    zeroCount = 0
    for i in range(9):
        if myList[i] == 0:
            zeroCount += 1
    _, checkedList = checkList(myList)
    if len(checkedList) != zeroCount:
        return False
    return True

def stabilityAllRow(matrix2D):
    for i in range(rows):
        row = matrix2D[:,i]
        if checkStability(row) == False:
            return False
    return True
        
def stabilityAllColumn(matrix2D):
    for i in range(cols):
        col = matrix2D[i,:]
        if checkStability(col) == False:
            return False
    return True

def stabilitySquare(matrix2D):
    for m in range(3):
        for n in range(3):
            i = 3*m + 1
            j = 3*n + 1
            newList = []
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    newList.append(matrix2D[x,y])
            if checkStability(newList) == False:
                return False
    return True

# Scan input values for each element in the 2D array
for i in range(rows):
    values = input().split()
    for j in range(cols):
        matrix[i][j] = int(values[j])

matrix = np.array(matrix)


elementList = []
while(not(checkAllRow(matrix) and checkAllColumn(matrix) and checkSquare(matrix))):
    # if we have 0 we must trun it into 1
    getOut = False
    for i in range(rows):
        for j in range(cols):
            if matrix[i,j] == 0:
                matrix[i,j] = 1
                new = [1, [i,j]]
                elementList.append(new)
                getOut = True
                break
        if getOut:
            break
    # we should create a stable position each iteration
    getOut2 = False
    while (not(stabilityAllRow(matrix) and stabilityAllColumn(matrix) and stabilitySquare(matrix))):
        # check if conditions became false with value 9
        if (elementList[-1])[0] >= 9: # remove 9
            valueX = ((elementList[-1])[1])[0]
            valueY = ((elementList[-1])[1])[1]
            matrix[valueX, valueY] = 0
            elementList.pop()
            # if there is no element in list it means that matrix could not be solve
            if elementList == []:
                print("sudoko is wrong!")
                getOut2 = True
                break
            # increment last element
            valueElement = (elementList[-1])[0]
            valueX = ((elementList[-1])[1])[0]
            valueY = ((elementList[-1])[1])[1]
            matrix[valueX, valueY] = valueElement + 1
            (elementList[-1])[0] = valueElement + 1
        # check if conditions became false without value 9
        else :
            valueElement = (elementList[-1])[0]
            valueX = ((elementList[-1])[1])[0]
            valueY = ((elementList[-1])[1])[1]
            matrix[valueX, valueY] = valueElement + 1
            (elementList[-1])[0] = valueElement + 1
    if getOut2 == True:
        break
# print the matrix
print("Here is Solved Sudoku with BackTrack Algorithm")
for row in matrix:
    for element in row:
        print(str(element) + " ", end="")
    print()
    