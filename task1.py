list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def list_revers(list):
    for i in reversed(list):
        yield i

for i in list_revers(list1):
    print(i)