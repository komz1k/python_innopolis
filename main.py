# def sum_string (*params: str):
# s=""
# for i in range (len(params)):
#     s=s+params[i]
# return s
# print(sum_string("abc","vb"))


import asyncio
# def append_to_list (s: str, a: list[str]):
#   a.append(s.upper())
#  return a
# print(append_to_list("дАша",[1,2,3]))


# from math import sqrt
# def area_calculator (s: str):
#   def square (x):
#      return x**2
# def rectangle (x,y):
#     return x*y
# def triangle (x,y,z):
#     return sqrt(((x+y+z)/2)*(((x+y+z)/2)-x)*(((x+y+z)/2)-z)*(((x+y+z)/2)-y))
# def circle (r):
#   return 3.14*r*r
#   if s=="square":
#      return square
#  if s=="rectangle":
#      return rectangle
#  if s=="circle":
#     return circle
#  if s=="triangle":
#       return triangle
# print(area_calculator("rectangle")(3,6))
# def stepen (exp: int):
#   def square (x):
#       return x**2
#   def cub (x):
#       return x**3
#   def st (x):
#       return x**exp
#   if exp == 2:
#       return square
#   if exp == 3:
#       return cub
#   if exp!=2 and exp!=3:
#     return st
# print(stepen(4)(5))
# a = [
#  []
# ]
# n = 5
# m = 5
# table = [None] * n
# for g in range (n):
#    table[g] = [0] * m
# for i in range (n):
#   for j in range (m):
#    if i == j:
#        table[i][j] = 1
#    else:
#  table[i][j] = i+j
# for line in table:
# print(*(line))
# n = 5
# m = 6
# table = [None] * n
# for i in range (n):
# table[i] = [0] * m
# print([x*x for x in range (1,6)])
# print([[0]*5 for x in range(5)])
# s = input("Введите строку: ")
# s = s.split(" ")
# s1 = list(set(s))
# for i in range (len(s1)):
# print(s1[i], "-", s.count(s1[i]))
# s = input("Введите строку: ")
# s = s.split(" ")
# dict = {}
# for word in s:
# if word in dict:
#     dict[word] +=1
#  else:
#    dict[word]=1
# for word, count in dict.items():
#  print(word,"-", count)
# import  random
# def example ():
#   r= random.randint(0,2)
#    def good_morning ():
#      return "Good morning"
#  def good_day ():
#       return "Good day"
#  def good_evening ():
#    return "Good evening"
#  if r== 0:
#       return good_morning()
#   if r == 1:
#     return good_day()
# if r == 2:
#      return good_evening()
# print(example())
# def cache_decorator (func):
#  cache = {}
#  def wrapper (*args, **kwargs):
#      if args in cache:
#         return cache[args]
#    cache[args] = func(*args)
#     return cache[args]
#  wrapper.cache = cache

