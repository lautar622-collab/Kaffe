import sys
import os
html = ""
def formattext(text):
    parts = text.split("**")
    result = ""
    for i, part in enumerate(parts):
        if i % 2 == 1:
            result += f"<b>{part}</b>"
        else:
            result += part
    return result
with open(sys.argv[1]) as x:
    ls = x.readlines()
html = "<html>\n<head>\n"
for m in ls:
    m = m.strip()
    if m.startswith("\\m encoding "):
        html += f'<meta charset="{m[12:]}">\n'
    elif m.startswith("\\m title "):
        html += f'<title>{m[9:]}</title>\n'
    elif m.startswith("\\m favicon "):
        html += f'<link rel="icon" href="{m[11:]}">\n'
    elif m.startswith("\\ss "):
        stylefile = m[4:]
        if stylefile.endswith(".kss"):
            cssfile = stylefile[:-4] + ".css"
        else:
            cssfile = stylefile + ".css"
        ksscompiler = sys.argv[3]
        os.system(f'python "{ksscompiler}" "{stylefile}" "{cssfile}"')
        html += f'<link rel="stylesheet" href="{cssfile}">\n'
html += "</head>\n<body>\n"
for l in ls:
    l = l.strip()
    if l.startswith("\\t "):
        html += f"<h1>{formattext(l[3:])}</h1>\n"
        print("Title Compiled")
    elif l.startswith("\\b "):
        html += f"<button>{l[3:]}</button>\n"
        print("Button Compiled")
    elif l.startswith("\\i "):
        html += f"<img src='{l[3:]}'>\n"
        print("Image Compiled")
    elif l.startswith("\\l "):
        parts = l.split(" ", 2)
        if len(parts) >= 3:
            html += f"<a href='{parts[1]}'>{parts[2]}</a>\n"
            print("Link Compiled")
        else:
            print("Invalid Link")
    elif l.startswith("\\v "):
        html += f'<video controls><source src="{l[3:]}"></video>\n'
        print("Video Compiled")
    elif l.startswith("\\a "):
        html += f'<audio controls><source src="{l[3:]}"></audio>\n'
        print("Audio Compiled")
    elif l.startswith("\\m") or l.startswith("\\ss"): 
        pass
    elif l == "":
        pass
    else:
        html += f"<p>{formattext(l)}</p>\n"
html += "</body>\n</html>"
with open(sys.argv[2], "w") as h:
    h.write(html)
