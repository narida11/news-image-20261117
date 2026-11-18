import os
from PIL import Image, ImageDraw, ImageFont

def draw_newspaper():
    width, height = 1024, 1024
    image = Image.new("RGB", (width, height), "#F7F3EE")
    draw = ImageDraw.Draw(image)

    # Fonts
    font_dir = "/data/data/com.termux/files/usr/share/fonts/TTF"
    font_serif_bold = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 14)
    font_serif = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif.ttf"), 11)
    font_serif_small = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif.ttf"), 9)
    font_masthead = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 42)
    font_date = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 15)
    font_headline = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 16)
    font_subheadline = ImageFont.truetype(os.path.join(font_dir, "DejaVuSerif-Bold.ttf"), 13)

    black = "#1A1A1A"
    red = "#C8102E"
    gray = "#E2DBD0"
    dark_gray = "#555555"

    # Outer border
    draw.rectangle([10, 10, width - 10, height - 10], outline=black, width=2)
    draw.rectangle([14, 14, width - 14, height - 14], outline=black, width=1)

    # --- MASTHEAD ---
    draw.text((width // 2, 25), "THE WORLD IN ONE DAY", fill=black, font=font_masthead, anchor="mm")
    
    # Sub-masthead info
    sub_info = "VOL. III NO. 322  •  THE INTERNATIONAL DAILY NEWSPAPER  •  MONDAY/TUESDAY EDITION"
    draw.text((width // 2, 58), sub_info, fill=dark_gray, font=font_serif_small, anchor="mm")

    # Date line box
    draw.line([25, 70, width - 25, 70], fill=black, width=2)
    draw.line([25, 73, width - 25, 73], fill=black, width=1)
    date_text = "TUESDAY, NOVEMBER 17, 2026"
    draw.text((width // 2, 85), date_text, fill=red, font=font_date, anchor="mm")
    draw.line([25, 98, width - 25, 98], fill=black, width=1)

    # --- TOP STORIES SECTION ---
    draw.line([615, 105, 615, 510], fill=gray, width=1)
    draw.line([25, 515, width - 25, 515], fill=black, width=2)

    # --- MAIN STORY: TANKER ABLAZE IN THE STRAIT OF HORMUZ ---
    mx, my = 35, 115
    draw.text((mx, my), "TANKER ABLAZE IN THE STRAIT OF HORMUZ", fill=black, font=font_headline)
    
    ix1, iy1, ix2, iy2 = mx, my + 24, mx + 565, my + 175
    draw.rectangle([ix1, iy1, ix2, iy2], fill="#EAE3D9", outline=black, width=1)
    draw.rectangle([ix1+5, iy1+80, ix2-5, iy2-5], fill="#B5C2C8") # water
    draw.polygon([(ix1+100, iy1+110), (ix1+450, iy1+110), (ix1+430, iy1+145), (ix1+120, iy1+145)], fill="#333333")
    draw.rectangle([ix1+180, iy1+75, ix2-180, iy1+110], fill="#888888") # superstructure
    draw.ellipse([ix1+220, iy1+50, ix1+280, iy1+90], fill=red)
    draw.ellipse([ix1+235, iy1+30, ix1+300, iy1+70], fill="#FF8C00")
    draw.arc([ix1+250, iy1+10, ix1+350, iy1+50], 180, 360, fill=dark_gray, width=3)
    draw.arc([ix1+310, iy1+5, ix1+410, iy1+40], 180, 360, fill=dark_gray, width=2)
    draw.polygon([(ix1+60, iy1+130), (ix1+100, iy1+130), (ix1+95, iy1+142), (ix1+65, iy1+142)], fill=red)
    draw.text(((ix1+ix2)//2, iy1+155), "[ ARTWORK: LPG TANKER TARA GAS ON FIRE IN STRAIT OF HORMUZ ]", fill=dark_gray, font=font_serif_small, anchor="mm")

    main_caption = (
        "LPG carrier Tara Gas hit twice and set on fire; crew evacuated as Iran claims "
        "naval mines in the world's oil chokepoint. Emergency response vessels deployed "
        "as shipping traffic halts across the vital Gulf corridor."
    )
    cury = iy2 + 12
    for line in wrap_text(main_caption, font_serif, 560, draw):
        draw.text((mx, cury), line, fill=black, font=font_serif)
        cury += 15

    # --- SECOND STORY: QUAD LEADERS MEET IN MANILA ---
    sx = 630
    draw.text((sx, my), "QUAD LEADERS MEET IN MANILA", fill=black, font=font_headline)
    
    qix1, qiy1, qix2, qiy2 = sx, my + 24, width - 35, my + 175
    draw.rectangle([qix1, qiy1, qix2, qiy2], fill="#EAE3D9", outline=black, width=1)
    draw.rectangle([qix1+40, qiy1+85, qix2-40, qiy2-15], fill="#555555") # table
    draw.ellipse([qix1+70, qiy1+50, qix1+110, qiy1+95], fill="#222222")
    draw.ellipse([qix1+140, qiy1+50, qix1+180, qiy1+95], fill="#222222")
    draw.ellipse([qix1+210, qiy1+50, qix1+250, qiy1+95], fill="#222222")
    draw.ellipse([qix1+280, qiy1+50, qix1+320, qiy1+95], fill="#222222")
    draw.rectangle([qix1+20, qiy1+25, qix1+70, qiy1+50], fill=red)
    draw.rectangle([qix2-70, qiy1+25, qix2-20, qiy1+50], fill="#003366")
    draw.text(((qix1+qix2)//2, qiy1+155), "[ ARTWORK: QUAD SUMMIT IN MANILA ]", fill=dark_gray, font=font_serif_small, anchor="mm")

    quad_caption = (
        "Trump joins the Quad summit as Washington says it takes Iran's 'dirty bomb' "
        "threat seriously. Leaders reaffirm security pact and regional maritime cooperation."
    )
    cury_q = qiy2 + 12
    for line in wrap_text(quad_caption, font_serif, 360, draw):
        draw.text((sx, cury_q), line, fill=black, font=font_serif)
        cury_q += 15

    # --- SMALL PANELS GRID ---
    panels = [
        ("CRIMEA BRIDGE HIT AGAIN", "Ukraine strikes the Kerch Bridge two days running; Russia answers by hitting a Kyiv bridge."),
        ("COP31 FIGHTS OVER FOSSIL FUELS", "Ministers in Antalya battle over a draft to phase out fossil fuels and a $120bn adaptation fund."),
        ("WALL STREET SLIDES, NVIDIA REPORTS", "Fourth straight down day; Nvidia posts its first results without founder Jensen Huang."),
        ("EBOLA SPREADS AT RECORD PACE", "Outbreak passes 11,000 cases and 5,500 deaths, the fastest growth on record."),
        ("STORMS BATTER CALIFORNIA & FLORIDA", "An atmospheric river floods California as Florida's St. Johns River overflows."),
        ("VOYAGER 1, ONE LIGHT-DAY AWAY", "NASA celebrates as its farthest spacecraft nears a full light-day from home."),
        ("PULISIC'S BICYCLE KICK", "USA beat Haiti 2-0 in Pochettino's farewell; Argentina hit seven, Brazil hit seven.")
    ]

    col_widths = 315
    col_xs = [25, 355, 685]
    row_ys = [525, 685, 845]

    for idx, (title, caption) in enumerate(panels):
        c = idx % 3
        r = idx // 3
        px = col_xs[c]
        py = row_ys[r]

        draw.rectangle([px, py, px + col_widths - 10, py + 150], outline=gray, width=1)
        draw.text((px + 8, py + 8), title, fill=black, font=font_subheadline)
        
        mv_x1, mv_y1, mv_x2, mv_y2 = px + 8, py + 28, px + col_widths - 18, py + 95
        draw.rectangle([mv_x1, mv_y1, mv_x2, mv_y2], fill="#EAE3D9", outline=gray, width=1)
        
        draw_mini_graphic(draw, idx, mv_x1, mv_y1, mv_x2, mv_y2)

        cap_y = mv_y2 + 6
        for line in wrap_text(caption, font_serif_small, col_widths - 26, draw):
            draw.text((px + 8, cap_y), line, fill=black, font=font_serif_small)
            cap_y += 12

    image.save("entry.png", "PNG")
    print("Successfully generated entry.png locally")

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def draw_mini_graphic(draw, idx, x1, y1, x2, y2):
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    if idx == 0:  # Crimea Bridge
        draw.line([x1+10, cy+10, x2-10, cy+10], fill="#333333", width=4)
        draw.rectangle([cx-15, cy-15, cx+15, cy+10], fill="#777777")
        draw.ellipse([cx-10, cy-25, cx+10, cy-5], fill="#C8102E")
    elif idx == 1:  # COP31 Fossil Fuels
        draw.ellipse([cx-25, cy-25, cx+25, cy+25], outline="#333333", width=2)
        draw.arc([cx-25, cy-25, cx+25, cy+25], 0, 180, fill="#C8102E", width=3)
    elif idx == 2:  # Wall Street / Nvidia
        draw.line([x1+15, y2-15, cx-5, cy], fill="#333333", width=2)
        draw.line([cx-5, cy, x2-15, y2-25], fill="#C8102E", width=3)
    elif idx == 3:  # Ebola
        draw.ellipse([cx-20, cy-20, cx+20, cy+20], outline="#C8102E", width=3)
        draw.line([cx-12, cy, cx+12, cy], fill="#C8102E", width=3)
        draw.line([cx, cy-12, cx, cy+12], fill="#C8102E", width=3)
    elif idx == 4:  # Storms
        draw.rectangle([x1+10, cy-5, x2-10, cy+15], fill="#888888")
        draw.line([cx-15, cy-15, cx-5, cy-5], fill="#C8102E", width=2)
        draw.line([cx+5, cy-15, cx+15, cy-5], fill="#C8102E", width=2)
    elif idx == 5:  # Voyager 1
        draw.ellipse([cx-15, cy-15, cx+15, cx+15], fill="#222222")
        draw.ellipse([x2-20, y1+15, x2-12, y1+23], fill="#C8102E")
        draw.line([cx, cy, x2-16, y1+19], fill="#555555", width=1)
    elif idx == 6:  # Pulisic bicycle kick
        draw.ellipse([cx-20, cy-10, cx-5, cy+5], fill="#333333")
        draw.ellipse([cx+5, cy-15, cx+15, cy-5], fill="#C8102E")

if __name__ == "__main__":
    draw_newspaper()
