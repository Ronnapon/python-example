# Backup Old File and Copy New File instead of Old File
from pathlib import Path
from datetime import datetime
import shutil

now = datetime.now()
dt = now.strftime("%d%m%Y_%H%M%S")


def back(oldpath):
    source = Path(oldpath)  # Floder Original Source
    target = Path() / "Backup" / dt  # Floder Backup
    if not target.exists():
        target.mkdir()
    target = target / oldpath
    if source.is_dir():
        target.mkdir()
    elif source.is_file():
        shutil.copy(source, target)
        print("Back >>", source.name)


def copy(newpath, oldpath):
    source = Path(newpath)  # Floder Deploy
    target = Path(oldpath)  # Floder Original Source
    if source.is_dir():
        if not target.exists():
            target.mkdir()
    elif source.is_file():
        shutil.copy(source, target)
        print("Copy >>", source.name)


def read(path, typefile="ALL"):
    path_source = Path(path)
    path_source = [p3 for p3 in path_source.rglob("*")]
    for source in path_source:
        newpath = str(source)
        oldpath = str(source).replace(path + "\\", "")
        if typefile == "B":
            back(oldpath)
        elif typefile == "C":
            copy(newpath, oldpath)
        else:
            back(oldpath)
            copy(newpath, oldpath)

def zipfile(path):
    print("test")

print("*" * 30)
read("Deploy", "B")
print("*" * 30)
read("Deploy", "C")
print("*" * 30)
print("-- complete --")
