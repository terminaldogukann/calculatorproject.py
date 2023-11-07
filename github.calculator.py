print("Hi, this is a small 4 x 4 calculator.")
print("Just like a  Wilhelm Schickard.")


operatör = str(input("Yapacak operatörü giriniz : Toplama  1 : Çıkartma 2 : Çarpma 3 : Bölme 4 : "))
ilkSayi = int(input("Merhaba, İlk sayıyı giriniz : "))
ikinciSayi = int(input("Merhaba, İkinci sayıyı giriniz : "))

if(operatör == "1"):
    print("{} + {} = {}".format(ilkSayi,ikinciSayi, ilkSayi + ikinciSayi))

elif(operatör =="2"):
    print("{} - {} = {}".format(ilkSayi,ikinciSayi,ilkSayi - ikinciSayi))

elif(operatör == "3"):
    print("{} x {} = {}".format(ilkSayi,ikinciSayi, ilkSayi * ikinciSayi))

elif(operatör == "4"):
    print("{} / {} = {}".format(ilkSayi,ikinciSayi, ilkSayi / ikinciSayi))
else:
    print("Geçerli bir işlem giriniz...")
