#1.���� ����������� ����� �� 20 �� 50. ���������� �� �� ���, ������� ������� �� 3, �� �� ������� �� 5.

for i in range(20,50+1):
    if i%3==0 and i%5>0:
        print(i)


#2.������ � ���������� 10 ��� �����.  �������� ����� � ������ ���� � ���������� ������� �� ���.

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

#3. ������ 8 �����. ����� �� ������������ (������ �������������).

j=1
i=0
while i<8:
    i+=1
    A=float(input(f"sisesta A:"))
    if A>0:
        if int(A)==A: j*=A
print(j)

#4.��������� � ������������ ����� � � ������� ����� ���� ����������� ����� �� 1 �� �.

A= int(input("Sisesta A:"))
if A>=0:
    print(sum(range(1, A+1)))
else: 
    print("See ei ole naturaalarv")


#5.��������� ���������, ������� �������� ������� �������� ���������� �� ������ � ���������� (1 ���� =
#2,5 ��) ��� �������� ���� �� 1 �� 20 ������.

for i in range (1,21,1):
    print(i*2.5)

#6.��������� ���������, ������� ��������� ����� ������ ������������� �� N �����. 
#�������� N �������� � ����������.
j=0
i=0
while i<5:
    i+=1
    N=float(input("Sisesta N:"))
    if N<0:
        j+=N  
print(j)

#7. ������� �� ����� �����, ������� � �� ���������� [�,�].

for i in range(2,20,2):
    if i%2==0:
        print(i)

#8. � ���� �� �������������� ����� �������� S ����. ����� ������ ����� ������ ����� N ���?
S=float(input("Sisesta rahasumma:"))
N=int(input("aastate arv:"))
print((S+S*0.03)*N, "euro")

#9. ��������� ���������, ��������� �� ����� �������� ����� �� 10 �� 20.
for i in range(10,21,1):
    print(i**2)

#10.������ 15 �����. ����������, ������� ����� ��� �����.

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

