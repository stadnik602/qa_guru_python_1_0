import os.path

from pypdf import PdfReader
from script_os import TMP_DIR

reader = PdfReader("tmp/Python Testing With Pytest(Brian-Okken).pdf")

print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())
assert "Simple, Rapid, Effective, and Scalable" in reader.pages[1]
assert os.path.getsize("tmp/Python Testing With Pytest(Brian-Okken).pdf") == 3081510