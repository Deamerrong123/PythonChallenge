def firstDuplicate(a):
        Index = []
        for i in range(len(a)-1):
                if a[i:].count(a[i]) > 1:
                        Index.append((a[i+1:].index(a[i]),str(a[i])))
        if len(Index) > 0:
                return int(min(Index)[1])
        return -1


def firstDuplicate2(a):
        start = 0
        end = len(a)-1

        while(start < end):
                if (a[start:end].count(a[start]) > 1):
                      Index = a[start+1:].index(a[start]) + start
                      if Index < end:
                              end = Index
                start += 1

        if (end == (len(a)-1)):
                return -1
        return a[end]
                        
                        
        
