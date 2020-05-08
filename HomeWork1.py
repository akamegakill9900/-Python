num = input("Введите любое число: ")
print(str(num))

words = input("Какого цвета ёлка?")
print(words)

time_s = input("Введите время в секундах:")
time_normal_h = (int(time_s) // 3600)
time_normal_m = (int(time_s) % 3600) // 60
time_normal_s = (int(time_s) % 3600) % 60
print(f"В стандартном формате чч:мм:сс это будет: {time_normal_h}:{time_normal_m}:{time_normal_s}")

n = int(input("Введите число n: "))
print(n + n * n + n * n * n)


numb = int(input("Введите любое положительное целое число: "))
d = -1
while numb > 0:
    numb_max = numb % 10
    numb //= 10
    if d < numb_max:
        d = numb_max
print(d)


revenue = int(input("Введите значение выручки вашей фирмы: "))
costs = int(input("Введите значение издержек вашей фирмы: "))
if revenue > costs:
    print("Фирма работает в прибыль")
    profit = revenue - costs
    print("Чистая прибыль составляет: ", profit)
    profitability = profit / revenue
    print("Рентабельность: ", profitability)
    staff_count = int(input("Введите число персонала: "))
    print('Прибыль на 1 сотрудника составляет: ', profit / staff_count )
else:
    print("Фирма работает в убыток")


a = int(input("Результат в первый день: "))
b = int(input("Достигнутая дистанция: "))
count = 1
while a < b:
    a += a * 0.1
    count += 1
print(count)