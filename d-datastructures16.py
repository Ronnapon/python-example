# Comprehensive
# List
from sys import getsizeof
test1 = [x * 2 for x in range(1, 6)]
print(test1)

# Set
test1 = {x * 2 for x in range(1, 6)}
print(test1)

# Dict
test1 = {x: (index+1)*2 for index, x in enumerate("ABC")}
print(test1)

# Generator Object (ใช้ memory น้อยมาก กรณีมีการ ลูปเยอะๆ)
test1 = (x * 2 for x in range(10000000))
print(test1)
print(getsizeof(test1))


# Question (By Big)
sentence = "This is a common interview question"
sentence = sentence.replace(" ", "")
sentence = sentence.lower()
sentence = sorted(list(sentence))
org_alphbet = ""
alphbet_same = []
for index, alpabet in enumerate(sentence):
    if index == 0:
        org_alphbet = alpabet
    if alpabet == org_alphbet:
        alphbet_same.append(alpabet)
    org_alphbet = alpabet
# print(set(alphbet_same))

# Question (By Mosh)
sentence = "This is a common interview question"
sentence_num = {}
for alpabet in sentence:
    if alpabet in sentence_num:
        sentence_num[alpabet] += 1
    else:
        sentence_num[alpabet] = 1
sentence_sort1 = sorted(sentence_num.items(), key=lambda item: item[1])
sentence_sort2 = sorted(sentence_num.items(),
                        key=lambda item: item[1],
                        reverse=True)
print(sentence_sort1)
print(sentence_sort2)

list1 = [0.3, 0.3, 0.3, 0.1]
print(round(sum(list1)))
