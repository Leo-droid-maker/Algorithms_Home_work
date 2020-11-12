import timeit
import cProfile
import random as rd


def get_odd_even(num):
    odd = 0
    even = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10
    return odd, even


print(timeit.timeit('get_odd_even(52048)', number=100, globals=globals()))  # 0.00015471799997612834
print(timeit.timeit('get_odd_even(5204896456)', number=100, globals=globals()))  # 0.0003167810009472305
print(timeit.timeit('get_odd_even(7894563124898435)', number=100, globals=globals()))  # 0.0005802050000056624
print(timeit.timeit('get_odd_even(45678912345678147258369741852)', number=100, globals=globals()))
# 0.0010795180005516158

cProfile.run('get_odd_even(12367)')
# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:6(get_odd_even)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('get_odd_even(45678912345678147258369741852)')
# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:6(get_odd_even)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('*' * 100)


def rec(number, odd_new=0, even_new=0):
    while number != 0:
        if number % 2 == 0:
            even_new += 1
        else:
            odd_new += 1
        return rec(number // 10, odd_new, even_new)


print(timeit.timeit('rec(456189863)', number=100, globals=globals()))  # 0.0004102529983356362
print(timeit.timeit('rec(17317894235)', number=100, globals=globals()))  # 0.0004958989993610885
print(timeit.timeit('rec(9871342450000000000)', number=100, globals=globals()))  # 0.0009674499997345265
print(timeit.timeit('rec(412430984312310000000000000)', number=100, globals=globals()))  # 0.0014329550012917025
print(timeit.timeit('rec(9999999933846722203938475682910191873653728191)', number=100, globals=globals()))
# 0.0019858279993059114

cProfile.run('rec(456189863)')
# 13 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:65(rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('rec(17317894235)')
# 15 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      12/1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:65(rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('rec(9871342450000000000)')
# 23 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      20/1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:65(rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('rec(9999999933846722203938475682910191873653728191)')
# 50 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      47/1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:65(rec)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('*' * 100)


def get_odd_1(a):
    odd_list = []
    for i in a:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


def get_even_1(a):
    even_list = []
    for i in a:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def find_odd_even_in_list_1(n, min_=0, max_=100):
    array = [rd.randint(min_, max_) for _ in range(n)]
    odd = get_odd_1(array)
    even = get_even_1(array)
    return f' {odd} ,\n {even}'


print(timeit.timeit('find_odd_even_in_list_1(10)', number=100, globals=globals()))  # 0.0018872920009016525
print(timeit.timeit('find_odd_even_in_list_1(20)', number=100, globals=globals()))  # 0.004679841000324814
print(timeit.timeit('find_odd_even_in_list_1(30)', number=100, globals=globals()))  # 0.006637018999754218
print(timeit.timeit('find_odd_even_in_list_1(40)', number=100, globals=globals()))  # 0.007440232999215368
print(timeit.timeit('find_odd_even_in_list_1(50)', number=100, globals=globals()))  # 0.008290119998491718

cProfile.run('find_odd_even_in_list_1(10)')
# 70 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:109(get_odd_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:117(get_even_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:125(find_odd_even_in_list_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:126(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('find_odd_even_in_list_1(50)')
# 324 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:109(get_odd_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:117(get_even_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:125(find_odd_even_in_list_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:126(<listcomp>)
#        50    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        50    0.000    0.000    0.000    0.000 random.py:244(randint)
#        50    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        67    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('find_odd_even_in_list_1(80)')
# 509 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:109(get_odd_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:117(get_even_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:125(find_odd_even_in_list_1)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:126(<listcomp>)
#        80    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        80    0.000    0.000    0.000    0.000 random.py:244(randint)
#        80    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        80    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

print('*' * 100)


def get_odd(a):
    odd_list = [i for i in a if i % 2 != 0]
    return odd_list


def get_even(a):
    even_list = [i for i in a if i % 2 == 0]
    return even_list


def find_odd_even_in_list(n, min_=0, max_=100):
    array = [rd.randint(min_, max_) for _ in range(n)]
    odd = get_odd(array)
    even = get_even(array)
    return f' {odd} ,\n {even}'


print(timeit.timeit('find_odd_even_in_list(10)', number=100, globals=globals()))  # 0.00270662699949753
print(timeit.timeit('find_odd_even_in_list(20)', number=100, globals=globals()))  # 0.003548712000338128
print(timeit.timeit('find_odd_even_in_list(30)', number=100, globals=globals()))  # 0.004883677000179887
print(timeit.timeit('find_odd_even_in_list(40)', number=100, globals=globals()))  # 0.0070401180000772
print(timeit.timeit('find_odd_even_in_list(50)', number=100, globals=globals()))  # 0.007157746998927905

cProfile.run('find_odd_even_in_list(10)')
# 61 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:146(get_odd)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:147(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:151(get_even)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:152(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:156(find_odd_even_in_list)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:157(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('find_odd_even_in_list(50)')
# 269 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:146(get_odd)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:147(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:151(get_even)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:152(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:156(find_odd_even_in_list)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:157(<listcomp>)
#        50    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        50    0.000    0.000    0.000    0.000 random.py:244(randint)
#        50    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        50    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        60    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('find_odd_even_in_list(80)')
# 426 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:146(get_odd)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:147(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:151(get_even)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:152(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:156(find_odd_even_in_list)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_1.py:157(<listcomp>)
#        80    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        80    0.000    0.000    0.000    0.000 random.py:244(randint)
#        80    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        80    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        97    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


print('Вывод: На примере простого алгоритма можно увидеть, что быстрее всего отработала функция с\n'
      'простым циклом (самая первая).Эта же функция, но рекурсивно отработала медленнее. В принципе, во всех пример\n'
      'результаты были похожи на линейную зависимость. Далее, я попытался усложнить задачу и разделил функцию на три.\n'
      'В этом случае уже стало интереснее. Время выполнение алгоритма возросло. И профайлер указал, \n'
      'что можно оптимизировать\n'
      'например уменьшить количество вызовов. В функциях get_odd_1 и get_even_1 я использовал встроенную функцию\n'
      'append. Заменив использование этой функции на генератор (get_odd, get_even), мне удалось уменьшить кол-во\n'
      'вызовов (напр. 426 function calls против 509 function calls). Так же через профайлер можно увидеть\n, '
      'что генерация случайных чисел вызывается пропорционально длине списка.')
