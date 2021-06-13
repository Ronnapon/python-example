from pathlib import Path
from zipfile import ZipFile

# with ZipFile("zip1.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)
#     zip.close

with ZipFile("zip1.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/Sale2.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("Extract")
