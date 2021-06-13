# Making Custom Container
class TagCloud:
    def __init__(self):
        self.tag = {}

    def add(self, tag):
        self.tag[tag] = self.tag.get(tag, 0)+1

    def __setitem__(self, tag, count):
        self.tag[tag] = count

    def __getitem__(self, tag):
        return self.tag.get(tag, 0)

    def __len__(self):
        print(f"Count Dict = {len(self.tag)}")
        return len(self.tag)

    def __iter__(self):
        return iter(self.tag)


tagcloud = TagCloud()
# tagcloud.add("Ronnapon")
# tagcloud.add("Ronnapon")
tagcloud['A'] = 1  # Setitem
tagcloud['B'] = 2  # Setitem
tagcloud['A']  # Getitem
tagcloud['B']  # Getitem
tagcloud.tag["bbbb"] = 5
len(tagcloud)
