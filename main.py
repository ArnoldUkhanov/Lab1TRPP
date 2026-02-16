arr = []
n = int(input("Сколько элементов (до 15): "))

for i in range(n):
    x = int(input())
    arr.append(x)

print("Массив:")
for x in arr:
    print(x, end=" ")