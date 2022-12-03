#1.Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.

for i in range(20,50+1):
    if i%3==0 and i%5>0:
        print(i)


#2.Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.

for i in range(1,10):
    a,b=map(int,input().split())
    if i>9  : 
        break
    else:
        if a>b:
            print(a)
        elif a<b:
            print(b)

        else:
            print(a)

#3. Вводят 8 чисел. Найти их произведение (только положительных).

j=1
i=0
while i<8:
    i+=1
    A=float(input(f"sisesta A:"))
    if A>0:
        if int(A)==A: j*=A
print(j)

#4.Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.

A= int(input("Sisesta A:"))
if A>=0:
    print(sum(range(1, A+1)))
else: 
    print("See ei ole naturaalarv")


#5.Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм =
#2,5 см) для значений длин от 1 до 20 дюймов.

for i in range (1,21,1):
    print(i*2.5)

#6.Составьте программу, которая вычисляет сумму только отрицательных из N чисел. 
#Значение N вводится с клавиатуры.
j=0
i=0
while i<5:
    i+=1
    N=float(input("Sisesta N:"))
    if N<0:
        j+=N  
print(j)

#7. Вывести на экран числа, кратные К из промежутка [А,В].

for i in range(2,20,2):
    if i%2==0:
        print(i)

#8. В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
S=float(input("Sisesta rahasumma:"))
N=int(input("aastate arv:"))
print((S+S*0.03)*N, "euro")

#9. Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
for i in range(10,21,1):
    print(i**2)

#10.Вводят 15 чисел. Определить, сколько среди них целых.

j=0
for i in range(1,16,1):
    A=float(input(" sisesta A:"))
    int(A)==A
    if int(A)==A: j+=1
print(j)


j=0
i=0
while True:
    i+=1
    A=float(input("sisesta A:"))
    if int(A)==A: j+=1
    if i==15: break
print(j)


j=0
i=0
while i<15:
    i+=1
    A=float(input(f"sisesta A:"))
    if int(A)==A: j+=1
print(j)

