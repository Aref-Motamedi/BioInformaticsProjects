import numpy
import math
from collections import Counter


def returnchar(obj):
    return obj[0]


class Node:
    

    def __init__(self,sequense,leftchild,rightchild,number=None):
        self.sequense=sequense 
        self.leftchild=leftchild
        self.rightchild=rightchild
        self.number=number

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
            if (i!=j) and len(leafs)>2:
                newdistancematrix[i][j] = distanceMatrix[i][j] - ((distanceMatrixMax[i] + distanceMatrixMax[j]) / (len(leafs)-2))
                if (mininnew[0][0]>newdistancematrix[i][j]):
                    mininnew=[[newdistancematrix[i][j],i,j]]
                elif (mininnew[0][0] == newdistancematrix[i][j]):
                    mininnew.append([newdistancematrix[i][j],i,j])
            elif len(leafs)<=2:
                mininnew=[[0,0,1]]
    # print("&&&&&&&&&&&&&&&&&&&&&")
    # for row in newdistancematrix:
    #     print(row)
    # print("$$$$$$")
    # for row in distanceMatrix:
    #     print(row)
    # print("$$$$$$")
    # print(mininnew)
    if(len(mininnew) >1):
        temp=mininnew[0]
        minnum=min(temp[1],temp[2])
        for elem in mininnew:
            if (elem[1]<minnum) or (elem[2]<minnum):
                temp = elem
                minnum=min(temp[1],temp[2])
        
        mininnew=temp
    else:
        mininnew = mininnew[0]

    # print(leafs[mininnew[1]].sequense ," ### ", leafs[mininnew[2]].sequense)

    return newdistancematrix,mininnew

def updateDistanceMatrix(leafs,distanceMatrix,distanceMatrixMax,mininnew,distancesToMinNodes):

    # distanceMatrix1 =[[0 for c in range(len(leafs))] for r in range(len(leafs))]
    distanceMatrix1 = []
    # distanceMatrixMax1 = [0 for c in range(len(leafs))]
    distanceMatrixMax1 =[]
    for i in range(len(distanceMatrix)):
        dist_Arr = []
        if (i != mininnew[1] and i != mininnew[2]):
                
            for j in range(len(distanceMatrix)):
                # if (i==j):
                #     distanceMatrix1[i][j] =None
                #     distanceMatrixMax1[i] +=0
                # elif (distanceMatrix1[j][i] == 0):
                #     distanceMatrix1[i][j] = global_align(leafs[i].sequense,leafs[j].sequense,1,-1,-2)[2]
                #     distanceMatrixMax1[i] +=distanceMatrix1[i][j]
                # else:
                #     distanceMatrix1[i][j] = distanceMatrix1[j][i]
                #     distanceMatrixMax1[i] +=distanceMatrix1[i][j]

                if (j != mininnew[1] and j != mininnew[2]):
                    dist_Arr.append(distanceMatrix[i][j])
            sumnum =0
            
            for j in range(len(dist_Arr)):
                if (dist_Arr[j] != None):
                    sumnum += dist_Arr[j]
            
            distanceMatrix1.append(dist_Arr)
            distanceMatrixMax1.append(sumnum)


    # print("hoyooooyyy ",len(distanceMatrix1),len(distanceMatrix1[0]),len(leafs))

    # sau = (distanceMatrix[mininnew[1]][mininnew[2]] / 2) + ((distanceMatrixMax[mininnew[1]] - distanceMatrixMax[2]) / (2(len(leafs) - 2))) 
    # sbu = (distanceMatrix[mininnew[1]][mininnew[2]] - sau)
    
    dist_Arr = []
    maxnum=0
    for i in range(len(leafs)-1):
        
        distanceMatrix1[i].append( (distancesToMinNodes[0][i] + distancesToMinNodes[1][i] - distanceMatrix[mininnew[1]][mininnew[2]])/2 )
        # distanceMatrix1[len(leafs)-1][i] = distanceMatrix1[i][len(leafs)-1]
        dist_Arr.append( distanceMatrix1[i][len(leafs)-1] )
        distanceMatrixMax1[i] +=distanceMatrix1[i][len(leafs)-1]
        # distanceMatrixMax1[len(leafs)-1] +=distanceMatrix1[i][len(leafs)-1]
        maxnum +=distanceMatrix1[i][len(leafs)-1]

    
    distanceMatrix1.append(dist_Arr)
    distanceMatrixMax1.append(maxnum)


    distanceMatrix1[len(leafs)-1].append(None)

    # distanceMatrix = distanceMatrix1
    # distanceMatrixMax = distanceMatrixMax1
    return distanceMatrix1,distanceMatrixMax1



def updateConsensus(inputnode,consensus,sequenses):
    if (inputnode.leftchild != None):
        updateConsensus(inputnode.leftchild,consensus,sequenses)
    if (inputnode.rightchild != None):
        updateConsensus(inputnode.rightchild,consensus,sequenses)
    newseq=""
    counter=0
    for char in consensus:
        # print(inputnode.sequense , " /// ", consensus, " /// ",char," /// ",newseq, " /// ", counter)
        if (counter>=len(inputnode.sequense)):
            newseq += '-'
        elif (char == '-' and inputnode.sequense[counter] != '-'):
        # if (char == '-' and inputnode.sequense[counter] != '-'):
            newseq+='-'
        else:
            newseq += inputnode.sequense[counter]
            counter +=1
    # print('new: ',newseq," /old: ",inputnode.sequense)
    inputnode.sequense=newseq

    if ((inputnode.leftchild == None) and (inputnode.rightchild == None)):
        sequenses.append(inputnode.sequense)



def doAlignmentInTree (leafs,mininMD):
    leftnode= leafs[mininMD[1]]
    rightnode= leafs[mininMD[2]]
    # print(" /// LEFT: ",leftnode.sequense, "       /// RIGHT: ",rightnode.sequense)
    
    alignmentresult = global_align(leftnode.sequense,rightnode.sequense,1,-1,-2)

    consensusarray = []
    updateConsensus(leftnode,alignmentresult[0],consensusarray)
    updateConsensus(rightnode,alignmentresult[1],consensusarray)
    # if (rightnode.number !=None and leftnode.number != None):
    #     if (leftnode.number == 0 or leftnode.number == 4):
    #         if (rightnode.number == 0 or rightnode.number == 4):
    # print ("kkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    # print (consensusarray)
    # print(alignmentresult[0])
    # print(alignmentresult[1])

    # print(consensusarray)

    cons = findconsensus(consensusarray)

    # print(" /// CONS /// ",cons)

    parentNode = Node(cons,leftnode,rightnode)
    leafs.append(parentNode)
    leafs.remove(leftnode)
    leafs.remove(rightnode)
    return consensusarray



def findconsensus(sequenses):
    consensus =""
    for char in range(len(sequenses[0])):
        charlist = []
        for s in sequenses:
            if (s[char] == '-'):
                charlist.append('}}')
            else:
                charlist.append(s[char])
        
        

        words_to_count = (word for word in charlist if word[:1].isupper())
        counterlist = Counter(words_to_count)
        charlist =counterlist.most_common(10) 
        # maxnumber =0
        charlist.sort(key= returnchar)

        # char_counter = {}
        # for ch in charlist:
        #     if ch in char_counter:
        #         char_counter[ch] +=1
        #     else:
        #         char_counter[ch] =1
        # char_counter = sorted(char_counter,key=char_counter.get , reverse=True)

        # print("=================")
        # print(char_counter)

        # minchar = char_counter[0]
        # if (minchar=='}}' and len(char_counter)>1 ):
        #     minchar = char_counter[1]
        # if (minchar=='}}'):
        #     minchar = '-'
        
        minchar = charlist[0][0]
        if (minchar=='}}'):
            minchar = '-'
        consensus += minchar
    
    return consensus


def scoringMSA(msa):
    numberOfSequenses = len(msa)
    
    msaScore = 0
    for char in range(len(msa[0])):

        for c1 in range(numberOfSequenses):
            for c2 in range(numberOfSequenses):
                if (c1 < c2):
                    if (msa[c1][char] == '-' or msa[c2][char] == '-'):
                        msaScore +=-2
                    elif (msa[c1][char] ==msa[c2][char]):
                        msaScore +=1
                    else:
                        msaScore +=-1
    
    return msaScore

def findingMSA(node):
    msa = []
    if (node.leftchild != None):
        res = findingMSA(node.leftchild)
        if (len(res) !=0):
            for item in res:
                msa.append(item)
    if (node.rightchild != None):
        res = findingMSA(node.rightchild)
        if (len(res) !=0):
            for item in res:
                msa.append(item)
    if (node.number != None):
        # print(node.number)
        msa.append(node)
    return msa
        
def returnnumber(leaf):
    return leaf.number


def __main__():
    
    # print (global_align('HVLIP','HVLP',1,-1,-2))

    seqnumber = int(input())
    # seqnumber = 4

    sequenses = []
    # sequenses = ['HVLIP','HMIP','HVLP','LVLIP']

    for i in range(seqnumber) :
        sequenses.append(input())
    # print (sequenses)
    leafs = []
    for seq in sequenses:
        leafs.append( Node(seq,None,None,sequenses.index(seq)) )
    # for leaf in leafs:
    #     print(leaf.sequense)
    # print(len(newnodes))
    # while seqnumber>1:
    distanceMatrix = None
    distanceMatrixMax = None

    while len(leafs)>1:
        

        if (distanceMatrix == None and distanceMatrixMax == None):
            distanceMatrix,distanceMatrixMax = makeDistanceMatrix(leafs)
        # distanceMatrix,distanceMatrixMax = makeDistanceMatrix(leafs)
                
        # print(distanceMatrix)
        # print(distanceMatrixMax)

        
        newdistancematrix,mininnew = makeNewDM(leafs,distanceMatrix,distanceMatrixMax)

        # print (newdistancematrix)
        # print (mininnew)

        distancesToMinNodes = [[],[]]
        for i1 in range(len(leafs)):
            if (i1 != mininnew[1] and i1 != mininnew[2]):
                distancesToMinNodes[0].append(distanceMatrix[mininnew[1]][i1])
                distancesToMinNodes[1].append(distanceMatrix[mininnew[2]][i1])
        
        # print(distancesToMinNodes)
        # print("*************************")
        # for row in distanceMatrix:
        #     print(row)
        # print("*************************")
        
        # print(distanceMatrixMax)


        # print('----------------------------------')
        # print('leafs (before):')
        # for leaf in leafs:
        #     print(leafs.index(leaf),"-----",leaf.sequense , "--",leaf.rightchild, "--",leaf.leftchild)

        msa = doAlignmentInTree(leafs,mininnew)

        # print('----------------------------------')
        # print('leafs (after):')
        # for leaf in leafs:
        #     print(leafs.index(leaf),"-----",leaf.sequense , "--",leaf.rightchild, "--",leaf.leftchild)

        distanceMatrix,distanceMatrixMax = updateDistanceMatrix(leafs,distanceMatrix,distanceMatrixMax,mininnew,distancesToMinNodes)

        # print(distanceMatrix)
        # print(distanceMatrixMax)

        
        if len(leafs)==1:
            msssa = findingMSA(leafs[0])
            msssa.sort(key=returnnumber)
            for ll in msssa:
                print(ll.sequense)
            print(scoringMSA(msa))


    


__main__()


