# def decor_maker(dec_arg1, dec_arg2):
#     print('Я создаю декораторы! Я получил следующие аргументы:', dec_arg1, dec_arg2)
#
#     def my_decorator(func):
#         print('Я - декоратор! Я получил следующие аргументы:', dec_arg1, dec_arg2)
#
#         def wrapper(func_arg1, func_arg2):
#             print('Я - обёртка вокруг декорируемой функции. Я получил следующие аргументы:'
#                   '\t декоратора: {} , {}'
#                   '\t функции: {}, {}'.format(dec_arg1, dec_arg2, func_arg1, func_arg2))
#             return func(func_arg1, func_arg2)
#         print('Я возвращаю обёрнутую функцию.')
#         return wrapper
#     print('Я возвращаю декоратор')
#     return my_decorator
#
#
# def decorated_func():
#     print('я декорируемая функция')
#
#
# @decor_maker('Anton', 'Nikola')
# def new_decorated_func(func_arg1, func_arg2):
#     print('Я - декорируемая функция и я знаю только о своих аргументах: {0}, {1}'.format(func_arg1, func_arg2))
#
#
# new_decorated_func('Lilia', 'Anya')


