#Пример 7.3
# promos = []
#
#
# def reg_promos(func):
#     promos.append(func)
#     return func
#
#
# @reg_promos
# def promo1():
#     print(promo1.__name__)
#
#
# @reg_promos
# def promo2():
#     print(__name__)
#
#
# print(promos) # [<function promo1 at 0x00000000021F3DC8>, <function promo2 at 0x00000000021F3E58>]

#Пример 7.9
#
# def make_averager():
#     series = [] # это та самая свободная переменная
#     def average(n):
#         series.append(n)
#         total = sum(series)
#         return total/len(series)
#     return average
#
# avg = make_averager()
# print(avg(10)) #10
# print(avg(11)) #10.5
# print(avg.__code__.co_freevars) #('series',)
# print(avg.__closure__) #(<cell at 0x0000000002119798: list object at 0x00000000003C5208>,)
# print(avg.__closure__[0].cell_contents) #[10, 11]

# #Пример 7.14
#
# def make_averager():
#     total = 0
#     count = 0
#     def average(n):
#         nonlocal count, total #Тут мы объявляем эти переменные свободными, т.к. если эот не сделать, они станут
#         # локальными и код выдаст ошибку. А в этом случае их значение будет сохраняться так же, как в предыдущем примере
#         count += 1
#         total += n
#         return total/count
#     return average
#
# avg = make_averager()
# print(avg(10)) #10
# print(avg(11)) #10.5


#Пример с singledispatch
from functools import singledispatchmethod
class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

a = Negator()
print(a.neg(True)) #False
print(a.neg(1)) #-1