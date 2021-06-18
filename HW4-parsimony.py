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
                    sv[nodes.index(nod)][alpha] = 999999
    
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
                minSon =[99999999,None]
                for child in nod.children:
                    minSVson = min(sv[nodes.index(child)].items(), key=lambda x: x[1])
                    price=0
                    if alpha != minSVson[0] : 
                        price = 1
                    if minSon[0] > minSVson[1]+price:
                        minSon = [minSVson[1]+price,minSVson[0]]
                sv[nodes.index(nod)][alpha] = minSon[0]
    
    return min(sv[0].items(), key=lambda x: x[1])

            
    
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
    
    for i in range(seqLength):
        print(smallParsimony(nodes,i))




__main__()