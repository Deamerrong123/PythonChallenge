def firstDuplicate(a):
        Index = []
        for i in range(len(a)-1):
                if a[i:].count(a[i]) > 1:
                        Index.append((a[i+1:].index(a[i])+i+1,str(a[i])))
        if len(Index) > 0:
                return int(min(Index)[1])
        return -1


def firstDuplicate2(a):
        start = 0
        end = len(a)-1

        while(start < end):
                if (a[start:end].count(a[start]) > 1):
                      Index = a[start+1:].index(a[start]) + start+1
                      if Index < end:
                              end = Index
                start += 1

        if (end == (len(a)-1)):
                return -1
        return a[end]
                        

def firstDuplicate3(a):
    Index = []
    for i in range(len(a)):
        if a.count(a[i]) > 1:
            if a[i] in Index:
                return a[i]
            Index.append(a[i])
    return -1             


def firstDuplicate4(a):
        Index = [i for i in a if a.count(i)>1]
        return Index













        
