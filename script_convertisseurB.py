def convertirEnBinaire(num):
	list = []
	while num > 0:
		if (num % 2) == 0:#si divisible par 2
			list.append(0)
		else:
			list.append(1)
		num//=2 #division euclidienne par 2
	return int(''.join(map(str, list[::-1])))

#la ligne ci-dessus correspond à ceci en plus compact,
#parce que c'est plus fun en une seule ligne :
#si list = [3, 2, 1]
#s = map(str, list[::-1])	-> ['1','2','3']
#s = ''.join(s)				-> '123'
#s = int(s)					-> 123
#return s

print convertirEnBinaire(256)
