# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int,
# премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа
# и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

names = ["Иванов", "Петров", "Сидоров", "Егоров"]
bets = [35000, 40000, 45000, 50000]
prems = ['10.25%', '12.50%', '15.20%', '17.12%']
print({name: (bet * float(prem[:-1])/100) for name, bet, prem in zip(names, bets, prems)})

