import timeit
import cProfile


def prime(n):
    count = 1
    num = 1
    prime_lst = [2]

    if n == 1:
        return 2

    while count != n:
        num += 2
        for el in prime_lst:
            if num % el == 0:
                break
        else:
            count += 1
            prime_lst.append(num)
    return num


print(prime(5))


def sieve(n):
    d = 1000
    sieve_lst = [i for i in range(d)]
    sieve_lst[1] = 0
    for i in range(2, d):
        if sieve_lst[i] != 0:
            j = i + i
            while j < d:
                sieve_lst[j] = 0
                j += i
    for i in sieve_lst:
        while sieve_lst.count(i) > 1:
            sieve_lst.remove(i)

    for i, item in enumerate(sieve_lst, 1):
        if n == i:
            return item

    # return sieve_lst


print(sieve(5))

print(timeit.timeit('prime(5)', number=100, globals=globals()))  # 0.00020694700288004242
print(timeit.timeit('prime(1)', number=100, globals=globals()))  # 1.966399941011332e-05
print(timeit.timeit('prime(7)', number=100, globals=globals()))  # 0.00034354899980826303

print('*' * 100)

print(timeit.timeit('sieve(5)', number=100, globals=globals()))  # 0.6622297700014315
print(timeit.timeit('sieve(1)', number=100, globals=globals()))  # 0.6577893069988932
print(timeit.timeit('sieve(7)', number=100, globals=globals()))  # 0.6541694890001963

print('*' * 100)

cProfile.run('prime(3)')
# 6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:5(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(7)')
# 10 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:5(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('*' * 100)

cProfile.run('sieve(2)')
# 1836 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.001    0.001    0.007    0.007 Lesson_4_Task_2.py:28(sieve)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:30(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#      1000    0.004    0.000    0.004    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       831    0.002    0.000    0.002    0.000 {method 'remove' of 'list' objects}

cProfile.run('sieve(3)')
# 1836 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.001    0.001    0.007    0.007 Lesson_4_Task_2.py:28(sieve)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:30(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#      1000    0.004    0.000    0.004    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       831    0.002    0.000    0.002    0.000 {method 'remove' of 'list' objects}


def sieve_2(n):
    d = 1000
    sieve_lst = [i for i in range(d)]
    sieve_lst[1] = 0
    res_list = []
    for i in range(2, d):
        if sieve_lst[i] != 0:
            j = i + i
            while j < d:
                sieve_lst[j] = 0
                j += i

    for i in sieve_lst:
        if i not in res_list:
            res_list.append(i)

    res_list.remove(0)

    for i, item in enumerate(res_list, 1):
        if n == i:
            return item

    # return sieve_lst
    # return res_list


print(sieve_2(5))

cProfile.run('sieve_2(5)')
# 175 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Lesson_4_Task_2.py:117(sieve_2)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:119(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       169    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

cProfile.run('sieve_2(7)')
# 175 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 Lesson_4_Task_2.py:117(sieve_2)
#         1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:119(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       169    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

print('После выполнения профайлера в первый раз, заметил, что функции count и remove внутри sieve()\n'
      ' имеют большое кол-во вызовов.\n'
      'решил исправить, заменив на цикл.\n'
      'Так же очень долго выполняется функция prime при поиске первого простого числа.')
