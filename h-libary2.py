# Path Class
from pathlib import Path

# Path("C:\\Program File\\Microsoft")
# Path(r"C:\Program File\Microsoft")
# Path("/usr/local/ben")
# Path()
# Path("ecommerce/__init__.py")
# Path() / "ecommerce" / "__init__.py"
# print(Path.home())
path = Path("ecommerce/__init__.py")
print("exits     = ", path.exists())
print("is_file   = ", path.is_file())
print("is_dir    = ", path.is_dir())
print("path.name = ", path.name)
print("path.stem = ", path.stem)
print("path.suffix = ", path.suffix)
print("path.parent = ", path.parent)
path = path.with_name("file.txt")
print("path.absolute = ", path.absolute())
path = path.with_suffix(".py")
print("path.absolute = ", path.absolute())
