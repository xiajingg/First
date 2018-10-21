# from model.PowerFunction import power
# from model.Factorial import fact
#
# print("hello")
print(100 + 3)
#
#
# # name=input("请输入：")
# # print("The name is :",name)
#
# def abs(num):
#     if num >= 0:
#         return num
#     else:
#         return ("|a|=", -num)
#
#
# #  转义字符
# # print(r'''我是"shazi"''')
#
# sum = 0
# for x in range(101):
#     sum = sum + x
#
# print(sum)
#
# sum = 0
# n = 100
# while n > 0:
#     sum = sum + n
#     n = n - 1
# print(sum)
#
# b = abs(9)
# print(b)
#
# c = power(2, 4)
# print(c)
#
# d = fact(100)
# print(d)
#
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
#     print(d[key])
#
e = [(1, 1), (2, 4), (3, 9)]
for x, y in e:
    print(x, y)
print(list(range(1, 11)))

l = []
for x in range(1, 11):
    l.append(x * x)
print(l)

g = (x * x for x in range(1, 11))
print("g size:", g.__sizeof__())
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


fib(6)

g = lambda n: n % 2 == 1
l = list(filter(g, range(1, 20)))
print(l)