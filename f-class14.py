# Good Example inheritance
class InvalidOperationEorr(Exception):
    pass


class Steam:
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


class FilesSteam(Steam):
    def read(self):
        print("Reading Data from File Steam")


class NetworkSteam(Steam):
    def read(self):
        print("Reading Data from Network Steam")


filesteam = FilesSteam()
print("Initial", filesteam.opened)
filesteam.open()
print("Open", filesteam.opened)
filesteam.read()
filesteam.close()
print("Close", filesteam.opened)
