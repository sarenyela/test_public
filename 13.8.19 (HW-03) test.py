price_all = 0
while True:
    try:
        number_of_tickets = input('Укажите необходимое количество билетов ')
        number_of_tickets = int(number_of_tickets)
        if type(number_of_tickets) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(number_of_tickets):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'Для какого возраста билет №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 18 <= age_for_ticket < 25:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if number_of_tickets > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print('Сумма к оплате', price_all, 'руб. с учетом 10%-ой скидки за регистрацию более 3-х человек')
else:
    print('Сумма к оплате', price_all, 'руб.')