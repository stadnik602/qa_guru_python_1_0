import string
from zipfile import ZipFile

with ZipFile("tmp/Lyrics.zip") as zip_file:
    print(zip_file.namelist())
    text = zip_file.read("Lurics.txt").decode("utf-8")
    print(text)
    zip_file.extract("Lurics.txt", path="tmp")
