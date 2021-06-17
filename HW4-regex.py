
aminoAcid =['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','X','Z','J','U']


def newInputRegex(inputregex):
    newRegex = []
    for item in inputregex:
        if '(' in item:
            firstparindex = item.index('(')

            num = int(item[firstparindex+1:-1])
            # print(num)
            for i in range(num):
                newRegex.append(getCharacters(item[:firstparindex]))
        else:
            newRegex.append(getCharacters(item))
    return newRegex

def getCharacters(string):
    result = []
    if string == 'X':
        result = aminoAcid
    elif string.startswith('['):
        for i in range(len(string)-2):
            result.append(string[i+1])
    elif string.startswith('{'):
        result = aminoAcid
        for i in range(len(string)-2):
            result.remove(string[i+1])
    else:
        result.append(string)
    return result




def __main__():

    inputRegex = input().split('-')

    numberOfSeq = int(input())
    sequences = []
    for i in range(numberOfSeq):
        sequences.append(input())

    
    # inputRegex = '[AS]-D-[IVL]-G-X(4)-{PG}-C-[DE]-R-[FY](2)-Q'.split('-')
    # numberOfSeq = 4
    # sequences = ['ATLGAVFALCDRYFQ','WDVGPRSCFCDREYR','ADWGRTQNRCDCYYQ','ADIGQPHSLCERYFQ']

    inputcharachters = newInputRegex(inputRegex)

    result = []
    for seqNumber in range(numberOfSeq):
        seq = sequences[seqNumber]
        seqResult = ''
        faultNumber = 0
        for aminoNumber in range(len(seq)):
            if seq[aminoNumber] in inputcharachters[aminoNumber]:
                seqResult += '1'
            else:
                seqResult += '0'
                faultNumber += 1
            
        result.append([seqResult,faultNumber])
        if (faultNumber>2):
            print('No',seqResult)
        else:
            print('Yes',seqResult)



    # print(inputcharachters)
    # print(getCharacters('K'))

__main__()