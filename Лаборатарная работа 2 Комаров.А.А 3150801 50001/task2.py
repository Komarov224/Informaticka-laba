salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # подушка безопасности

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

for i in range(10): # 10 месяцев трат
    money_capital = money_capital + (spend - salary) # берем в долг из подушки
    spend = spend + spend * increase # повышение цен

money_capital = round(money_capital) # округляем

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
