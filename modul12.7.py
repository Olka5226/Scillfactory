per_cent={'ТБК':5.6, 'СКБ':5.9, 'ВТБ':4.28, 'СБЕР':4.0}
money=int(input('Введите сумму:'))
deposit=[5600.0, 5900.0, 4280.0, 4000.0]
for key in per_cent:
    deposit.append(per_cent[key]*money/100)
max_deposit=max(deposit)
print(deposit)
print('Max сумма, которую вы можете получить' + str(max_deposit))
