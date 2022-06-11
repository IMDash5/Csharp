import math

# 1. Найти НОК двух чисел

# N1 = 36
# N2 = 48

# def NOK(Num1, Num2):
#     i = 1
#     res = False
#     while res != True:
#         if i % Num1 == 0 and i % Num2 == 0:
#             res = True
#             return i
#         else:
#             i = i + 1
# print(NOK(N1, N2))

#_________________________________________________________________________________________

# 2. Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 
# d = 0.001
# i = 0
# while d != 1:
#     i = i + 1
#     d = d * 10
# print(round(math.pi, i))

#_________________________________________________________________________________________________

# 3. Составить список простых множителей натурального числа N

# def Multi(arg):
#     Spisok = []
#     i = 1
#     while arg >= i:
#         if arg % i == 0:
#             Spisok.append(i)
#             arg // i
#             i = i + 1
#         else:
#             i = i + 1
#     return Spisok
# print(Multi(91))

#__________________________________________________________________________________________________

#4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# spisok = [1, 2, 3, 5, 1, 5, 3, 10]
# i = 0
# while i < len(spisok):
#     if spisok.count(spisok[i]) > 1:
#         spisok.remove(spisok[i])
#         i = i + 1
#     else:
#         i = i + 1
# print(spisok)

# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

# with open ("nums.txt", "r") as Numbers:
#     Nums = Numbers.read()
#     i = 0
#     num = ""
#     NewList = []
#     while i < len(Nums):
#         if Nums[i] == " ":
#             NewList.append(int(num))
#             num = ""
#             i = i + 1
#         else:
#             num = num + Nums[i]
#             i = i + 1
#     NewList.append(int(num))
#     print(NewList)

# i = 0
# while i < len(NewList):
#     if NewList[i] % 2 == 0:
#         NewList.remove(NewList[i])
#     else:
#         i = i + 1
# print(NewList)

# with open ("nums.txt", "w") as f:
#     for i in NewList:
#         f.write(f"{i} ")

#__________________________________________________________________________________________