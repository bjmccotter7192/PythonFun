import numpy as np
from tabulate import tabulate as tb

def printTableForm(valueList, headerList):
    return tb(valueList, headers=headerList)

def getSizeForMatrix():
    x = int(input("Please specify how many rows: \n"))
    y = int(input("Please specify how many columns: \n"))
    return [x, y]

def getHeaderValues(columns):
    nameList = []
    for i in range(columns):
        nameList.append("Column" + str(i + 1))

    return nameList

### Get values for inputs and weights
#inputs = getSizeForMatrix()
##weights = getSizeForMatrix()

### Create Matrix to push through network
#inputsMatrix = np.random.random_sample((inputs[0], inputs[1]))
weightsMatrix = np.random.random_sample((3, 3))
biasMatrix = np.random.random_sample((3,1))

# print("Inputs Matrix \n")
# print(printTableForm(inputsMatrix, getHeaderValues(inputs[1])))

# print("Weights Matrix \n")
# print(printTableForm(weightsMatrix, getHeaderValues(weights[1])))

# print("\nPRINTING FROM LOOP:")
# for x in range(len(weightsMatrix)):
#     for y in range(len(weightsMatrix[0])):
#         print(weightsMatrix[y][x])

print("PRINTING FROM LOOP:")
print("===================")
print("Weight1\t\t\tWeight2\t\t\tWeight3\t\t\tBias")
for x in range(len(weightsMatrix)):
    for y in range(len(weightsMatrix[0])):
        print(str(weightsMatrix[x][y]) + "\t", end = '')
    
    print(str(biasMatrix[x]))

print('\n')

# print("  Number 1   Number 2   Number3")
# print(weightsMatrix)