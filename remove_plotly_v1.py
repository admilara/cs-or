"""Remove the redundant plotly-latest (v1.58.5) <script> tag from plot HTML files
that also load Plotly 2.x. Figures and data are not touched.

Usage (from the root of the cs-or repo):
    python remove_plotly_v1.py
"""
import pathlib
import re

TAG = re.compile(r'[ \t]*<script src="https://cdn\.plot\.ly/plotly-latest\.min\.js"></script>[ \t]*\r?\n?')
V2 = re.compile(r'plotly-2\.\d+\.\d+\.min\.js')

root = pathlib.Path(__file__).resolve().parent
edited = 0
for path in root.rglob("*.html"):
    if ".git" in path.parts or path.parts[-2:-1] == ("_layouts",):
        continue
    text = path.read_bytes().decode("utf-8")
    if "plotly-latest.min.js" in text and V2.search(text):
        new, n = TAG.subn("", text, count=1)
        if n == 1 and "plotly-latest" not in new:
            path.write_bytes(new.encode("utf-8"))
            edited += 1
        else:
            print("skipped (unexpected format):", path.relative_to(root))
print(f"edited {edited} files")
