def firstDuplicate(a):
        Index = []
        for i in range(len(a)-1):
            if a[i:].count(a[i]) > 1:
		Index.append((a[i+1:].index(a[i]),str(a[i]))
		
