from collections import Counter

PERIOD = 4

number_of_companies = int(input('Введите количество предприятий: '))
company = Counter()

for i in range(number_of_companies):
    comp_name = input(f'Введите название {i+1} - го предприятия: ')
    c = 0
    while c != PERIOD:
        profit = int(input(f'Введите прибыль предприятия {comp_name} за {c+1} - й квартал: '))
        company[comp_name] += profit
        c += 1


average_profit = sum(company.values()) / number_of_companies
print('*' * 50)
print(f'Общая прибыль предприятий: {sum(company.values()):.2f},\nСредняя прибыль {average_profit:.2f}')

print(f'Предприятие с наибольшей прибылью: {company.most_common(1)[0][0]}')

print(f'Предприятие с наименьшей прибылью: {company.most_common()[:-1-1:-1][0][0]}')

print(f'Предприятия с прибылью меньше средней: {list(i for i in company if company[i] < average_profit)}')
print(f'Предприятия с прибылью больше средней: {list(i for i in company if company[i] > average_profit)}')







# a = Counter()
# b = Counter('arbakadabra')
# c = Counter({'cats': 10, 'dogs': 23})
#
# print(a, b, c, sep='\n')
#
# print(b['z'])
# b['z'] = 3
# print(b)
#
# print(b.most_common(3))
# print(list(b.elements()))
# x = {'q': 3, 'w': 12}
# b.update(x)
# print(b)
#
# print(sum(b.values()))





















