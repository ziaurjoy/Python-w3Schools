
#
# def iterable_number(n):
#     for i in range(n):
#         yield i
#
# print(list(iterable_number(10)))

def filtering_number():
    n = 10
    for i in range(n):
        if i % 2 == 0:
            yield i
for i in filtering_number():
    print(i)
