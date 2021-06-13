# Properties Attibute
class TagCloud:
    #     def __init__(self, price):
    #         self.setitem(price)

    #     def getitem(self):
    #         return self.price

    #     def setitem(self, price):
    #         if price < 0:
    #             raise ValueError("Define Number incorrectly")
    #         self.price = price

    #     price = property(getitem, setitem)

    # tagcloud = TagCloud(10)

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Define Number incorrectly")
        self.__price = price


tagcloud = TagCloud(10)  # Call init & price.setter
print(tagcloud.price)  # Call get Value
