# Abstact Class
from abc import ABC, abstractmethod


class InvalidOperationEorr(Exception):
    pass


class Steam(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationEorr("File Already Open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationEorr("File Already close")
        self.opened = False

    @abstractmethod
    def read(self):
        print("Read Method")


class FilesSteam(Steam):
    def read(self):
        print("Reading Data from File Steam")


class NetworkSteam(Steam):
    def read(self):
        print("Reading Data from Network Steam")


# Sub class have to have "read Method (Because read Function is Abstact Method)
class MemorySteam(Steam):
    # pass
    def read(self):
        super().read()
        print("Reading Data from Memory Steam")


steam = MemorySteam()
print("Initial", steam.opened)
steam.open()
print("Open", steam.opened)
steam.read()
steam.close()
print("Close", steam.opened)


# 1 Abstract class เป็นคลาสที่มีอย่างน้อย 1 Method เป็นประเภท
# Abstract Method
# 2 Abstract Method คือ Method ที่มีแต่ชื่อไม่มีเนื้อหาหรือการ
# ทางานของ Method
# 3 Abstract class ไม่สามารถสร้างเป็น Object ได้โดยตรงต้อง
# ถ่ายทอดไปยัง Class ลูกแล้วให้ Class ลูกกำหนดการทำงานของ
# Abstract Method ก่อนจึงสามารถสร้างเป็น Object ได้ การ
# กระท าดังกล่าวท าได้โดย Overriding Method
