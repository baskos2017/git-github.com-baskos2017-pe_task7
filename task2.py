list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square_even(list):
    list2 = [x**2 for x in list  if x % 2 == 0 ]
    print(list2)


square_even(list1)

list2 = []
i = 0
while i < len(list1):
    x = list1[i]
    if x % 2 == 0:
        x = x ** 2
        list2.append(x)
    i += 1

print(list2)