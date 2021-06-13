# Working with Directory
from pathlib import Path

path = Path("ecommerce")
path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# print(path.iterdir())
# for path in path.iterdir():
#     print(path)

paths1 = [p for p in path.iterdir() if p.is_dir()]  # Show Directory
print("path1 = ", paths1)

#paths2 = [p2 for p2 in path.glob("**/*.py")]
paths2 = [p2 for p2 in path.glob("*.py")]
print("path2 = ", paths2)

paths3 = [p3 for p3 in path.rglob("*.py")]  # .py File all Ecommerce directory
print("path3 = ", paths3)
