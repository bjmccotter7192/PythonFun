import numpy as np
from tabulate import tabulate as tb

testArray = np.random.rand(10,10)
print(tb(testArray, 
        headers=[0,1,2,3,4,5,6,7,8,9], 
        tablefmt='orgtbl'))


# valueList = []
# headers = []
    
# table = PrettyTable()

# table.field_names = [0,1,2,3,4,5,6,7,8,9]

# table.add_row([1, random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random()])

# print(table)