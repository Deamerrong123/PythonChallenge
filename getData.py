def getData():
	data = []
	with open("hiddenTest.txt",'r') as f:
		tex = f.read()
		for num in tex[2:-2].split(','):
			data.append(int(num))
	return data

#print(data[:5])


