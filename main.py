# Зарплата = смены + премия (выполнение плана личного + выполнения плана общего)
# Планы: батут / паркур / дни рождения
# Общий план и личный план

# salary - зарплата
# work_shift - рабочие смены
# work_shift_quantity - количество рабочих смен
# work_shift_cost - ставка за рабочую смену
# bonus - премия
# kpi_ideal_dialogs - идеальные диалоги
# kpi_bonus - фиксированный бонус
# personal_fact - фактические продажи (значение "0"), чтобы не выбивало ошибку

# personal_tramp_plan - личный план по батутам
# personal_hb_plan - личный план по дням рождениям
# personal_parkour_plan - личный план по паркуру

# all_tramp_plan - общий план по батутам
# all_hb_plan - общий план по дням рождениям
# all_parkour_plan - общий план по паркуру

# personal_plan - личный план
# all_plan - общий план

# answer - решение пользователя
# personal_data_entered - флаг ввода данных (True/False)

#Основные фиксированные показатели
kpi_bonus = 10_000
kpi_ideal_dialogs = 3_000
work_shift_cost = 1_000

#Ввод смен
work_shift_quantity = int(input('Введите количество рабочих смен в месяц: '))
work_shift = work_shift_quantity * work_shift_cost
print(f'Сумма за выход в месяц: {work_shift} руб.')

#Разделитель
print('-' * 15)

#Ввод личных данных
answer = input('Внести данные ПЕРСОНАЛЬНОГО плана? (Да/Нет) ').lower()
if answer == 'да':
    personal_tramp_plan = int(input('Введите сумму ЛИЧНОГО плана по батутам: '))
    personal_hb_plan = int(input('Введите сумму ЛИЧНОГО плана по дням рождения: '))
    personal_parkour_plan = int(input('Введите сумму ЛИЧНОГО плана по паркуру: '))
    personal_plan = personal_tramp_plan + personal_parkour_plan + personal_hb_plan

    # Разделитель
    print('-' * 15)
    
    print(f'Общая сумма ЛИЧНОГО плана: {personal_plan} руб.')
    
    # Разделитель
    print('-' * 15)
    
    personal_tramp_fact = int(input('Введите ФАКТИЧЕСКУЮ сумму продаж по батутам: '))
    personal_hb_fact = int(input('Введите ФАКТИЧЕСКУЮ сумму продаж по дням рождения: '))
    personal_parkour_fact = int(input('Введите ФАКТИЧЕСКУЮ сумму продаж по паркуру: '))
    personal_fact = personal_tramp_fact + personal_parkour_fact + personal_hb_fact
    
    # Разделитель
    print('-' * 15)
    
    print(f'Фактическая сумма личных продаж: {personal_fact} руб.')

    personal_data_entered = True
else:
    personal_data_entered = False
    personal_fact = 0

#Разделитель
print('-' * 15)

#Ввод общих данных
answer = input('Внести данные ОБЩЕГО плана? (Да/Нет) ').lower()
if answer == 'да':
    all_tramp_plan = int(input('Введите сумму ОБЩЕГО плана по батутам: '))
    all_hb_plan = int(input('Введите сумму ОБЩЕГО плана по дням рождения: '))
    all_parkour_plan = int(input('Введите сумму ОБЩЕГО плана по паркуру: '))
    all_plan = all_tramp_plan + all_parkour_plan + all_hb_plan

    # Разделитель
    print('-' * 15)
    
    print(f'Общая сумма ОБЩЕГО плана: {all_plan} руб.')
    
    # Разделитель
    print('-' * 15)
    
    all_tramp_fact = int(input('Введите ФАКТИЧЕСКУЮ сумму продаж по батутам (отдел): '))
    all_hb_fact = int(input('Введите ФАКТИЧЕСКУЮ сумму продаж по дням рождения (отдел): '))
    all_parkour_fact = int(input('Введите ФАКТИЧЕСКУЮ сумму продаж по паркуру (отдел): '))
    all_fact = all_tramp_fact + all_parkour_fact + all_hb_fact

    # Разделитель
    print('-' * 15)
    
    print(f'Фактическая сумма общих продаж: {all_fact} руб.')

    all_data_entered = True
else:
    all_data_entered = False
    all_fact = 0

#Разделитель
print('-' * 15)

#Расчет премий
personal_bonus = 0
if personal_data_entered and all_data_entered:
    personal_percent = 0
    if all_fact >= all_plan:  # Отдел выполнил план
        if personal_fact >= personal_plan:
            personal_percent = 0.08
        else:
            personal_percent = 0.05
    else:  # Отдел НЕ выполнил план
        if personal_fact >= personal_plan:
            personal_percent = 0.06
        else:
            personal_percent = 0.04

    personal_bonus = personal_fact * personal_percent
    print(f'Премия за личные продажи: {round(personal_bonus)} руб.')

#Премия за выполнение общего плана (абонементы)
group_bonus = 0
if all_data_entered:
    plan_percent = (all_fact / all_plan) * 100 if all_plan > 0 else 0
    if 70 <= plan_percent < 80:
        group_bonus = 670
    elif 80 <= plan_percent < 100:
        group_bonus = 1_670
    elif 100 <= plan_percent <= 110:
        group_bonus = 3_500
    elif plan_percent > 110:
        group_bonus = 6_000
    print(f'Премия за выполнение общего плана отдела: {group_bonus} руб.')

#Итоговая зарплата
salary = work_shift + kpi_bonus + kpi_ideal_dialogs + personal_bonus + group_bonus
print('-' * 15)
print(f'ИТОГОВАЯ ЗАРПЛАТА: {round(salary)} руб.')
