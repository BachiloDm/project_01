# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

#  РЕШЕНИЕ
my_cities=['Moscow','Tver','Tula']
citizens=[12,1,0.5]
# vmeste=my_cities+citizens
vmeste=[my_cities,citizens]
# print(vmeste)
print('Начеление ',my_cities[1], citizens[1],' человек')
count=0
for i in citizens:
        count=count+i
print('Итого размер населения -',count,'человек')