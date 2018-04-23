import numpy as np

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

print(data)
b = np.array(data)
print(b.shape)