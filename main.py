arr = []
n = int(input("Сколько элементов (до 15): "))

if n > 15:
    print("Максимум 15!")
    n = 15
    print(10/0)

for i in range(n):
    x = int(input())
    arr.append(x)

print("Массив:")
for x in arr:
    print(x, end=" ")
