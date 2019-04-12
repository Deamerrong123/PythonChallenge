import json
def getData():
	data = []
	with open("hiddenTest.txt",'r') as f:
		tex = f.read()
		for num in tex[2:-2].split(','):
			data.append(int(num))
	return data


def getData2():
        data = []
        with open("hiddData.txt",'r') as f:
                tex = f.read()
                for num in tex[2:-1].split(','):
                        data.append(int(num))
        return data

#data = getData2()
#print(data[-3:])

def getData3():
        with open('test-22.json','r') as f:
                Dic = json.load(f)
        Ip_a = Dic['input']
        data = Ip_a['a']

        return data


def getOutput():
        with open('test-22.json','r') as f:
                Dic = json.load(f)
        Op_a = Dic['output']
        #data = Ip_a['a']

        return Op_a

print(getOutput())
#data = getData3()
#print(len(data))

