salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.03  # Ежемесячный рост цен
months = 10  # Количество месяцев, которые нужно продержаться

total_needed_capital = 0  # Общая необходимая подушка безопасности

for month in range(months):
    # Рассчитываем разницу между расходами и зарплатой
    deficit = spend - salary
    if deficit > 0:
        total_needed_capital += deficit  # Добавляем нехватку к общей подушке

    # Увеличиваем расходы на 3% для следующего месяца
    spend *= (1 + increase)

# Округляем до целого числа
total_needed_capital = round(total_needed_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", total_needed_capital)
