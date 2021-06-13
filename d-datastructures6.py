# Fiding Item
letters = ['a', 'b', 'c', 'c', 'd']
print(f"Finding C = {letters.index('c')}")
print(f"Count   C = {letters.count('c')}")

# You mush check before use "index for finding"
if 'd' in letters:
    print(letters.index('d'))

if letters.count('d') > 0:
    print(letters.index('d'))
