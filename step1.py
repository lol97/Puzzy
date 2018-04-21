import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
'''
	Soal dari buku : 	Kusumadewi, S.. (2004). Aplikasi Logika Fuzzy Untuk Pendukung Keputusan. Yogyakarta: Graha Ilmu.
						Bab V (kasus1)
	Code by: xsufyan@gmail.com (github.com/lol97)
	Entrepeter : Python 3.6
'''

data = [[2.150, 2.050, 1.650, 2.100, 1.950, 1.900, 2.800, 1.950, 2.250, 2.100, 2.000, 2.350, 1.850, 2.100, 2.500, 2.150, 2.000, 2.400, 1.750, 2.300, 2.400, 2.150, 2.150, 2.450, 2.300, 2.150, 2.200, 2.400, 2.600, 2.400, 2.400, 2.550, 2.700, 2.500, 2.450, 2.600, 2.650, 2.500, 2.400, 2.900, 2.050, 2.100, 2.100, 1.900, 1.800, 2.300, 2.650, 2.700], 
		[2.120, 1.800, 1.920, 1.720, 2.240, 1.880, 2.800, 2.040, 1.720, 2.160, 1.600, 2.240, 1.800, 1.480, 2.160, 1.720, 1.880, 2.240, 1.560, 2.680, 2.000, 1.720, 2.160, 2.320, 2.240, 1.920, 2.360, 2.040, 1.880, 2.160, 2.720, 2.560, 2.480, 2.400, 2.360, 2.240, 2.480, 2.400, 2.320, 2.480, 2.120, 2.120, 2.040, 1.920, 1.720, 2.320, 2.400, 2.720],
		[2.333, 2.000, 1.730, 2.000, 2.400, 2.400, 3.133, 2.400, 1.800, 2.467, 2.333, 2.467, 1.800, 1.867, 2.467, 2.067, 2.200, 2.733, 2.000, 3.000, 2.333, 2.000, 2.200, 2.200, 2.467, 2.400, 2.733, 2.200, 2.467, 2.333, 2.733, 2.533, 2.467, 2.400, 2.533, 2.467, 2.733, 2.533, 2.533, 3.333, 2.533, 2.000, 2.133, 1.867, 1.800, 2.133, 2.800, 3.000],
		[1.000, 0.500, 0.375, 0.750, 1.000, 1.125, 2.000, 0.375, 0.500, 0.750, 1.125, 1.125, 1.125, 1.125, 1.750, 0.750, 0.500, 1.000, 0.750, 1.750, 1.125, 1.125, 1.000, 0.750, 1.375, 1.375, 1.125, 1.375, 1.125, 0.750, 2.750, 2.375, 2.500, 2.375, 2.375, 2.000, 2.500, 2.750, 2.125, 3.125, 1.375, 2.000, 1.500, 1.125, 1.500, 1.125, 2.375, 3.000],
		[2.300, 1.600, 1.800, 1.700, 1.700, 1.900, 3.000, 1.900, 1.500, 2.100, 2.100, 2.300, 2.100, 2.000, 2.200, 2.000, 1.500, 2.400, 1.700, 2.500, 2.300, 2.300, 2.400, 2.300, 2.300, 2.500, 2.400, 2.400, 2.500, 2.000, 2.900, 2.700, 2.700, 2.500, 2.700, 2.700, 2.600, 2.900, 2.700, 3.300, 2.200, 2.200, 1.900, 1.900, 2.200, 2.100, 2.800, 2.900],
		[2.364, 2.091, 1.727, 1.909, 2.182, 2.182, 3.000, 2.273, 1.727, 2.636, 2.909, 2.000, 2.091, 1.818, 2.273, 2.364, 1.818, 2.455, 1.909, 2.636, 2.455, 2.455, 2.636, 2.091, 1.818, 2.000, 2.000, 2.455, 2.909, 1.646, 3.182, 2.909, 2.818, 2.818, 2.545, 2.909, 3.000, 2.818, 3.000, 3.272, 2.545, 2.000, 1.818, 2.455, 1.909, 2.000, 2.909, 3.091]
	   ]

data2 = [[7000000, 10000000, 7500000, 5000000, 17000000, 7000000, 14000000, 18000000, 40000000, 10000000, 11000000, 15000000, 8000000, 5000000, 10000000, 9000000, 7000000, 8000000, 6500000, 20000000, 4000000, 8000000, 8000000, 20000000, 40000000, 5000000, 25000000, 10000000, 10000000, 24000000, 10000000, 10000000, 10000000, 10000000, 8000000, 10000000, 8500000, 16000000, 8000000, 5000000, 15000000, 7500000, 25000000, 7000000, 9000000, 12000000, 8000000, 7500000],
		 [3000000, 4000000, 2000000, 1200000, 5000000, 2000000, 5000000, 5500000, 10000000, 4000000, 5000000, 6500000, 3000000, 1500000, 5500000, 1500000, 1000000, 2500000, 1000000, 7000000, 1500000, 2250000, 2500000, 5000000, 12000000, 1000000, 7000000, 2500000, 3000000, 10000000, 6000000, 5000000, 3500000, 5000000, 2500000, 5500000, 2500000, 6000000, 2000000, 1500000, 5000000, 2000000, 7000000, 3000000, 3000000, 4000000, 2000000, 2000000]
		]

# print('cek Len data')
# print (len(data[0]))
# print (len(data[1]))
# print (len(data[2]))
# print (len(data[3]))
# print (len(data[4]))
# print (len(data[5]))

# print('cek Len data2')
# print (len(data2[0]))
# print (len(data2[1]))
def ubahKeFuzzy(data, skala):
	olah1=[]
	for y in data:
		temp=[]
		for x in y:
			temp.append(x/skala)
		olah1.append(temp)
	return olah1

def ubahkeFuzzyDana(data):
	hasil = []
	myu = []
	laba = []
	i = 0
	while(i<len(data[0])):
		total = data[0][i]
		if(total>=0 and total<40000000):
			y=total/40000000
		elif(total>=40000000):
			y=1
		myu.append(y)
		laba.append(data[1][i])
		i+=1
		
	hasil.append(laba)
	hasil.append(myu)
	return(hasil)

def keanggotaanTinggi(data):
	hasil = []
	for x in data:
		if(x>=0 and x<40000000):
			y=x/40000000
		elif(x>=40000000):
			y=1
		hasil.append(y)


def clearFile(namaFile):
	namaFile = str(namaFile+'.txt')
	file = open(namaFile,'w')
	file.close()


def insertFile(namaFile, data):
	data = list(map(list,zip(*data))) #transpose data
	namaFile = str(namaFile+'.txt')
	file = open(namaFile,'a')
	for y in data:
		temp = [] 
		for x in y:
			file.write(str(x))
			file.write('\t')
		file.write('\n')
	file.close()


def linearRegresion(data):
	'''
		indeks[0] -> response variable -> x
		indeks[1] -> predictor variable -> y
	'''
	x2=[]
	y2=[]
	xy=[]
	n = len(data[0])

	for x in data[0]:
		x2.append(x**2)

	for y in data[0]:
		y2.append(y**2)

	i=0;
	while(i<n):
		dump = data[0][i]*data[1][i]
		xy.append(dump)
		i+=1
	jmlhx = sum(data[0])
	jmlhy = sum(data[1])
	jmlhx2 = sum(x2)
	jmlhy2 = sum(y2)
	jmlhxy = sum(xy)

	a = ((jmlhy*jmlhx2)-(jmlhx*jmlhxy))/(n*jmlhx2-(jmlhx**2))
	b = ((n*jmlhxy)-(jmlhx*jmlhy))/(n*jmlhx2-(jmlhx**2))

	return(a,b)


# hasil = []
# hasil = ubahkeFuzzyDana(data2)
# print(hasil[1])


# b,a = linearRegresion(data2)
# print(a)
# print(b)


# cek Hasil1
# normalisasi = ubahKeFuzzy(data,4)
# print(normalisasi)

# tulisDataRaw ke File
# namaFileRaw='dataRaw1'
# namaFileRaw2='dataRaw2'
# clearFile(namaFileRaw)
# insertFile(namaFileRaw,data)
# clearFile(namaFileRaw2)
# insertFile(namaFileRaw2,data2)

# tulisDataNormalisasi ke File
# normalisasi = ubahKeFuzzy(data,4)
# clearFile('normalisasi1')
# insertFile('normalisasi1',normalisasi)

'''
# menggambarkan grafik linear regresi untuk y = laba dan x = nilai kenaggotaan tinggi dari total
total,_ = data2 #0-> total, 1-> laba
laba,keanggotaan = ubahkeFuzzyDana(data2) #0 -> laba, 1->keanggotaan tinggi dari total

dataProses = []
dataProses.append(keanggotaan)
dataProses.append(laba)
a,b = linearRegresion(dataProses)
print(a)
print(b)


plt.scatter(keanggotaan,laba,label='data aktual')
def f(data,a,b):
	hit = []
	for x in data:
		y = b*x+a
		hit.append(y)
	return(hit)

plt.plot(keanggotaan,f(keanggotaan,a,b),c='k',label='hasil regresi')
plt.legend()
plt.show()
'''

def pembentukanVektorG(keanggotaan):
	vektorHasil=[]
	i=0
	while(i<len(keanggotaan)):
		vektorTemp=[]
		j=0
		while (j<len(keanggotaan)):
			if(i==j):
				vektorTemp.append(keanggotaan[i])
			else:
				vektorTemp.append(0)
			j+=1
		i+=1
		vektorHasil.append(vektorTemp)
	return (vektorHasil)

# def transposeCuy(dataMatrix):
# 	hasil=[]
# 	for x in dataMatrix:
# 		temp=[]
# 		temp.append(x)
# 		hasil.append(temp)
# 	return (hasil)

def cariNilaiA(G,X,Xt,Yt):
	hasil1 = np.matmul(X,G)
	hasil2 = np.matmul(hasil1,Xt)
	hasil3 = inv(hasil2)
	hasil4 = np.matmul(hasil3,X)
	hasil5 = np.matmul(hasil4,G)
	hasil6 = np.matmul(hasil5,Yt)
	return(hasil6)


normalisasi= ubahKeFuzzy(data,4)#tenagakerja, modal, material, teknologi, informasi, manajerial
ntk, nmo, nma, nte, nin, nman = normalisasi
laba,keanggotaan = ubahkeFuzzyDana(data2)
##dibuat ke numpy supaya 2D
G = np.array(pembentukanVektorG(nmo))
X = np.array([keanggotaan])
Xt = X.T
Y = np.array([laba])
Yt = Y.T
##print(G.shape,X.shape,Xt.shape,Y.shape,Yt.shape)
a = cariNilaiA(G,X,Xt,Yt)
a = a[0,0]
##print(a)

def gambarGrafik(dataProses,value,flag):
	a,b = linearRegresion(dataProses)
	keanggotaan,laba = dataProses
	def f1(keanggotaan,a,b):
		hit = []
		for x in keanggotaan:
			y = b*x+a
			hit.append(y)
		return(hit)
	def f2(keanggotaan,a):
		hit = []
		for x in keanggotaan:
			y = x*a
			hit.append(y)
		return(hit)
	plt.scatter(keanggotaan,laba,label='data aktual',s=0.5)
	plt.plot(keanggotaan,f1(keanggotaan,a,b),c='k',label='hasil regresi without',linewidth=0.1)
	if(flag==1):
		plt.plot(keanggotaan,f2(keanggotaan,value),c='r',label='hasil regresi',linewidth=0.1)
	plt.legend()
	plt.show()

def cariTitikPotong(garis1,garis2):
	xdiff = (garis1[0][0]-garis1[1][0],garis2[0][0]-garis2[1][0])
	ydiff = (garis1[0][0]-garis1[1][0],garis2[0][0]-garis2[1][0])

	def det(a,b):
		return (a[0]*b[0] - a[1]*b[0])

	div = det(xdiff,ydiff)
	if div == 0:
		raise exception('Tidak pernah bertemu')

	d = (det(*garis1),det(*garis2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return (x,y)



def FQT1(data,data2,flag):
	Gfuzzy=[]
	SelisihLaba=[]
	normalisasi=ubahKeFuzzy(data,4)
	laba,keanggotaan = ubahkeFuzzyDana(data2)
	#without
	wb,wa = linearRegresion([keanggotaan,data2[1]])
	dataProses = []
	dataProses.append(keanggotaan)
	dataProses.append(laba)
	kec = min(keanggotaan)
	bes = max(keanggotaan)
	X = np.array([keanggotaan])
	Xt = X.T
	Y = np.array([laba])
	Yt = Y.T
	#Store semua data A
	for kol in data:
		G = np.array(pembentukanVektorG(kol))
		a = cariNilaiA(G,X,Xt,Yt)
		a = a[0,0]
		SelisihLaba.append(a-wa)
		Gfuzzy.append(a)
	#cek
	print (Gfuzzy)
	print (SelisihLaba)
	if(flag==666):
		gambarGrafik(dataProses,0,0)
	elif(flag==1):
		gambarGrafik(dataProses,Gfuzzy[flag-1],1)
	elif(flag==2):
		gambarGrafik(dataProses,Gfuzzy[flag-1],1)
	elif(flag==3):
		gambarGrafik(dataProses,Gfuzzy[flag-1],1)
	elif(flag==4):
		gambarGrafik(dataProses,Gfuzzy[flag-1],1)
	elif(flag==5):
		gambarGrafik(dataProses,Gfuzzy[flag-1],1)
	elif(flag==6):
		gambarGrafik(dataProses,Gfuzzy[flag-1],1)


FQT1(data,data2,2)




