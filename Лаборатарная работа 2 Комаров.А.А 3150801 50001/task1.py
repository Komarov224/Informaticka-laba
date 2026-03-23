money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_month = 0 # счетчик месяцев

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while((money_capital + salary - spend) > 0):
    money_capital = money_capital - (spend - salary) # взяли с подушки
    count_month = count_month + 1 # прожили месяц
    spend = spend + spend * increase # повышение цен


print("Количество месяцев, которое можно протянуть без долгов:", count_month)
