import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.linalg import matrix_power as mp
from scipy.linalg import cholesky as chol
from scipy.linalg import sqrtm as sm
from numpy.linalg import eig as eg
from numpy.linalg import eigvals as egval
from scipy.sparse.linalg import eigs as hahaha
import cv2

'''
	Soal dari buku : 	Kusumadewi, S.. (2004). Aplikasi Logika Fuzzy Untuk Pendukung Keputusan. Yogyakarta: Graha Ilmu.
						Bab V (kasus 5.2)
	Code by: xsufyan@gmail.com (github.com/lol97)
	Entrepeter : Python 3.6
'''

external_standard = [[0.2, 0.3, 0.4, 0.7, 0.6, 0.4, 0.2, 0.7, 0.1, 0.4, 0.3, 0.4, 0.1, 0.5, 0.7],
					[0.8, 0.5, 0.6, 0.3, 0.6, 0.8, 0.8, 0.3, 0.9, 0.5, 0.6, 0.3, 0.8, 0.5, 0.2]
					]

harga = [[0.3, 0.4, 0.8, 0.6, 0.4, 0.9, 1.0, 0.6, 0.2, 0.0, 0.3, 0.1, 0.2, 0.7, 0.8],
		[0.8, 0.5, 0.3, 0.5, 0.7, 0.1, 0.2, 0.4, 1.0, 0.9, 0.7, 0.8, 0.8, 0.2, 0.0]
		]

selera_rasa = [[0.3, 1.0, 0.0, 0.6, 0.7, 0.2, 0.9, 0.4, 0.2, 0.6, 0.1, 0.2, 0.3, 0.7, 0.5],
			   [0.8, 0.1, 0.9, 0.4, 0.3, 0.7, 0.0, 0.7, 1.0, 0.5, 0.9, 0.9, 0.7, 0.4, 0.6]
			  ]

komposisi = [[1.0, 0.2, 0.0, 0.1, 0.4, 0.0, 0.3, 0.8, 0.9, 0.2, 0.1, 0.2, 0.5, 0.2, 0.1],
			 [0.1, 0.2, 0.3, 0.0, 0.5, 0.0, 0.4, 1.0, 0.1, 0.8, 0.9, 0.5, 0.5, 0.8, 0.9],
			 [0.0, 0.9, 0.8, 0.0, 0.1, 1.0, 0.1, 0.0, 0.0, 0.1, 0.1, 0.5, 0.1, 0.2, 0.0]
			 ]

ukuran = [[0.2, 0.3, 0.5, 0.6, 0.8, 0.9, 1.0, 0.0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.4, 0.2],
		  [0.9, 0.6, 0.5, 0.4, 0.3, 0.1, 0.0, 0.9, 1.0, 0.7, 0.6, 0.5, 0.4, 0.7, 0.8]
		 ]

kemasan = [[0.2, 1.0, 0.6, 0.3, 0.5, 0.0, 0.7, 0.5, 0.6, 1.0, 0.3, 0.8, 0.9, 0.4, 0.1],
		   [0.8, 0.0, 0.5, 0.7, 0.6, 0.8, 0.2, 0.5, 0.6, 0.1, 0.7, 0.3, 0.0, 0.7, 0.0]
		  ]

kmdhn_mdptkn = [[0.1, 0.3, 0.5, 0.8, 0.7, 0.9, 0.1, 1.0, 0.3, 0.0, 0.0, 0.5, 1.0, 0.4, 0.6],
				[1.0, 0.8, 0.6, 0.2, 0.4, 0.0, 1.0, 0.0, 0.8, 0.8, 0.9, 0.3, 0.1, 0.6, 0.3]
			   ]

#cekData
	# print(len(external_standard[0]),len(external_standard[1]))
	# print(len(harga[0]),len(harga[1]))
	# print(len(selera_rasa[0]),len(selera_rasa[1]))
	# print(len(komposisi[0]),len(komposisi[1]))
	# print(len(ukuran[0]),len(ukuran[1]))
	# print(len(kemasan[0]),len(kemasan[1]))
	# print(len(kmdhn_mdptkn[0]),len(kmdhn_mdptkn[1]))

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

def insert1ArrayFile(namaFile,data):
	namaFile = str(namaFile+'.txt')
	file = open(namaFile,'a')
	for y in data:
		file.write(str(y))
		file.write('\n')
	file.close()

def buatMatriksRespon(harga,selera_rasa,komposisi, ukuran, kemasan, kmdhn_mdptkn):
	hasil = []
	list_data = [harga, selera_rasa, komposisi, ukuran, kemasan, kmdhn_mdptkn]

	i = 0
	while(i<len(harga[0])):
		temp = []
		for x in list_data:
			j = 0
			while(j<len(x)):
				temp.append(x[j][i])
				j+=1
		hasil.append(temp)
		i+=1
	return hasil


#cek buatMatriksRespon
data = buatMatriksRespon(harga, selera_rasa, komposisi, ukuran, kemasan, kmdhn_mdptkn)
	# print(cek1[14])
# datan = np.array(data)
# datat = datan.T
# namaFile = 'Data'
# clearFile(namaFile)
# insertFile(namaFile,datat)

edn = np.array(external_standard)
edt = edn.T
namaFile = 'DataExternalStandard'
clearFile(namaFile)
insertFile(namaFile,edn)

def buatMatriksA(data):
	temp = data+data
	tempn = np.array(temp) #cekifneeded
	return temp

#cek buatMatriksA
	# cekMatriks = buatMatriksA(buatMatriksRespon(harga, selera_rasa, komposisi, ukuran, kemasan, kmdhn_mdptkn))
	# print(cekMatriks[15])

def buatMatriksAG(data,external_standard):
	hasil1=[]
	hasil2=[]
	#standar1
	i=0
	while(i<len(data[0])):
		j=0
		sumtemp = 0
		while(j<len(data)):
			sumtemp = sumtemp+data[j][i]*external_standard[0][j]
			j+=1
		hasil1.append(round(sumtemp/sum(external_standard[0]),2))
		i+=1
	# hasil1 = [hasil1]*len(data)
	#standar2
	i=0
	while(i<len(data[0])):
		j=0
		sumtemp = 0
		while(j<len(data)):
			sumtemp = sumtemp+data[j][i]*external_standard[1][j]
			j+=1
		hasil2.append(round(sumtemp/sum(external_standard[1]),2))
		i+=1
	# hasil2 = [hasil2]*len(data)
	hasil = []
	for x in data:
		hasil.append(hasil1)
	for z in data:
		hasil.append(hasil2)
	return(hasil)
Ag = buatMatriksAG(data,external_standard)
Ag = np.array(Ag)
# print(Ag.shape)
Ag = Ag.T
clearFile('matriksAG')
insertFile('matriksAG',Ag)
#cek buatMatriksAG
	# cekMatriks = buatMatriksRespon(harga, selera_rasa, komposisi, ukuran, kemasan, kmdhn_mdptkn)
	# cek = buatMatriksAG(cekMatriks,external_standard)
	# print(cek[16])

def buatMatriksMeanA(data, external_standard):
	hasil1=[]
	hasil=[]
	i=0
	N = sum(external_standard[0])+sum(external_standard[1])
	while(i<len(data[0])):
		j=0
		sumtemp = 0
		while(j<len(data)):
			sumtemp = sumtemp+data[j][i]
			j+=1
		hasil1.append(sumtemp/N)
		i+=1
	i=0
	while (i<len(data)*2):
		hasil.append(hasil1)
		i+=1
	return(hasil)
meanA = buatMatriksMeanA(data,external_standard)
meanA = np.array(meanA)
meanA = meanA.T
clearFile('matriksMeanA')
insertFile('matriksMeanA',meanA)
#cek buatMatriksMeanA
	# cekMatriks = buatMatriksRespon(harga, selera_rasa, komposisi, ukuran, kemasan, kmdhn_mdptkn)
	# cek = buatMatriksMeanA(cekMatriks,external_standard)
	# print(cek[1])

'''
def buatMatriksakecil(external_standard):
	a = external_standard[0]+external_standard[1]
	a = np.array([a])
	return(a)
'''
#cekdataMatriksakecil
	# a = buatMatriksakecil(external_standard)
	# print(a,a.shape)

def buatMatriksG(external_standard):
	vektorCari = external_standard[0]+external_standard[1]
	vektorHasil=[]
	i=0
	while(i<len(vektorCari)):
		vektorTemp=[]
		j=0
		while (j<len(vektorCari)):
			if(i==j):
				vektorTemp.append(vektorCari[i])
			else:
				vektorTemp.append(0)
			j+=1
		i+=1
		vektorHasil.append(vektorTemp)
	return (vektorHasil)
G = buatMatriksG(external_standard)
G = np.array(G)
G = G.T
clearFile('matriksG')
insertFile('matriksG',G)

#cek buatMatriksG
	# cek = buatMatriksG(external_standard)
	# print(cek[28][28])

def cariMatriksSG(data,external_standard):
	G = np.array(buatMatriksG(external_standard))
	Amean = np.array(buatMatriksMeanA(data,external_standard))
	Ag = np.array(buatMatriksAG(data,external_standard))
	hasil1 = sm(G)
	hasil2 = np.subtract(Ag,Amean)
	hasil3 = np.matmul(hasil1,hasil2)
	hasil4 = hasil3.T
	hasil5 = np.matmul(hasil4,hasil1)
	hasil6 = np.matmul(hasil5,hasil2)
	#print(hasil6.shape)
	return(hasil6)
SG = cariMatriksSG(data,external_standard)
SG = np.array(SG)
SG = SG.T
clearFile('matriksSG')
insertFile('matriksSG',SG)
#cek cariMatriksSG
cek = cariMatriksSG(data,external_standard)
#print(cek[:,11])

def cariMatriksS(data,external_standard):
	A = np.array(buatMatriksA(data))
	G = np.array(buatMatriksG(external_standard))
	Amean = np.array(buatMatriksMeanA(data,external_standard))
	Ag = np.array(buatMatriksAG(data,external_standard))
	hasil1 = sm(G)
	hasil2 = np.subtract(A,Amean)
	hasil3 = np.matmul(hasil1,hasil2)
	hasil4 = hasil3.T
	hasil5 = np.matmul(hasil1,hasil2)
	hasil6 = np.matmul(hasil4,hasil5)
	#print(hasil6.shape)
	return (hasil6)
S = cariMatriksS(data,external_standard)
S = np.array(S)
S = S.T
S = S.real
clearFile('matriksS')
insertFile('matriksS',S)
#cek cariMatriksS
	# cek = cariMatriksS(data,external_standard)
	# print(cek)

def decompositionCholesky(data,external_standard):
	hasil = cariMatriksS(data, external_standard)
	final = chol(hasil)
	#print(final.shape)
	return(final)

#cek decomposition
#cek = cariMatriksS(data,external_standard)
seg = decompositionCholesky(data,external_standard)
dataChol = decompositionCholesky(data,external_standard)
dataChol = np.array(dataChol)
dataChol = dataChol.T
dataChol = dataChol.real
clearFile('matriksChol')
insertFile('matriksChol',dataChol)
#print(cek)
#print("-------------")
#print(np.dot(dataChol,dataChol.T))
#print(dataChol)

def cariMatriksGamma(data,external_standard):
	seg = np.array(decompositionCholesky(data,external_standard))
	Sg = np.array(cariMatriksSG(data,external_standard))
	hasil1 = seg.T
	#print(np.amin(hasil1))
	hasil2 = inv(hasil1)
	#print(np.amin(hasil2))
	hasil3 = np.matmul(hasil2,Sg)
	#print(np.amin(hasil3))
	hasil4 = inv(seg)
	#print(np.amin(hasil4))
	hasil5 = np.matmul(hasil3,hasil4)
	#print(np.amax(hasil5))
	return(hasil5)

#cek cariMatriksGamma
gamma = cariMatriksGamma(data,external_standard)
gammaW = np.array(gamma)
gammaW = gammaW.T
gammaW = gammaW.real
clearFile('matriksGamma')
insertFile('matriksGamma',gammaW)
evalue,evector = eg(gamma)
evalue = evalue.real
#print(evalue)
clearFile('EigenValue')
insert1ArrayFile('EigenValue',evalue)
maxKey = max(evalue)
nevector = np.array(evector)
evector = evector.real
clearFile('evectorMat')
insertFile('evectorMat',evector.T)
bobot = evector[:,1].real
#print(bobot)

def cariBobotFinal(bobot,seg):
	hasil = inv(seg)
	return np.matmul(hasil,bobot)
final = cariBobotFinal(bobot,seg)

def findKolomYJ(final, data):
	i=0
	hasil = []
	while(i<len(data)):
		j = 0
		temp = 0
		while (j<len(bobot)):
			temp = temp + (data[i][j]*bobot[j].real)
			j+=1
		hasil.append(temp.real)
		i+=1

	return(hasil)
#print(findKolomYJ(bobot,data))
#cek YJ
rangkuman1 = findKolomYJ(bobot, data)
	# print(rangkuman1)

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

#cek hasillinearregression
send = []
send.append(external_standard[0])
send.append(rangkuman1)
reg1 = linearRegresion(send)
reg2 = linearRegresion([external_standard[1],rangkuman1])

# print(reg1)
# print(reg2)

def gambarGafik(reg1, reg2, yj,external_standard):
	def f1(yj,reg):
		hit = []
		for x in yj:
			y = reg[0]*x+reg[1]
			hit.append(y)
		return(hit)
	plt.scatter(yj,external_standard[0],label='Merk A',s=10,marker='^')
	plt.scatter(yj,external_standard[1],label='Merk B',s=10,marker='o')
	plt.plot(yj,f1(yj,reg1),c='k',label='regressi 1',linewidth=0.1)
	plt.plot(yj,f1(yj,reg2),c='r',label='regressi 2',linewidth=0.1)
	plt.legend()
	plt.show()

gambarGafik(reg1,reg2,rangkuman1,external_standard)
