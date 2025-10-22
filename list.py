N=int(input(" Введите число N:")) #вводим число N
list=[0,1]
a = 0
b = 0
sum = 0
while a < (N-2):
  list.append(list[a]+list[a+1])
  a+=1
print("Исходный список:")
print(list)
a = 0
min = list[0]
max = list[0]
while a <= (N-1): 
  #print(list)
  #print(a)
  if a%2 == 0:
    list[a] = list[a] * 2
  else:
    list[a] = list[a] ** 2
  if min >= list[a]:
    min=list[a]
  if max <= list[a]:
    max=list[a]
  sum+=list[a]
  a+=1
median = sum/N
print("Изменённый список:")
print(list)
a = 0
while a <= (N-1): 
  if list[a] > median:
    b+=1
  a+=1
print("Минимальный элемент:", min)
print("Максимальный элемент:", max)
print("Длина списка:", len(list))
print("Количество элементов, большее медианного значения списка:", b)
