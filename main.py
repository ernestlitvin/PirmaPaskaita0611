import math
import random
import re
import statistics
from statistics import median

print("hi")
print("hello")
print("sveiki")
print('sveiki')

skaicius = 24
tekstas = "Viktoras"
yra_skanu = True

print(skaicius)
print(tekstas)
print(yra_skanu)

print("Vartotojas yra " + tekstas + ", jam yra " + str(skaicius) + " metai")

# 11:02 - 11:13 - watch record

r = 165312

print("Apskritimo, kurio spindulys yra " + str(r) + " plotas yra " + str(r * math.pi))

print(f"Apskritimo, kurio spindulys yra {r} plotas yra {r * math.pi}")


if 5 < 3:
    print("taip, 5 yra daugiau uz 3")
else:
    print("teiginys buvo klaidingas")

print("kodas einantis zemiau salyginio sakinio")

rnd_num = random.randint(1, 10)
print("Mokinys gavo is egzamino " + str(rnd_num))





mark = random.randint(1, 10)
print("Studentas gavo " + str(mark) + " is egzamino.")
if mark <= 3:
    print("Prastai pasirode, neislaike egzamino")

print()
print()
print()
print("-------------------------- uzd 1 --------------------------")
# Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus).
# Parašykite kodą, kuris pagal gimimo metus paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų
# tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".
name = "Ernest"
surname = "Litvin"
birthday = 1993
now = 2025

print("Aš esu " + name + " " + surname + "." + " Man yra " + str(now-birthday) + " metai(ų)" + ".")

print("-------------------------- uzd 2 --------------------------")
# Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.

x = random.randint(0, 4)
y = random.randint(0, 4)
print("Skaicius X - " + str(x))
print("Skaicius Y - " + str(y))

if x == 0 or y == 0:
    print("dalyba is nulio (x arba y)")
elif x == y:
    print("Lygus skaiciai")
elif x > y:
    print("IF x>y -> " + str(round(x / y,2)))
elif x < y:
    print("IF x<y -> " + str(round(y / x,2)))

print()
print("-------------------------- uzd 3 --------------------------")
# Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 25.
# Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

x = random.randint(0, 25)
y = random.randint(0, 25)
z = random.randint(0, 25)

print("Skaicius X - " + str(x))
print("Skaicius Y - " + str(y))
print("Skaicius Z - " + str(z))

if x < y < z:
    print("Vidurinis - " + str(y))
elif x < z < y:
    print("Vidurinis - " + str(z))
elif y < z < x:
    print("Vidurinis - " + str(z))
elif y < x < z:
    print("Vidurinis - " + str(x))
elif z < x < y:
    print ("Vidurinis - " + str(x))
elif z < y < x:
    print ("Vidurinis - " + str(y))



# duomenys = 332,3434,34534
# print(median(duomenys))

print()
print("-------------------------- uzd 4 --------------------------")
# Įvedami skaičiai - a, b, c – kraštinių ilgiai, trys kintamieji (naudokite random.randint(x,x) funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.


a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)

print("Ilgis a - " + str(a))
print("Ilgis b - " + str(b))
print("Ilgis c - " + str(c))


if a == 0 or b == 0 or c == 0:
    print("Trikampis neimanomas")
elif a + b > c:
    print("Trikampis imanomas" , str(a + b) , str(c))
elif a + c > b:
    print("Trikampis imanomas", str(a + c) , str(b))
elif b + a > c:
    print("Trikampis imanomas", str(b + a) , str(c))
elif b + c > a:
    print("Trikampis imanomas", str(b + c) , str(a))
elif c + a > b:
    print("Trikampis imanomas", str(c + a) , str(b))
elif c + b > a:
    print("Trikampis imanomas", str(c + b) , str(a))


print()
print("-------------------------- uzd 5 --------------------------")
# Sukurkite keturis kintamuosius ir random.randint(x,x) funkcija sugeneruokite jiems reikšmes nuo 0 iki 2.
# Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).

x = random.randint(0, 2)
y = random.randint(0, 2)
z = random.randint(0, 2)
w = random.randint(0, 2)

print("Skaicius X - " + str(x))
print("Skaicius Y - " + str(y))
print("Skaicius Z - " + str(z))
print("Skaicius W - " + str(w))

zeros = 0
ones = 0
twos = 0

if x == 0:
    zeros += 1
elif x == 1:
    ones += 1
else:
    twos += 1

if y == 0:
    zeros += 1
elif y == 1:
    ones += 1
else:
    twos += 1

if z == 0:
    zeros += 1
elif z == 1:
    ones += 1
else:
    twos += 1

if w == 0:
    zeros += 1
elif w == 1:
    ones += 1
else:
    twos += 1

print("Zero: " + str(zeros) + ", One: " + str(ones) + ", Two: " + str(twos))

print("--or--") ### ALTERNATIVE WAY ###

print(f"Zero: {zeros}, One: {ones}, Two: {twos}")


print()
print("-------------------------- uzd 6 --------------------------")
# Naudokite funkcija random.randint(x,x). Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10.
# Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose [], 0 -  (), didesni už 0 {}.
# CHECK ONE MORE TIME ?!?!?!??!?!?!?!?!?!?!?!?!

num1 = random.randint(-10, 10)
num2 = random.randint(-10, 10)
num3 = random.randint(-10, 10)

print(f"Skaicius X - {num1}")
print(f"Skaicius Y - {num2}")
print(f"Skaicius Z - {num3}")

def format_number(num):
    if num < 0:
        return f"[{num}]"
    elif num == 0:
        return f"({num})"
    else:
        return f"{{{num}}}"

formatted_num1 = format_number(num1)
formatted_num2 = format_number(num2)
formatted_num3 = format_number(num3)

print("Generated numbers")
print(formatted_num1, formatted_num2, formatted_num3)

print()
print("-------------------------- uzd 7 --------------------------")

# Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų- 4 % nuolaida.
# Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama.
# Žvakių kiekį generuokite random.randint(x,x) funkcija nuo 5 iki 3000.


zvakes = random.randint(5,3000)
print(zvakes)

if zvakes <= 1000:
    print("Zvakiu kaina " + str(zvakes) + " EUR" + " ." + " Zvakiu kiekis " + str(zvakes))
elif zvakes > 1000 and zvakes < 2000:
    print("Zvakiu kaina " + str(zvakes * 0.97) + " EUR" + "." + " Zvakiu kiekis " + str(zvakes))
elif zvakes > 2000:
    print("Zvakiu kaina " + str(zvakes * 0.96) + " EUR" + " ." + " Zvakiu kiekis " + str(zvakes))

print()
print("-------------------------- uzd 8 --------------------------")

# Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100.
# Paskaičiuokite jų aritmetinį vidurkį. Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10 arba didesnės nei 90.
# Abu vidurkius atspausdinkite. Rezultatus apvalinkite iki sveiko skaičiaus.

x = random.randint(0, 100)
y = random.randint(0, 100)
z = random.randint(0, 100)

print(str(x) + " " + str(y) + " " + str(z))

avg = (x + y + z) / 3 ## " // " ##
print(avg)

# if avg < 10:
#     print("Vidurkis < 10 " + str(avg))
# elif avg > 90:
#     print("Vidurkis > 90 " + str(avg))
# else:
#     print("Vidurkis norm " + str(avg))






print()
print("next stop")
print()


##asd##

