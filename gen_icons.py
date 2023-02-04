import glob, re
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


# files = glob.glob("devicon/icons/**/*-original.svg")

# def get_lang_name1(path: str) -> str:
#     res = re.match(r"devicon/icons/([^/]*)/.*-original.svg", path)
#     return res.group(1)

# for path in files:
#     drawing = svg2rlg(path)
#     renderPM.drawToFile(drawing, "images/icons/" + get_lang_name1(path) + ".png", fmt="PNG")

files = glob.glob("skill-icons/icons/*.svg")

def get_lang_name2(path: str) -> str:
    res = re.match(r"skill-icons/icons/([^/]*).svg", path)
    return res.group(1)

for path in files:
    drawing = svg2rlg(path)
    renderPM.drawToFile(drawing, "images/icons/" + get_lang_name2(path) + ".png", fmt="PNG")