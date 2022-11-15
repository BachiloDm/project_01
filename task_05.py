# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000
# Решение
i=1 # количество месяцев
total_expenses=expenses
while i<=11:
    expenses=expenses+expenses*.03
    total_expenses=total_expenses+expenses
    i+=1
print(expenses)
print(total_expenses)
salary=salary*12
print(salary)
print('Нужно взять в долг',round(total_expenses-salary,2),'рублей')