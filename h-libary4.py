# Work with File
from pathlib import Path
from time import ctime
import shutil

# with open("ecommerce/__init__.py") as file:
#    print("Hello")

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("__init__.txt")
# path.unlink()
# print(path.read_bytes())
print(path.stat())
print(ctime(path.stat().st_ctime))
print(ctime(path.stat().st_mtime))
print(path.read_text())
# path.write_text("aaaaa")  # Before write You have to open & read File


# Copy File
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"
print("source =", source)
print("target =", target)
# target.write_text(source.read_text())
shutil.copy(source, target)
