

from typing import Sequence

def printMatrix(matrix):
    for row in matrix:
        print(row)  

def probabilityMatrix(sequences):

    seqlen= len(sequences[0])
    pseudocount = 1

    probMat = {}
    alphabet = []

    for seq in sequences:
        for c in seq:
            if not (c in alphabet):
                alphabet.append(c)
    
    for char in alphabet:
        probMat[char] = [0 for i in range(seqlen+1)]
    
    for i in range(len(sequences)):
        seq = sequences[i]
        for c in seq:
            probMat[c][i]+=1
    
    for char in alphabet:
        probMat[char][seqlen] = sum(probMat[char][0:seqlen])
    
    print(probMat)

    for char in alphabet:
        for i in range(seqlen):
            ## B is thought to be alphabet Characters
            probMat[char][i] = (probMat[char][i] + pseudocount)/( len(sequences) + (len(alphabet)*pseudocount))
    
    # print(probMat)
    return alphabet, probMat



def findProfile(query,alphabet,probMat,seqLen):
    
    for i in range(len(query)-seqLen+1):
        print(query[i])
    
    



def __main__():
    numberOfSequenses = int(input())
    sequences = []
    for i in range(numberOfSequenses):
        sequences.append(input())
    
    querySeq = input()
    # printMatrix(sequences)

    seqLen=len(sequences[0])
    alphabet, probMat = probabilityMatrix(sequences)

    findProfile(querySeq,alphabet,probMat,seqLen)

    
    
    

__main__()