import math
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_capital = 0
for month in range(months):
    total_capital += (spend * ((increase + 1) ** month)) - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(total_capital))
