import math
from colorama import init, Fore, Style
init()
print(Fore.RED+"Hesap Makinesi\n—————————————"+Style.RESET_ALL)
print(Fore.BLUE+"1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("5. Üs Alma")
print("6. Karakök")
print("7. Sinüs")
print("8. Kosinüs")
print("9. Tanjant")
print("10. Logaritma")
print("11. Çıkış"+Style.RESET_ALL)

while True:
    choice = int(input("Seçiminiz (1/2/3/4/5/6/7/8/9/10/11): "))

    if choice == 11:
        print("\nHesap Makinesinden çıkış yaptınız")
        break

    num1 = float(input("İlk sayı: "))

    if choice != 6 and choice != 7 and choice != 8 and choice != 9 and choice != 10:
        num2 = float(input("İkinci sayı: "))

    if choice == 1:
        result = num1 + num2
        print("Sonuç:", result)
    elif choice == 2:
        result = num1 - num2
        print("Sonuç:", result)
    elif choice == 3:
        result = num1 * num2
        print("Sonuç:", result)
    elif choice == 4:
        result = num1 / num2
        print("Sonuç:", result)
    elif choice == 5:
        result = num1**num2
        print("Sonuç:", result)
    elif choice == 6:
        result = math.sqrt(num1)
        print("Sonuç:", result)
    elif choice == 7:
        result = math.sin(num1)
        print("Sonuç:", result)
    elif choice == 8:
        result = math.cos(num1)
        print("Sonuç:", result)
    elif choice == 9:
        result = math.tan(num1)
        print("Sonuç:", result)
    elif choice == 10:
        base = float(input("Taban: "))
        result = math.log(num1, base)
        print("Sonuç:", result)
    else:
        print("Geçersiz seçim")
