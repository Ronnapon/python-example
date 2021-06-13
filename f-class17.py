# Duck Type
class TextBox:
    def draw(self):
        print("Textbox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()
    return ("Good Bye")


textbox = TextBox()
dropdown = DropDownList()
print(draw([textbox, dropdown]))
