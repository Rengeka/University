
from re import L
from sys import getsizeof

# ������� 1



# 2



# ������

print('''
   List
      ''');

lis = [1, 4, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 1, 2]
print(lis)



# ����� ���������
print(lis[0])   # ������
print(lis[2])   # ������



# ������������ �������� �������� ������
lis[1] = 2
print(lis)



# ���� � 4 �� 11 �������� � ����� � 1 
print(lis[3:10:1]) # 4 ������� ������������, 11 - ���

# ���� � 4 �� 10 �������� � ����� � 3
print(lis[3:9:3]) # 4 ������� ������������, 10 - ���

#print(crt[1:]) - � 2 �� ��������� ������� � ����� 1
#print(crt[:4]) - � 0 �� 5 ������� � ����� 1
#print(crt[1:4]) - � 2 �� 5 ������� � ����� 1



# ������ �������



# ���������� �������� � ����� ������
lis.append(20)
print(lis)

# ������� ���������� ��������� ����� �������� � ������
print(lis.count(1))

# ��������� ������� ������� ��������� �������� � ������
print(lis.index(2))

# �������� �������� �� ������ (� ������� ��� ��������) 
# (���� ������� ������ �� ��� ������ �� �������, ���� ��� �� ������ ��������� �������)
lis.pop()
print(lis)

# ���������� ������ �� �����������
lis.sort() # (����� ��������� � ����������� �������)
print(lis)



# ������� ��� ������ �� ��������

# ��������� ���� ������
print(type(lis))

# ��������� ������ ������
print(len(lis))

# �������� ������
del(lis)



# 3



# ������

print('''
   Tuple
      ''');

crt = ("Text", 2, True, 10.5)
print(crt)


# ��������� ���� �������
print(type(crt))

# ��������� ���� ������ �� ��������� �������
print(type(crt[1]))



# ������ � ��������� ��������
print(crt[0])
print(crt[-1])



# ���� � 2 �� 4 �������� � ����� � 1
print(crt[1:3:1]) # 2 ������� ������������, 4 - ���



# ������ ��������



# ������� ��������� ���������� �������� � ������
print(crt.count("Text"));

# ���������� ������ ������� �������� �� ���������, ���������� ������
print(crt.index(True))



# ������� ��� ������ � ���������



# ������ ���������
print(crt)
print(crt[2:4])
print(crt[1:])

# ��������� �����
print(len(crt))

# ��������� �������
print(getsizeof(crt))

# ��������
del(crt)

# 4



# ���������

print('''
   Set
      ''');

sett = {1,2,3,4,5}
print(sett)



# ������� ��� ������ � �����������



# ��������� �����
print(len(sett))



# ������ ��� ������ � ���������



# ���������� ��������
sett.add(6);
print(sett);

# �������� ��������
sett.remove(6)
print(sett);



# 5



# �������

print('''
   Dictionary
      ''');

dictt = {1:10, 2:20, 'key':5}
print(dictt)

# ��������� ���������
print(dictt['key'])
print(dictt[1])



# ������ ��� ������ � ���������



# ��������� ��������
print(dictt.get(1))

# �������� ��������
dictt.pop(2)
print(dictt)

# ��������� ������ 
print(dictt.keys());



# ������� ��� ������ � �����������



# ��������� �����
print(len(dictt))

# �������������� ����
print(list(dictt))



# ������� 2


print('''
   Task 2
      ''');



# 1



_set = [1,2,3]
_another_set = ["PC", "PS5", "XBOX SERIES X"]

print("{} price: ${}".format(_another_set[0], _set[0]))
print("{} price: ${}".format(_another_set[1], _set[1]))
print("{} price: ${}".format(_another_set[2], _set[2]))



# 2



print("Enter your age please")

age = int(input())

print("After 5 years your age will be : " + str(age + 5) + " years")



# 3




_str = "Text"
print('x' in _str)
print('X' in _str)

tpl = (True, 2, "ABC")
print(2 in tpl);

dct = {'A':"Text1", 3:"Text2"}
print(3 in dct)
print("Text1" in dct)