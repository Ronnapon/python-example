# Private Member  (ไม่ให้เรียก หรือสร้างตัวแปร จากข้างนอก function)


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag] = self.__tags.get(tag, 0)+1

    def __setitem__(self, tag, count):
        self.__tags[tag] = count

    def __getitem__(self, tag):
        return self.__tags.get(tag, 0)

    def __len__(self):
        print(f"Count Dict = {len(self.__tags)}")
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


tagcloud = TagCloud()
print(tagcloud.__dict__)  # Hold Attibute in Class
tagcloud.add("Python")
tagcloud.add("Python")
tagcloud.add("Python")
print(tagcloud._TagCloud__tags)  # เรียกใช้ private member
