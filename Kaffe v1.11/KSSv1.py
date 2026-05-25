import sys
css = ""
with open(sys.argv[1]) as x:
    ls = x.readlines()
for l in ls:
    l = l.strip()
    # BODY #
    if l.startswith("text color = "):
        css += f"p{{color:{l[13:]};}}\n"
    elif l.startswith("background color = "):
        css += f"body{{background-color:{l[19:]};}}\n"
    elif l.startswith("font = "):
        css += f"body{{font-family:{l[7:]};}}\n"
    elif l.startswith("size = "):
        css += f"body{{font-size:{l[7:]};}}\n"
    elif l.startswith("align = "):
        css += f"body{{text-align:{l[8:]};}}\n"
    # TITLES #
    elif l.startswith("\\t text color = "):
        css += f"h1{{color:{l[16:]};}}\n"
    elif l.startswith("\\t size = "):
        css += f"h1{{font-size:{l[10:]};}}\n"
    elif l.startswith("\\t font = "):
        css += f"h1{{font-family:{l[10:]};}}\n"
    elif l.startswith("\\t align = "):
        css += f"h1{{text-align:{l[12:]};}}\n"
    # BUTTONS #
    elif l.startswith("\\b text color = "):
        css += f"button{{color:{l[16:]};}}\n"
    elif l.startswith("\\b background color = "):
        css += f"button{{background-color:{l[22:]};}}\n"
    elif l.startswith("\\b width = "):
        css += f"button{{width:{l[11:]};}}\n"
    elif l.startswith("\\b height = "):
        css += f"button{{height:{l[12:]};}}\n"
    elif l.startswith("\\b border = "):
        css += f"button{{border:{l[12:]};}}\n"
    elif l.startswith("\\b border radius = "):
        css += f"button{{border-radius:{l[19:]};}}\n"
    elif l.startswith("\\b padding = "):
        css += f"button{{padding:{l[13:]};}}\n"
with open(sys.argv[2], "w") as h:
    h.write(css)