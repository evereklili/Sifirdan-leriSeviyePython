#name="OMER DOGU KAYSERI"
#for letter in name:
#	if letter=='a' or letter=='A':
#		break
#	print(letter)

 
#O
#M
#E
#R

#D
#O
#G
#U

#K
#Press any key to continue . . .

 
#name="OMER DOGU KAYSERI"
#for letter in name:
#	if letter=='a' or letter=='A':
#		continue
#	print(letter)

#O
#M
#E
#R

#D
#O
#G
#U

#K
#Y
#S
#E
#R
#I
#Press any key to continue . . .

#x=0
#while(x<5):
#	if(x==2):
#		continue
#	print(x)
#	x+=1 

#1 den 100 kadar tek sayıların toplamı nedir?
#x=1
#result=0
#while x<=100:
#	x+=1
#	if x%2==0:
#		continue  #eğer x sayının 2 ile kalanı 1 ise
#	result+=x
	

#print(f'toplam: {result}')
##sadece çift sayıların toplamı bulunur. if x%2==1 dersek

#toplam: 2600
#Press any key to continue . . .

#döngü methodları kullanalım. 
#list=[1,2,3,4,5]
#for item in list:
#	print(item)
#döngü methodları kullanalım. 
#list=[1,2,3,4,5]
#for item in range(100):
#	print(item) #listeyi yazdırır. 
 
#for item in range(50,100,20):#50,70,90
##	print(item) #listeyi yazdırır.
#list=[1,2]
#for xx in range(10,1000,12):
#	list=[xx]

##print(list(range(10,1000,10)))
#result=0
#for x in list:
#	result+=x

#print(f'Toplamı:{result}')
##yazdırabilriz. 


#enumarate
#string bilgi olsu. for döngüsü ile letter in greatin diyelim .
#her bir bilgiyi ekrana yazdıralım. tek tek teklimeler ekran yazdırılır. 
#her gelen kelimienin index ulaşmak istersek while dögüsünde yapıyorduk, index 0 başlatırı z he seferinde a yaparz 

#index=0
#greeting='Hello Three Dear Friends'
#for letter in greeting:
#	print(f'index :{index}  -- letter: {letter}')
#	index+=1
#index :0  -- letter: H
#index :1  -- letter: e
#index :2  -- letter: l
#index :3  -- letter: l
#index :4  -- letter: o
#index :5  -- letter:
#index :6  -- letter: T
#index :7  -- letter: h
#index :8  -- letter: r
#index :9  -- letter: e
#index :10  -- letter: e
#index :11  -- letter:
#index :12  -- letter: D
#index :13  -- letter: e
#index :14  -- letter: a
#index :15  -- letter: r
#index :16  -- letter:
#index :17  -- letter: F
#index :18  -- letter: r
#index :19  -- letter: i
#index :20  -- letter: e
#index :21  -- letter: n
#index :22  -- letter: d
#index :23  -- letter: s
#Press any key to continue . . .

##zip methodu iki liste tnaımlayaılım
#list1=[1,2,3,4,5,6]
#list2=['a','b','c','d','e','ğ']
#list3=[100,200,300,400,500,600,700]
##böyle isimler ve kişiler listesi olsun. 
##bir eşleştirme yapmak için zip kullanır
 
#print(list(zip(list1,list2,list3))) #dikkat 700 numaralandırmadı devre dışı bıraktı.diğerlerini birebir function kullandı. 


#for x in range(10):
#	print(x) #bunun daha kolayı ise
#numbers=[x for x in range(10)]
#print(numbers) #alternatifidir. 


#for x in range(10):
#	print(x**2) #bunun daha kolayı ise
#numbers=[x**2 for x in range(10)]
#print(numbers) #alternatifidir. 


 
#numbers=[x**2 for x in range(10) if x%3==0]
#print(numbers) #alternatifidir. 
#myList=[]
#for listem in myList:
#	myList.append(letter)

#print(myList)


#years=[1995,1993,2000,1987,1993,1986]
#ages=[2021-year for year in years]
#print(ages)
#[26, 28, 21, 34, 28, 35]
#Press any key to continue . . .

#resuls=[x if x%2==0 'Çift'  else 'Tek' for x in range(10,1000,2)]


#import random
#sayi=random.randint(1,100)
#print(sayi)
#sayac=0
#hak=10
#while hak>0:
#	tahmin=int(input('Tahmininiz:'))
#	if(sayi==tahmin):
#		print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız:{100-20*(sayac-2)}')
#		break
#	elif(sayi>tahmin):
#		print("Yukarı çıkınız...")
#		sayac=sayac+1
#	else:
#		print("Aşağı ininiz...")
#		sayac=sayac+1
#	if(hak==0):
#		print(f'Hakkınız bitti malesef... Tuttuğunuz sayi:{sayi}')


#asal sayı olup olmadığını kontrol edelim
'''
asal sayı: 1 ve kendinden başka böleni olmayan sayılara asal sayı denir. 
1 sayısını asal olmadığın belirtmeliyiz. 
kullanıcıan sayı al. 

'''

	
'''

bir method bir sınıfta değerlendirilir. 
bir fonksiyon oluşturualrım def ile tanımlanır. 
'''

#def sayHello():#yazdığımız kodlar sayHello üyesi olmasıdır. 
#	print("Hello")

#sayHello()
 
#def total(x,y):
#	return x+y
#def subraction(x,y):
#	return x-y

#results=total(29,359) 
#print(results)
#result=subraction(29,359)
#print(result)

#def yasHesapla(yil,dYil):
#	return yil-dYil

#print(yasHesapla(2022,1987))

#def emekliligeKacYilKaldi(dogumYili,isim):
#	yas=yasHesapla(2021,dogumYili)
#	emeklilik=65-yas
#	if(emeklilik>0):
#		print(f'emekliliğinize {emeklilik} yıl kaldı')

#emekliligeKacYilKaldi(1987,"ömer");

