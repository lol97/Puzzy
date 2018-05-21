# metode mamdani

def fkipk(ipk):
	buruk=0
	cukup=0
	bagus=0
	if ipk<2.00:
		buruk=1
	elif ipk<2.75 and ipk>=2.00:
		buruk=(2.75-ipk)/(2.75-2.00)

	if ipk<=2.00:
		cukup=0;
	elif ipk>2.00 and ipk<=2.75:
		cukup= (ipk-2.00)/(3.25-2.75)
	elif ipk>2.75 and ipk<=3.25:
		cukup= (3.25-ipk)/(3.25-2.75)

	if ipk<3.25 and ipk>=2.75:
		bagus=(ipk-2.75)/(3.25-2.75)
	elif ipk>=3.25:
		bagus=1

	hasil=[buruk,cukup,bagus]
	return hasil
def fkpenghasilan(uang):
	kecil=0
	sedang=0
	besar=0
	sangatbesar=0
	
	if uang<1:
		kecil=1
	elif uang>=1 and uang <3:
		kecil=(3-uang)/(3-1)

	if uang<1 :
		sedang = 0
	elif uang>=1 and uang<3:
		sedang=(uang-1)/(3-1)
	elif uang>=3 and uang<4:
		sedang=1
	elif uang>=4 and uang<6:
		sedang=(6-uang)/(6-4)

	if uang<4:
		besar=0
	elif uang>=4 and uang<6:
		besar=(6-uang)/(6-4)
	elif uang>=6 and uang<7:
		besar=1
	elif uang>=7 and uang<12:
		besar=(uang-7)/(12-7)

	if uang>7 and uang<=12:
		sangatbesar=(12-uang)/(12-7)
	elif uang>12:
		sangatbesar=1
	hasil = [kecil,sedang,besar,sangatbesar]
	return hasil
# def nrendah(input):
# 	rendah=0
# 	if input<50:
# 		rendah=1
# 	elif input>=50 and input<100:
# 		rendah=(input-50)/(100-50)
# 	return rendah

def ntinggi(input):
	tinggi=0
	if input<50:
		rendah=1
	elif input>=50 and input<100:
		rendah=(input-50)/(100-50)

	return tinggi

def cekMin(input1,input2):
	if(input1<=input2):
		return input1
	else:
		return input2

def cekMinR(input1,input2):
	if input1<=input2:
		return input1
	else:
		return input2
def cekMaxR(input1,input2):
	if input1<=input2:
		return input2
	else:
		return input1

def fknk(ipk,gaji):
	hasil1=0
	temp1=0
	temp2=0
	hasil2=0
	nk=0;
	if(ipk[0]!=0.0000):
		if(gaji[0]!=0.0000):
			nk=cekMin(ipk[0],gaji[0])
			hasil1=nk;
		elif(gaji[1]!=0):
			nk=cekMin(ipk[0],gaji[1])
			temp1=nk
			hasil1=cekMaxR(temp1,hasil1)
		elif(gaji[2]!=0):
			nk=cekMin(ipk[0],gaji[2])
			temp1=nk
			hasil1=cekMaxR(temp1,hasil1)
		elif(gaji[3]!=0):
			nk=cekMin(ipk[0],gaji[3])
			temp1=nk
			hasil1=cekMaxR(temp1,hasil1)
	if(ipk[1]!=0):
		#print(ipk[1])
		if(gaji[0]!=0.0000):
			nk=cekMin(ipk[1],gaji[0])
			hasil2=nk
		elif(gaji[1]!=0):
			nk=cekMin(ipk[1],gaji[1])
			temp1=nk
			hasil1=cekMaxR(temp1,hasil1)
		elif(gaji[2]!=0):
			nk=cekMin(ipk[1],gaji[2])
			temp1=nk
			hasil1=cekMaxR(temp1,hasil1)
		elif(gaji[3]!=0):
			nk=cekMin(ipk[1],gaji[3])
			temp1=nk
			hasil1=cekMaxR(temp1,hasil1)
	if(ipk[2]!=0):
		if(gaji[0]!=0.0000):
			nk=cekMin(ipk[2],gaji[0])
			temp2=nk
			hasil2=cekMaxR(temp2,hasil2)
		elif(gaji[1]!=0):
			nk=cekMin(ipk[2],gaji[1])
			temp2=nk
			hasil2=cekMaxR(temp2,hasil2)
		elif(gaji[2]!=0):
			nk=cekMin(ipk[2],gaji[2])
			temp2=nk
			hasil2=cekMaxR(temp2,hasil2)
		elif(gaji[3]!=0):
			nk=cekMin(ipk[2],gaji[3])
			temp1=nk
			hasil1=cekMaxR(temp1,hasil1)
	hasilt=[hasil1,hasil2]
	return hasilt

#mamdani
def kelayakan(input1,input2):
	batas1=80-(input1*(80-50))
	batas2=(80+50)/2
	selisih=batas2-batas1
	total=0
	ysempil=0
	dec=0
	i=0
	j=0
	k=0
	akhir=0
	while dec<batas1:
		dec=dec+10
		total=total+dec*input1
		i = i+1
	if(selisih>=10):
		while selisih<=10:
			dec=dec+10
			j = j+1
			selisih=selisih-10
			ysempil=(batas2-(dec))/(batas2-batas1)
			total=total+dec*ysempil
			
	while dec<=100:
		dec=dec+10
		k=k+1
		total=total+dec*input2
	#print(selisih)

	akhir = total/(input1*i+ysempil*j+input2*k)
	return akhir
#sugeno
def kelayakanS(input1,input2):
	return (input1*50+input2*80)/(input1+input2)
		
# print ("hasil %.3f, %.3f, %.4f"%(fkipk(2.85)[0],fkipk(2.85)[1],fkipk(2.85)[2]))
# h1=fkipk(2.85)
# h2=fkpenghasilan(3)
# h3=fknk(h1,h2)
# print (h2)
# print (h3)
def main():
	ipk=2.85
	penghasilan=3
	h1=fkipk(ipk)
	h2=fkpenghasilan(penghasilan)
	h3=fknk(h1,h2)
	print ("Seberapa layak calon tersebut = %.4f %% berdasarkan mamdani"%kelayakan(h3[0],h3[1]))
	print ("Seberapa layak calon tersebut = %.4f %% berdasarkan sugeno"%kelayakanS(h3[0],h3[1]))

main()


