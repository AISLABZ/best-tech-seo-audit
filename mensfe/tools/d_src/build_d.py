import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from d_css import css, DARK, LIGHT
from d_common import I
import d_home, d_board, d_topic, d_article

BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "redesign"))
PAGES = {"home.html": d_home.html, "board.html": d_board.html, "topic.html": d_topic.html, "article.html": d_article.html}
THEMES = [("d", DARK, "dark"), ("d-light", LIGHT, "light")]

def switch(page, current):
    dark_href = page if current == "dark" else f"../d/{page}"
    light_href = page if current == "light" else f"../d-light/{page}"
    dc = ' aria-current="true"' if current == "dark" else ""
    lc = ' aria-current="true"' if current == "light" else ""
    return (f'<div class="theme" role="group" aria-label="Colour theme"><span>Theme:</span>'
            f'<a href="{dark_href}"{dc}>{I("moon", 15)}Dark</a><a href="{light_href}"{lc}>{I("sun", 15)}Light</a></div>')

for folder, theme, name in THEMES:
    os.makedirs(f"{BASE}/{folder}", exist_ok=True)
    for page, html in PAGES.items():
        out = html.replace("@@CSS@@", css(theme)).replace("@@THEME@@", switch(page, name))
        assert "@@" not in out
        with open(f"{BASE}/{folder}/{page}", "w") as f:
            f.write(out)
        print(folder, page, len(out))
