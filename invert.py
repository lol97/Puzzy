import numpy as np
data2 = [[7000000, 10000000, 7500000, 5000000, 17000000, 7000000, 14000000, 18000000, 40000000, 10000000, 11000000, 15000000, 8000000, 5000000, 10000000, 9000000, 7000000, 8000000, 6500000, 20000000, 4000000, 8000000, 8000000, 20000000, 40000000, 5000000, 25000000, 10000000, 10000000, 24000000, 10000000, 10000000, 10000000, 10000000, 8000000, 10000000, 8500000, 16000000, 8000000, 5000000, 15000000, 7500000, 25000000, 7000000, 9000000, 12000000, 8000000, 7500000],
		 [3000000, 4000000, 2000000, 1200000, 5000000, 2000000, 5000000, 5500000, 10000000, 4000000, 5000000, 6500000, 3000000, 1500000, 5500000, 1500000, 1000000, 2500000, 1000000, 7000000, 1500000, 2250000, 2500000, 5000000, 12000000, 1000000, 7000000, 2500000, 3000000, 10000000, 6000000, 5000000, 3500000, 5000000, 2500000, 5500000, 2500000, 6000000, 2000000, 1500000, 5000000, 2000000, 7000000, 3000000, 3000000, 4000000, 2000000, 2000000]
		]

# datanp = np.array(data2)
# datanpT = datanp.T
i =0
dataBaru=[]
temp1=[]
temp2=[]
while(i<7):
	
	temp1.append(data2[0][i])
	temp2.append(data2[1][i])
	i+=1
dataBaru.append(temp1)
dataBaru.append(temp2)
print(dataBaru)
# def clearFile(namaFile):
# 	namaFile = str(namaFile+'.txt')
# 	file = open(namaFile,'w')
# 	file.close()


# def insertFile(namaFile, data):
# 	data = list(map(list,zip(*data))) #transpose data
# 	namaFile = str(namaFile+'.txt')
# 	file = open(namaFile,'a')
# 	for y in data:
# 		temp = [] 
# 		for x in y:
# 			file.write(str(x))
# 			file.write('\t')
# 		file.write('\n')
# 	file.close()
# datanpT.tolist()
# print(datanp)

# namaFile = 'penjualandanlaba'
# clearFile(namaFile)
# insertFile(namaFile, datanpT)
