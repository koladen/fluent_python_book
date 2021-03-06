#ЧАСТЬ 1, ПРИМЕР 1:

# import collections
# from random import choice
#
# Card = collections.namedtuple('Card', "rank suit")
#
#
# class FrenchDeck:
#     ranks = [rank for rank in range(2, 11)] + list('JQKA')
#     suits = 'вини бубы крести червы'.split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __len__(self): #Описывая метод __len__ мы даем возможность определить величину данного класса. Без описания
#         return len(self._cards) # __len__, конструкция len(deck) - выдаст ошибку
#
#     def __getitem__(self, item): #А данный метод позволяет обратиться к элементу коллекции по индексу. Не реализуем,
#         return self._cards[item] # выдаст ошибку при обращении. Кроме того, реализовав данный метод, мы определяем класс
#     # как последовательность???? к которой, например, может обращаться меотд choice из random
#     # Поскольку метод __getitem__ делегирует выполнение оператору [] объекта self._cards, класс начинает поддерживать
#     # срезы
#     # А так же, автоматически начинает работать итерирование. Итерирование часто подразумевается неявно. Если в
#     # коллекции отсутствует метод __contains__, то оператор in производит последовательный просмотр коллекции. В нашем
#     # классе оператор in работает, поскольку этот класс итерируемый
#     # В следствие реализации методов __len__ и __getitem__, класс FrenchDeck начинает вести себя как стандартная
#     # последовательность и использовать базовые средства языка, например итерирование и получение среза, а так же работу
#     # методов reversed и sorted
#     # Как правило, специальный метод вызывается неявно. Например, for i in x: вызывает метод iter(x), который в свою
#     # очередь вызывает x.__iter__(), если он реализован
#
#
# deck = FrenchDeck()
#
# print(deck[-1])
# print(choice(deck))
# print(deck[1:5])
# for card in deck[7:10]:
#     print(card)
# print(Card(10, 'вини') in deck)
# suit_values = dict(вини=3, червы=2, бубы=1, крести=0)
#
#
# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value*len(suit_values) + suit_values[card.suit]
#
#
# for card in sorted(deck, key=spades_high):
#     print(card)

#ЧАСТЬ 1, ПРИМЕР 2:
#####################################################ПРИМЕР 2###########################################################
from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self): # Вызывается для получения строкового представления объекта. это однозначное представление
        # объекта в виде строки, которое можно использовать, чтобы воссоздать точно такой же объект, а если это
        # невозможно, то вывести какое-нибудь полезное сообщение. __str__ используется, когда нужно вывести красивое
        # или понятное представление объекта для человека
        return f'Vector({self.x}, {self.y})'

    def __abs__(self): # Вызывается при получении модуля
        return hypot(self.x, self.y)

    def __bool__(self): # Вызывается при приведении экземпляра класса к булевому типу. По умолчанию, любой объект
        # пользовательского класса считается Истинным, но положение меняется, если реализован хотя бы один из методов:
        # __bool__ или __len__. Этот метод можно было реализовать проще: return bool(self.x or self.y). Оператор or
        # работает так: если х - истина, возвращаем его, иначе возвращаем y независимо от его значения
        return bool(abs(self))

    def __add__(self, other): # Вызывается при вызове оператора +. Не модифицирует текущий объект, а возвращает новый!
        #Это ожидаемое поведение для подобных операторов! Так нужно делать всегда!
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar): # Вызывается при вызове оператора *. Не модифицирует текущий объект, а возвращает новый!
        #Это ожидаемое поведение для подобных операторов! Так нужно делать всегда!
        if isinstance(scalar, Vector):
            return Vector(self.x * scalar.x, self.y * scalar.y)
        else:
            return Vector(self.x * scalar, self.y * scalar)

vec = Vector(4, 2)
vec2 = Vector(5, 7)
vec3 = Vector(0, 0)
print(vec) #Vector(4, 2)
print(vec2) #Vector(5, 7)
print(bool(vec3)) #False
print(abs(vec)) #4.47213595499958
print(vec+vec2) #Vector(9, 9)
print(vec*7) #Vector(28, 14)
print(vec*vec2) #Vector(20, 14)