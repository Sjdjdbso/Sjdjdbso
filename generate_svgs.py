import os

cream = "#F4EBD9"
black = "#000000"
yellow = "#FFC900"
blue = "#80C6FF"
pink = "#FF90E8"
green = "#23A094"
orange = "#FF7A00"

def rect(x, y, w, h, fill, stroke, rx=0, shadow=True, shadow_color=black, shadow_offset=8, stroke_width=4):
    out = ""
    if shadow:
        out += f'<rect x="{x+shadow_offset}" y="{y+shadow_offset}" width="{w}" height="{h}" rx="{rx}" fill="{shadow_color}" />\n'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />\n'
    return out

def text(x, y, content, size, weight="bold", color=black, anchor="start", font="Arial, sans-serif"):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{content}</text>\n'

if not os.path.exists('assets'):
    os.makedirs('assets')

# 1. Header (Navbar + Welcome)
header_svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="800" height="280" viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="{cream}" />
    <!-- Navbar Pill -->
    {rect(150, 30, 500, 60, "#FFFFFF", black, rx=30, shadow_offset=6)}
    {text(220, 68, "HOME", 18, color=black, anchor="middle")}
    <circle cx="280" cy="60" r="5" fill="{black}" />
    {text(340, 68, "ABOUT", 18, color=black, anchor="middle")}
    <circle cx="400" cy="60" r="5" fill="{black}" />
    {text(460, 68, "SKILLS", 18, color=black, anchor="middle")}
    <circle cx="520" cy="60" r="5" fill="{black}" />
    {text(580, 68, "STATS", 18, color=black, anchor="middle")}

    <!-- Welcome Card -->
    {rect(50, 130, 700, 120, yellow, black, rx=0, shadow_offset=10)}
    {text(400, 180, "Hi 👋, I'm Leonardo_", 36, anchor="middle", font="Courier New, monospace")}
    {text(400, 220, "A passionate bot developer from Indonesia 🇮🇩", 22, anchor="middle", weight="bold", font="Courier New, monospace")}
</svg>
"""
with open('assets/header.svg', 'w') as f:
    f.write(header_svg)

# 2. Tools (Colorful Cards)
tools_svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="800" height="220" viewBox="0 0 800 220" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="{cream}" />
    {text(400, 50, "🛠️ Tools &amp; Technologies", 32, anchor="middle", font="Courier New, monospace")}

    <!-- Python -->
    {rect(100, 90, 170, 80, blue, black, rx=0, shadow_offset=8)}
    {text(185, 140, "Python", 26, anchor="middle", color=black, font="Courier New, monospace")}

    <!-- Telegram -->
    {rect(315, 90, 170, 80, pink, black, rx=0, shadow_offset=8)}
    {text(400, 140, "Telegram", 26, anchor="middle", color=black, font="Courier New, monospace")}

    <!-- Linux -->
    {rect(530, 90, 170, 80, green, black, rx=0, shadow_offset=8)}
    {text(615, 140, "Linux", 26, anchor="middle", color=black, font="Courier New, monospace")}
</svg>
"""
with open('assets/tools.svg', 'w') as f:
    f.write(tools_svg)
