import numpy
import math

class Node:
    # def __init__(self,sequense):
    #     self.sequense=sequense
    #     self.leftchild=None
    #     self.rightchild=None

    def __init__(self,sequense,leftchild,rightchild):
        self.sequense=sequense 
        self.leftchild=leftchild
        self.rightchild=rightchild

def global_align(x, y, s_match, s_mismatch, s_gap):
    A = []
    for i in range(len(y) + 1):
        A.append([0] * (len(x) +1))
    for i in range(len(y)+1):
        A[i][0] = s_gap * i
    for i in range(len(x)+1):
        A[0][i] = s_gap * i
    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):

            A[i][j] = max(
            A[i][j-1] + s_gap,
            A[i-1][j] + s_gap,
            A[i-1][j-1] + (s_match if (y[i-1] == x[j-1] and y[i-1] != '-') else 0) +(s_mismatch if (y[i-1] != x[j-1] and y[i-1] != '-' and x[j - 1] != '-') else 0) +(s_gap if (y[i-1] == '-' or x[j - 1] == '-') else 0)
            )

    align_X = ""
    align_Y = ""
    i = len(x)
    j = len(y)

    while i > 0 or j > 0:

        current_score = A[j][i]

        if i > 0 and j > 0 and (
            ((x[i - 1] == y[j - 1] and y[j-1] != '-') and current_score == A[j - 1][i - 1] + s_match)  or 
            ((y[j-1] != x[i-1] and y[j-1] != '-' and x[i - 1] != '-') and current_score == A[j - 1][i - 1] +s_mismatch) or
            ((y[j-1] == '-' or x[i - 1] == '-') and current_score == A[j - 1][i - 1] + s_gap)
            ):
            align_X = x[i - 1] + align_X
            align_Y = y[j - 1] + align_Y
            i = i - 1
            j = j - 1
        elif i > 0 and (current_score == A[j][i - 1] + s_gap):
            align_X = x[i - 1] + align_X
            align_Y = "-" + align_Y
            i = i - 1      
        else:
            align_X = "-" + align_X
            align_Y = y[j - 1] + align_Y
            j = j - 1
    return (align_X, align_Y,A[len(y)][len(x)])

def findconsensus(sequenses):
    consensus =""
    for char in range(len(sequenses[0])):
        charlist = []
        for s in sequenses:
            if (s[char] == '-'):
                charlist.append('}}')
            else:
                charlist.append(s[char])
        minchar = min(charlist)
        if (minchar=='}}'):
            minchar = '-'
        consensus += min(charlist)
    
    return consensus

def makeDistanceMatrix(leafs):
    distanceMatrix =[[0 for c in range(len(leafs))] for r in range(len(leafs))]
    distanceMatrixMax = [0 for c in range(len(leafs))]
    for i in range(len(leafs)):
        for j in range(len(leafs)):
            if (i==j):
                distanceMatrix[i][j] =None
                distanceMatrixMax[i] +=0
            elif (distanceMatrix[j][i] == 0):
                distanceMatrix[i][j] = global_align(leafs[i].sequense,leafs[j].sequense,1,-1,-2)[2]
                distanceMatrixMax[i] +=distanceMatrix[i][j]
            else:
                distanceMatrix[i][j] = distanceMatrix[j][i]
                distanceMatrixMax[i] +=distanceMatrix[i][j]

    return distanceMatrix,distanceMatrixMax

def makeNewDM (leafs,distanceMatrix,distanceMatrixMax):
    
    newdistancematrix = [[0 for c in range(len(leafs))] for r in range(len(leafs))]
    mininnew = [[999999999,None,None]]
    for i in range(len(leafs)):
        for j in range(len(leafs)):
            if (i!=j):
                newdistancematrix[i][j] = distanceMatrix[i][j] - ((distanceMatrixMax[i] + distanceMatrixMax[j])/(len(leafs)-2))
                if (mininnew[0][0]>newdistancematrix[i][j]):
                    mininnew=[[newdistancematrix[i][j],i,j]]
                elif (mininnew[0][0] == newdistancematrix[i][j]):
                    mininnew.append([newdistancematrix[i][j],i,j])
    
    print(mininnew)
    if(len(mininnew) >1):
        temp=mininnew[0]
        minnum=min(temp[1],temp[2])
        for elem in mininnew:
            if (elem[1]<minnum) or (elem[2]<minnum):
                temp = elem
                minnum=min(temp[1],temp[2])
        
        mininnew=temp

    return newdistancematrix,mininnew



def __main__():
    
    # print (global_align('HVLIP','HVLP',1,-1,-2))

    # seqnumber = int(input())
    seqnumber = 4

    # sequenses = []
    sequenses = ['HVLIP','HMIP','HVLP','LVLIP']

    # for i in range(seqnumber) :
    #     sequenses.append(input())
    # print (sequenses)
    leafs = []
    for seq in sequenses:
        leafs.append( Node(seq,None,None) )
    # for leaf in leafs:
    #     print(leaf.sequense)
    # print(len(newnodes))
    while seqnumber>1:
    # while len(leafs)>1:
        # seqnumber=2
        
        # distanceMatrix =[[0 for c in range(seqnumber)] for r in range(seqnumber)]
        # distanceMatrixMax = [0 for c in range(seqnumber)]
        # for i in range(seqnumber):
        #     for j in range(seqnumber):
        #         if (i==j):
        #             distanceMatrix[i][j] =None
        #             distanceMatrixMax[i] +=0
        #         elif (distanceMatrix[j][i] == 0):
        #             distanceMatrix[i][j] = global_align(sequenses[i],sequenses[j],1,-1,-2)[2]
        #             distanceMatrixMax[i] +=distanceMatrix[i][j]
        #         else:
        #             distanceMatrix[i][j] = distanceMatrix[j][i]
        #             distanceMatrixMax[i] +=distanceMatrix[i][j]

        distanceMatrix,distanceMatrixMax = makeDistanceMatrix(leafs)
                
        print(distanceMatrix)
        print(distanceMatrixMax)

        # newdistancematrix = [[0 for c in range(seqnumber)] for r in range(seqnumber)]
        # mininnew = [999999999,None,None]
        # for i in range(seqnumber):
        #     for j in range(seqnumber):
        #         if (i!=j):
        #             newdistancematrix[i][j] = distanceMatrix[i][j] - ((distanceMatrixMax[i] + distanceMatrixMax[j])/(seqnumber-2))
        #             if (mininnew[0]>newdistancematrix[i][j]):
        #                 mininnew=[newdistancematrix[i][j],i,j]
        newdistancematrix,mininnew = makeNewDM(leafs,distanceMatrix,distanceMatrixMax)

        print (newdistancematrix)
        print (mininnew)
        
        newalignment = global_align(sequenses[mininnew[1]],sequenses[mininnew[2]],1,-1,-2)
        # print(sequenses[1][3]) 

        print (findconsensus(['abcd','-avf','jd-e']))


        seqnumber =1

    
    
    # distanceMatrix1 = distanceMatrix
    # guidetree = []
    # for c in range(math.ceil(seqnumber/2)):
    #     minInDistanceM = [99999999,0,0]
    #     for i in range(seqnumber):
    #         for j in range(seqnumber):
    #             if ((i!=j) and distanceMatrix1[i][j]<minInDistanceM[0] and distanceMatrix1[i][j]!=None):
    #                 minInDistanceM = [distanceMatrix1[i][j],i,j]
    #     # dis
    #     guidetree.append(minInDistanceM[1])
    #     guidetree.append(minInDistanceM[2])




__main__()


