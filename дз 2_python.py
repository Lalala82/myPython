
item_1 = 25
item_2 = 4

#Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2
print ("result_sum=", result_sum)

#Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению
result_subtr = item_1 - item_2
print("result_subtr=", result_subtr)

#Создать переменную result_multi в которой вы умножаете item_1 на item_2
result_multi = item_1 * item_2
print("result_multi=", result_multi)

#Создать переменную result_exp в которой вы item_1 возводите в степень item_2
result_exp = item_1 ** item_2
print("rresult_exp=", result_exp)

#Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
import math
result_m_exp = math.pow(item_1, item_2)
print("result_m_exp=", result_m_exp)

#. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_1 ** 0.5
print("result_s_root", result_s_root)

#. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math
result_m_s_root = math.sqrt(item_1)
print("result_m_s_root=", result_m_s_root)

#Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow
result_mp_s_root = math.pow(item_1, 0.5)
print("result_mp_s_root=", result_mp_s_root)


item_1 = 35
item_2 = 8

#Создать переменную result_division в которой вы разделите item_1 на item_2
result_division = item_1 / item_2
print("result_division=", result_division)

#Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division
result_division = 67.9494
result_m_floor = math.floor(result_division)
print("result_m_floor=", result_m_floor)

#Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division
result_division = 27.6543
result_m_ceil = math.ceil(result_division)
print("result_m_ceil=", result_m_ceil)

#. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_division = 87.9245
result_int = int(round(result_division))
print("result_int=", result_int)

#Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1 // item_2
print("result_no_division_loss=", result_no_division_loss)

#. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2
print("result_division_loss=", result_division_loss)


item_3 = 15
item_3 += 10
print("item_3=", item_3)


item_3 -= 5
print("item_3=", item_3)


item_3 *= 3
print("item_3=", item_3)


item_3 /= 2
print("item_3=", item_3)


item_3 **= 2
print("item_3=", item_3)

item_3 **= 0.5
print("item_3=", item_3)










