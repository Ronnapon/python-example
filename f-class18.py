# Extending-build
class Text(str):
    def dupicate(self):
        return self + self


class List(list):
    def append(self, object):
        print("Append")
        return super().append(object)


text = Text("Python")
print(text.lower())
print(text.dupicate())

list1 = List([1, 2, 3])
print(list1)
list1.append(4)
print(list1)
