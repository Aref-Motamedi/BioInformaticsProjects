aminoAcid =['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','X','Z','J','U']
dnaPro = ['A','T','C','G']

def printMatrix(matrix):
    for row in matrix:
        print(row) 

def returnScore(elem):
    return elem[1]  

def probabilityMatrix(sequences):

    seqlen= len(sequences[0])
    pseudocount = 1

    probMat = {}
    alphabet = dnaPro

    for seq in sequences:
        for c in seq:
            if not (c in alphabet):
                alphabet = aminoAcid
    alphabet.append('-')
    
    
    for char in alphabet:
        probMat[char] = [0 for i in range(seqlen+1)]
    
    for i in range(len(sequences)):
        seq = sequences[i]
        for c in range(seqlen):
            probMat[seq[c]][c]+=1
    
    for char in alphabet:
        probMat[char][seqlen] = sum(probMat[char][0:seqlen])
    
    # print(probMat)

    for char in alphabet:
        for i in range(seqlen):
            ## B is thought to be alphabet Characters
            probMat[char][i] = (probMat[char][i] + pseudocount)/( len(sequences) + ((len(alphabet)-1)*pseudocount))
    
    # print(probMat)
    return alphabet, probMat




def findProfile(query,alphabet,probMat,seqLen):
    scores = [[None,0] for i in range(len(query)-seqLen+1) ]
    for i in range(len(query)-seqLen+1):
        
        flag = True

        for j in range(seqLen):
            if not(query[i+j] in alphabet):
                flag=False
        
        if (flag == True):
            for j in range(seqLen):
                scores[i][1] += probMat[query[i+j]][j]
        else:
            scores[i][1] = None
        scores[i][0] = query[i:i+seqLen]
    
    scores.sort(key=returnScore,reverse=True)
    return scores[0]
        
    



def __main__():
    numberOfSequenses = int(input())
    sequences = []
    for i in range(numberOfSequenses):
        sequences.append(input())
    
    querySeq = input()
    # printMatrix(sequences)

    seqLen=len(sequences[0])
    alphabet, probMat = probabilityMatrix(sequences)

    # print(probMat)

    profile = findProfile(querySeq,alphabet,probMat,seqLen)
    print(profile[0])
    
    
    

__main__()