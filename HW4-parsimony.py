alphabet = ['A','C','G','T']


class Node:

    def __init__(self):
        self.sequence=None 
        self.children = []
        self.leaf=True
        # self.tag=0
    def addSeq(self,sequence):
        self.sequence = sequence
    def addChild(self,newchild):
        if (self.leaf == True):
            self.leaf = False
        self.children.append(newchild)


def returnAparent(nodes,tag):
    
    # for nod in nodes:
    #     print(tag[nodes.index(nod)])

    for nod in nodes:
        if (tag[nodes.index(nod)] ==0):
            # print(nod.leaf)
            
            flag = True
            for child in nod.children:
                if tag[nodes.index(child)] ==0:
                    flag=False
            if flag==True:
                return nod
    return None


def smallParsimony(nodes,collumn):
    tag = [0 for i in range(len(nodes))]
    sv = [{'A': 0,'C' : 0,'G' : 0,'T' : 0} for i in range(len(nodes))]
    for nod in nodes:
        if (nod.leaf):
            tag[nodes.index(nod)] = 1
            for alpha in alphabet:
                if nod.sequence[collumn] == alpha:
                    sv[nodes.index(nod)][alpha] = 0
                else:
                    sv[nodes.index(nod)][alpha] = 1

    
    flag = True
    if 0 in tag:
        flag=False
    
    while (not flag):
        nod = returnAparent(nodes,tag)
        if (nod==None):
            flag = True
        else:
            tag[nodes.index(nod)] = 1
            for alpha in alphabet:
                minSon =0

                child1 = nod.children[0]
                child2 = nod.children[1]

                temp = min(sv[nodes.index(child1)].values())
                temp2 = min(sv[nodes.index(child2)].values())

                minForChild1 = 0
                minForChild2 = 0
                if (temp>sv[nodes.index(child1)][alpha]-2):
                    minForChild1 =sv[nodes.index(child1)][alpha]
                else:
                    minForChild1 = temp+1
                
                
                if (temp2>sv[nodes.index(child2)][alpha]-2):
                    minForChild2 =sv[nodes.index(child2)][alpha]
                else:
                    minForChild2 = temp2+1

                sv[nodes.index(nod)][alpha] = minForChild1 + minForChild2
            
            if(nod.sequence == None):
                nod.sequence = ''
            nod.sequence +=min(sv[nodes.index(nod)].items(), key=lambda x: x[1])[0]
    
    # print(collumn)
    # for nod in nodes:
    #     print(sv[nodes.index(nod)])
    # print()
    
    return min(sv[0].items(), key=lambda x: x[1])


def findDiff(seq1,seq2):
    diff = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            diff +=1
    return diff
    
def __main__():

    numberOfNodes = int(input())
    nodes = []
    for i in range(numberOfNodes):
        nodes.append(Node())
    for i in range(numberOfNodes-1):
        inp = input().split(" ")
        nodes[int(inp[0])].addChild(nodes[int(inp[1])])
    
    numberOfLeaves = int(input())
    seqLength = None
    for i in range(numberOfLeaves):
        inp = input().split(" ")
        nodes[int(inp[0])].addSeq(inp[1])
        seqLength = len(inp[1])    
    
    leastPrice = 0
    # resSeq = ''
    for i in range(seqLength):
        leastPrice += smallParsimony(nodes,i)[1]
        # resSeq += smallParsimony(nodes,i)[0]
    print(leastPrice)
    # print(resSeq)

    



__main__()