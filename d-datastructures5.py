# Add & Remove List
letters = []
letters = ['a', 'b', 'c', 'A']

# Add---------------->
# End of List
letters.append('d')
print(f"Append Method={letters}")

# Index
letters.insert(0, 'A')
print(f"insert Method={letters}")

# Remove------------->
# End of List  & can input index to remove
letters.pop()
print(f"pop Method={letters}")

# Don't know index
letters.remove('A')
print(f"remove Method={letters}")

# Remove mutiple
del letters[0:1]
print(f"del={letters}")

# Remove all
letters.clear()
print(letters)
