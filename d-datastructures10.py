# Stack (Lifo)
page = []
page.append(1)
print(page)
page.append(2)
print(page)
page.append(3)
print(page)

# ------------->
page.pop()
print(page)
page.pop()
print(page)
page.pop()
print(page)
if not page:  # "", 0 , []
    print("disable")
else:
    print('redirect', page[-1])
