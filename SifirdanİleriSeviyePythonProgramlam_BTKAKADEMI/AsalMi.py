class my_class(object):
        while(True):
	asal=True
	sayi=0
	ayi=int(input('sayi'))


	if sayi==1:
		print('1 sayısı asal sayı değildir')
	for i in range(2, sayi):
		if sayi%i==0:
			asal=False
			break


	if asal:
		print("Sayı asaldır.")
	else:
		print("Sayı asal değildir.")


gfdsa




