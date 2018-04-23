import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.linalg import matrix_power as mp
from numpy.linalg import cholesky as chol
from scipy.linalg import sqrtm as sm
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
		hasil1.append(sumtemp/sum(external_standard[0]))
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
		hasil2.append(sumtemp/sum(external_standard[1]))
		i+=1
	# hasil2 = [hasil2]*len(data)
	hasil = []
	for x in data:
		hasil.append(hasil1)
	for z in data:
		hasil.append(hasil2)
	return(hasil)

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

#cek cariMatriksSG
	# cek = cariMatriksSG(data,external_standard)
	# print(cek)

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

#cek cariMatriksS
	# cek = cariMatriksS(data,external_standard)
	# print(cek)

def decompositionCholesky(data,external_standard):
	hasil = cariMatriksS(data, external_standard)
	final = chol(hasil)
	#print(final.shape)
	return(final)

#cek decomposition
#dataChol = decompositionCholesky(data,external_standard)
#print(dataChol)

def cariMatriksgamma(data,external_standard):
	

