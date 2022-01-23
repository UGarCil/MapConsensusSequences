# Program created on 1/22/2022 by Uriel GC
# Takes a list of items where last 4 columns are int, returning a sequence of G,C,T,A

# Modules
import pandas as pd
import random
# Data def CSV
# csv = pd.read_csv(str)
# interp. csv file


with open('test.txt', 'r') as file:
    file = file.readlines()
    headers = file[0].strip().split('\t')[-4:]
    content = [x.strip().split('\t') for x in file[1:]]
    content = [x[-4:] for x in content]
    content = [[int(cell) for cell in row] for row in content]
        
            
sequence = ''
for row in content:
    # print(row)
    index = row.index(max(row))
    sequence += headers[index]

print(sequence)
        
