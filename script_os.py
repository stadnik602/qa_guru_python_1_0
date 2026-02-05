import os.path
import shutil

CURRENT_FILE = os.path.abspath(__file__)
# print(os.path.abspath("script_open"))
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
print(TMP_DIR)

if not os.path.exists("tmp2"):
    os.mkdir("tmp2")
    print("created tmp2")
else:
    print("tmp2 already exists")

shutil.rmtree(os.path.join(CURRENT_DIR, "tmp2")) #remove directory