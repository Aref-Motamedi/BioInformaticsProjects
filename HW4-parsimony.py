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
    for nod in nodes:
        if (not nod.leaf):
            flag = True
            for child in nod.children:
                if tag[nodes.index(child)] ==1:
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
            flag = False
        else:
            tag[nodes.index(nod)] = 1
            for alpha in alphabet:
                print("k")
            





    
def __main__():

    numberOfNodes = int(input())
    nodes = []
    for i in range(numberOfNodes):
        nodes.append(Node())
    for i in range(numberOfNodes-1):
        inp = input().split(" ")
        nodes[int(inp[0])].addChild(nodes[int(inp[1])])
    
    numberOfLeaves = int(input())
    for i in range(numberOfLeaves):
        inp = input().split(" ")
        nodes[int(inp[0])].addSeq(inp[1])
    
    # for nod in nodes:
    #     print(nodes.index(nod),nod.children,nod.sequence)





__main__()