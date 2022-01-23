# Program created on 1/22/2022 by Uriel GC
# Takes a list of items where last 4 columns are int, returning a sequence of G,C,T,A

# Modules
import argparse


# Func. def. mapSeq()
# Signature: str -> str
# interp. map columns with frequencies from 
# nucleotides into letters based on index of their headers
def mapSeq(file):
    with open(file, 'r') as file:
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
        

if __name__ == "__main__":
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True,
        help="file to process")
    args = vars(ap.parse_args())
    print(args)
    mapSeq(args["file"])
