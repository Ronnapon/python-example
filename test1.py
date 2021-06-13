from itertools import combinations


def listIndexes(list1, list2):
    newList = list()
    for x in list2:
        newList.append(list1.index(x))
    return newList


def listSum(list1):
    newList = list()
    someList = list()
    for x in range(1, len(list1), 1):
        print(x)
        print(list(combinations(list1, x)))
        for y in list(combinations(list1, x)):
            if sum(y) == 7:
                newList.append(listIndexes(list1, y))


listSum([1, 4, 5, 7, 3, 2])
