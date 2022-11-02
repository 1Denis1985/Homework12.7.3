# дано ключ — название банка, значение — процент.
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую хотите положить под проценты: "))
# получим список-представление значений словаря
value_dict_percent = per_cent.values()
# так же, ключей словаря для более расширенного ответа в конце задачи
name_of_bank = list(per_cent.keys())

# Первый способ:
deposit = []
for item in value_dict_percent:
    deposit.append(int(money * item / 100))

# Второй способ:
# def calc_ann(value):
#     return int(money*value/100)
# deposit = list(map(calc_ann, value_dict_percent))


print(
    f"Максимальная сумма, которую вы можете заработать - {max(deposit)}, если вложите средства в: {name_of_bank[deposit.index(max(deposit))]}")
