#!/usr/bin/env python3
"""Procedural pixel-art car interior kit for The Outskirts (640x360, 32 colours).
Run: python3 make_kit.py   -> writes PNG layers + previews next to this file."""
import math, os, random
from PIL import Image, ImageDraw, ImageChops

W, H = 640, 360
OUT = os.path.dirname(os.path.abspath(__file__))

PAL = {
    'ink': (12, 10, 8), 'brown0': (30, 23, 18), 'brown1': (51, 40, 30), 'brown2': (74, 58, 43),
    'brown3': (107, 85, 64), 'brown4': (140, 114, 86),
    'cream0': (168, 148, 112), 'cream1': (201, 181, 142), 'cream2': (227, 211, 175),
    'grey0': (37, 38, 42), 'grey1': (60, 62, 66), 'grey2': (89, 92, 96), 'grey3': (127, 130, 135), 'grey4': (166, 168, 170),
    'olive0': (47, 51, 32), 'olive1': (74, 80, 48), 'olive2': (107, 114, 69),
    'red0': (90, 28, 22), 'red1': (140, 42, 32), 'red2': (176, 64, 44),
    'amber0': (138, 90, 20), 'amber1': (217, 140, 34), 'amber2': (245, 192, 74),
    'green0': (29, 74, 38), 'green1': (95, 207, 106),
    'wood0': (79, 46, 22), 'wood1': (122, 74, 34), 'rust': (110, 63, 34),
    'steel0': (92, 102, 112), 'steel1': (138, 148, 156), 'glass': (216, 226, 232), 'blue': (90, 168, 255),
}
assert len(PAL) == 32

# ---------------------------------------------------------------- geometry
WS = [(118, 38), (528, 38), (586, 182), (62, 182)]            # windscreen
WL = [(0, 80), (88, 58), (40, 176), (0, 176)]                  # left side window
mx = lambda pts: [(639 - x, y) for x, y in pts]
WR = mx(WL)
PILLAR_L = [(96, 36), (122, 36), (64, 186), (36, 186)]
PILLAR_R = mx(PILLAR_L)
WHEEL = (245, 268, 68, 40)   # cx, cy, rx, ry   (pivot = 245,268)
CLUSTER = (184, 192, 306, 232)
SPEEDO = (232, 214, 13); FUEL = (280, 214, 8)
LAMPS = {'engine': (203, 197, 211, 202), 'highbeam': (246, 197, 254, 202), 'fuel': (290, 197, 298, 202)}
RADIO_DISP = (330, 218, 366, 226)
GLOVE = (420, 216, 500, 248)

# ---------------------------------------------------------------- helpers
CHECK = [Image.new('L', (W, H), 0) for _ in range(2)]
for ph in range(2):
    px = CHECK[ph].load()
    for y in range(H):
        for x in range(y % 2 ^ ph, W, 2):
            px[x, y] = 255

def new(): return Image.new('RGBA', (W, H), (0, 0, 0, 0))
def ip(pts): return [(int(round(x)), int(round(y))) for x, y in pts]
def mask_poly(pts, erase_pts=None):
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m); d.polygon(ip(pts), fill=255)
    if erase_pts: d.polygon(ip(erase_pts), fill=0)
    return m
def poly(img, pts, c, a=255): img.paste(PAL[c] + (a,), mask=mask_poly(pts))
def rect(img, box, c, a=255): poly(img, [(box[0], box[1]), (box[2], box[1]), (box[2], box[3]), (box[0], box[3])], c, a)
def ell_pts(cx, cy, rx, ry, a0=0, a1=360, n=48):
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy - ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
def ellipse(img, cx, cy, rx, ry, c, a=255): poly(img, ell_pts(cx, cy, rx, ry), c, a)
def dither(img, pts, c, ph=0, a=255):
    img.paste(PAL[c] + (a,), mask=ImageChops.multiply(mask_poly(pts), CHECK[ph]))
def line(img, pts, c, w=1, a=255):
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).line(ip(pts), fill=255, width=w, joint='curve')
    img.paste(PAL[c] + (a,), mask=m)
def erase(img, pts): img.paste((0, 0, 0, 0), mask=mask_poly(pts))
def clip(img, pts):
    r, g, b, a = img.split(); img.putalpha(ImageChops.multiply(a, mask_poly(pts)))
def band(pts, w):  # thick line as polygon between two points
    (x0, y0), (x1, y1) = pts; dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L * w / 2, dx / L * w / 2
    return [(x0 + nx, y0 + ny), (x1 + nx, y1 + ny), (x1 - nx, y1 - ny), (x0 - nx, y0 - ny)]

# ---------------------------------------------------------------- interior frame
def interior_frame():
    im = new()
    rect(im, (0, 0, W, H), 'grey0')
    # roof / headliner, kept flat for the top-centre readout
    rect(im, (0, 0, W, 30), 'grey1'); dither(im, [(0, 20), (W, 20), (W, 30), (0, 30)], 'grey0')
    rect(im, (0, 30, W, 38), 'grey0')
    # door frames above side windows
    poly(im, [(0, 30), (120, 30), (96, 36), (88, 58), (0, 80)], 'grey1')
    poly(im, mx([(0, 30), (120, 30), (96, 36), (88, 58), (0, 80)]), 'grey1')
    # door tops + panels
    for side in (0, 1):
        f = (lambda p: p) if side == 0 else mx
        poly(im, f([(0, 172), (44, 172), (66, 186), (70, 200), (0, 200)]), 'brown3')
        poly(im, f([(0, 196), (70, 196), (70, 200), (0, 200)]), 'brown2')
        poly(im, f([(0, 200), (70, 200), (64, 262), (0, 262)]), 'brown2')
        dither(im, f([(0, 230), (68, 230), (64, 262), (0, 262)]), 'brown1')
        poly(im, f([(0, 172), (44, 172), (44, 176), (0, 176)]), 'brown4')
        rect(im, (14, 164, 18, 178) if side == 0 else (621, 164, 625, 178), 'ink')   # lock pin
        rect(im, (15, 165, 17, 177) if side == 0 else (622, 165, 624, 177), 'grey3')
        cx = 24 if side == 0 else 615                                                  # window crank
        ellipse(im, cx, 214, 5, 4, 'ink'); ellipse(im, cx, 214, 3, 2, 'grey2')
        line(im, [(cx, 214), (cx + (14 if side == 0 else -14), 222)], 'grey3', 2)
        ellipse(im, cx + (14 if side == 0 else -14), 222, 3, 3, 'grey3')
    # dashboard top (faded, cracked)
    poly(im, [(62, 182), (586, 182), (604, 206), (44, 206)], 'cream0')
    dither(im, [(62, 182), (586, 182), (590, 190), (58, 190)], 'brown4')
    dither(im, [(80, 198), (560, 198), (604, 206), (44, 206)], 'cream1', 1)
    for crack in ([(90, 186), (120, 192), (128, 203)], [(540, 184), (520, 194), (525, 204)], [(352, 190), (370, 196)], [(160, 200), (175, 204)]):
        line(im, crack, 'brown2'); line(im, [(x + 1, y) for x, y in crack], 'brown3')
    dither(im, [(372, 186), (400, 184), (412, 198), (380, 202)], 'brown3')             # stain
    dither(im, [(150, 190), (200, 188), (195, 198), (160, 200)], 'cream2', 1)          # dust
    # dash face + wood strip
    rect(im, (40, 206, 604, 252), 'grey1')
    rect(im, (40, 206, 604, 213), 'wood1'); rect(im, (40, 212, 604, 214), 'wood0')
    dither(im, [(40, 207), (604, 207), (604, 210), (40, 210)], 'wood0', 1)
    rect(im, (40, 246, 604, 252), 'grey0')
    dither(im, [(40, 236), (604, 236), (604, 246), (40, 246)], 'grey0')
    # cluster binnacle + face
    poly(im, [(176, 174), (314, 174), (322, 194), (168, 194)], 'grey0')
    poly(im, [(176, 174), (314, 174), (312, 178), (178, 178)], 'grey2')
    rect(im, (178, 188, 312, 236), 'grey1'); rect(im, CLUSTER, 'grey0'); dither(im, [(184, 192), (306, 192), (306, 232), (184, 232)], 'ink', 1)
    for cx, cy, r in (SPEEDO, FUEL): ellipse(im, cx, cy, r + 2, r + 2, 'grey1'); ellipse(im, cx, cy, r, r, 'ink')
    for box in LAMPS.values(): rect(im, box, 'grey1')
    # steering column + gear stalk (under the wheel)
    poly(im, [(232, 232), (258, 232), (264, 270), (226, 270)], 'grey0')
    poly(im, [(232, 232), (240, 232), (236, 270), (226, 270)], 'grey1')
    line(im, [(258, 246), (296, 256)], 'grey2', 3); ellipse(im, 298, 257, 3, 3, 'grey3')
    # vents
    for cx in (304, 406):
        ellipse(im, cx, 224, 10, 10, 'grey0'); ellipse(im, cx, 224, 8, 8, 'ink')
        for dy in (-4, 0, 4): line(im, [(cx - 6, 224 + dy), (cx + 6, 224 + dy)], 'grey2')
    # centre stack: cassette radio, heater sliders
    rect(im, (318, 206, 392, 252), 'grey0')
    rect(im, (324, 214, 386, 231), 'grey1'); rect(im, RADIO_DISP, 'green0')
    rect(im, (330, 227, 352, 230), 'ink'); ellipse(im, 377, 222, 4, 4, 'grey3'); ellipse(im, 377, 222, 1, 1, 'ink')
    for y in (236, 241, 246):
        rect(im, (326, y, 384, y + 2), 'ink')
    for x, y in ((340, 236), (356, 241), (332, 246)): rect(im, (x, y - 1, x + 5, y + 4), 'grey3')
    # glovebox (closed)
    rect(im, GLOVE, 'grey2'); rect(im, (GLOVE[0] + 1, GLOVE[1] + 1, GLOVE[2] - 1, GLOVE[3] - 1), 'grey1')
    rect(im, (455, 219, 467, 223), 'grey3'); rect(im, (455, 223, 467, 224), 'ink')
    # map + paper cup on the dash top
    poly(im, [(440, 184), (520, 186), (516, 204), (436, 202)], 'cream2')
    poly(im, [(466, 185), (494, 185), (492, 203), (464, 203)], 'cream1')
    for y in (190, 196): line(im, [(444, y), (514, y)], 'olive1')
    line(im, [(452, 186), (458, 202)], 'red1'); line(im, [(500, 186), (506, 202)], 'olive0')
    poly(im, [(396, 170), (412, 170), (410, 204), (398, 204)], 'cream1')
    poly(im, [(406, 170), (412, 170), (410, 204), (405, 204)], 'cream0')
    rect(im, (395, 168, 413, 172), 'grey3'); rect(im, (395, 172, 413, 173), 'grey1')
    # seats (bench) + headrests
    rect(im, (0, 252, W, H), 'brown2'); rect(im, (0, 252, W, 258), 'brown3')
    dither(im, [(0, 300), (W, 300), (W, H), (0, H)], 'brown1')
    for x in (60, 220, 360, 600): line(im, [(x, 258), (x, H)], 'brown1')
    rect(im, (70, 150, 205, 252), 'brown2'); dither(im, [(70, 150), (205, 150), (205, 252), (70, 252)], 'brown1', 1)
    rect(im, (100, 92, 172, 156), 'brown2'); rect(im, (100, 92, 172, 97), 'brown3'); rect(im, (126, 156, 130, 170), 'grey2'); rect(im, (142, 156, 146, 170), 'grey2')
    rect(im, (505, 240, 575, 276), 'brown2'); rect(im, (505, 240, 575, 245), 'brown3'); dither(im, [(505, 260), (575, 260), (575, 276), (505, 276)], 'brown1')
    # clutter on passenger seat: jacket, empty can
    poly(im, [(378, 290), (420, 278), (470, 286), (478, 312), (450, 332), (400, 334), (374, 316)], 'olive1')
    dither(im, [(378, 290), (420, 278), (430, 300), (390, 310)], 'olive2', 1)
    poly(im, [(430, 300), (470, 286), (478, 312), (450, 332), (436, 322)], 'olive0')
    line(im, [(400, 296), (440, 318)], 'olive0'); line(im, [(414, 284), (436, 300)], 'olive2')
    rect(im, (470, 300, 486, 320), 'grey3'); rect(im, (480, 300, 486, 320), 'grey2'); rect(im, (470, 306, 486, 312), 'red1')
    ellipse(im, 478, 300, 8, 3, 'grey4'); ellipse(im, 478, 300, 5, 2, 'ink')
    # windows out, then the things that sit in front of the glass
    for w in (WS, WL, WR): erase(im, w)
    for p in (PILLAR_L, PILLAR_R):
        poly(im, p, 'grey1'); poly(im, [p[0], p[1], ((p[1][0] + p[2][0]) / 2, (p[1][1] + p[2][1]) / 2), ((p[0][0] + p[3][0]) / 2, (p[0][1] + p[3][1]) / 2)], 'grey2')
        dither(im, p, 'grey0', 1)
    poly(im, [(176, 174), (314, 174), (322, 194), (168, 194)], 'grey0'); poly(im, [(176, 174), (314, 174), (312, 178), (178, 178)], 'grey2')
    poly(im, [(396, 170), (412, 170), (410, 182), (398, 182)], 'cream1'); poly(im, [(406, 170), (412, 170), (410, 182), (405, 182)], 'cream0')
    rect(im, (395, 168, 413, 172), 'grey3'); rect(im, (395, 172, 413, 173), 'grey1')
    # sun visors
    poly(im, [(122, 38), (232, 38), (228, 56), (128, 58)], 'cream0'); poly(im, [(128, 54), (228, 52), (228, 56), (128, 58)], 'brown4')
    poly(im, [(408, 38), (524, 38), (518, 58), (412, 56)], 'cream0'); poly(im, [(412, 52), (518, 54), (518, 58), (412, 56)], 'brown4')
    # rear-view mirror + hanging tag
    rect(im, (328, 36, 334, 46), 'grey0'); rect(im, (290, 44, 372, 68), 'grey0'); rect(im, (293, 47, 369, 65), 'grey2'); dither(im, [(293, 47), (369, 47), (369, 65), (293, 65)], 'grey3')
    line(im, [(322, 68), (322, 78)], 'grey3'); rect(im, (316, 78, 328, 94), 'cream1'); rect(im, (316, 90, 328, 94), 'cream0'); rect(im, (321, 80, 323, 82), 'ink')
    return im

# ---------------------------------------------------------------- wheel + driver
def wheel(rot=0):
    im = new(); cx, cy, rx, ry = WHEEL
    ellipse(im, cx, cy, rx, ry, 'grey2'); ellipse(im, cx + 2, cy + 3, rx, ry, 'grey1')
    dither(im, ell_pts(cx + 1, cy + 2, rx, ry), 'grey0', 1)
    erase(im, ell_pts(cx, cy, rx - 8, ry - 7))
    for a in (150 + rot, 30 + rot, 270 + rot):
        p = (cx + (rx - 6) * math.cos(math.radians(a)), cy - (ry - 5) * math.sin(math.radians(a)))
        poly(im, band([(cx, cy), p], 9), 'grey1'); poly(im, band([(cx, cy), p], 3), 'grey2')
    ellipse(im, cx, cy, 18, 12, 'grey0'); ellipse(im, cx, cy, 14, 9, 'grey1'); ellipse(im, cx - 2, cy - 2, 7, 4, 'grey2')
    return im

def plaid(im, pts):
    poly(im, pts, 'red1'); m = mask_poly(pts)
    pat = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(pat)
    for x in range(0, W, 10): d.rectangle((x, 0, x + 3, H), fill=PAL['red0'] + (255,))
    for y in range(0, H, 10): d.rectangle((0, y, W, y + 3), fill=PAL['brown1'] + (255,))
    for x in range(0, W, 10):
        for y in range(0, H, 10): d.rectangle((x, y, x + 3, y + 3), fill=PAL['ink'] + (255,))
    for x in range(5, W, 10): d.line((x + 2, 0, x + 2, H), fill=PAL['red2'] + (255,))
    pat.putalpha(ImageChops.multiply(pat.split()[3], m)); im.alpha_composite(pat)

def hand_pos(a):
    cx, cy, rx, ry = WHEEL
    return (cx + rx * math.cos(math.radians(a)), cy - ry * math.sin(math.radians(a)))

def driver(rot=None):
    """rot None = body + arms only (wheel separate). rot given = body + arms + wheel turned by rot degrees."""
    im = new()
    if rot is not None: im.alpha_composite(wheel(rot))
    rot = rot or 0
    # torso
    body = [(76, 198), (84, 188), (102, 182), (170, 182), (190, 188), (198, 198), (206, 360), (66, 360)]
    plaid(im, body); dither(im, [(66, 300), (206, 300), (206, 360), (66, 360)], 'ink'); dither(im, [(76, 194), (96, 182), (104, 360), (66, 360)], 'ink', 1)
    # neck, head, hair
    rect(im, (124, 136, 148, 186), 'brown4'); rect(im, (124, 136, 131, 186), 'brown3'); dither(im, [(124, 150), (148, 150), (148, 186), (124, 186)], 'brown3', 1)
    ellipse(im, 136, 118, 31, 36, 'brown4'); poly(im, [(106, 120), (114, 154), (158, 154), (166, 120)], 'brown3')
    ellipse(im, 136, 110, 33, 35, 'brown1')
    poly(im, [(104, 112), (106, 140), (114, 147), (122, 142), (130, 150), (138, 145), (146, 151), (154, 144), (162, 147), (167, 136), (168, 112)], 'brown1')
    poly(im, [(118, 80), (150, 78), (166, 96), (168, 118), (160, 122), (156, 100), (140, 90), (122, 92)], 'brown2')
    dither(im, ell_pts(146, 100, 18, 16), 'brown3', 1); dither(im, [(104, 112), (106, 140), (120, 146), (114, 100)], 'ink')
    for y in (126, 134): line(im, [(112, y), (160, y + 2)], 'brown0')
    ellipse(im, 105, 124, 4, 6, 'brown3'); ellipse(im, 167, 124, 4, 6, 'brown4')
    # arms: upper (plaid) + rolled-sleeve forearm (skin) + hand on the rim
    for side, a in (('L', 150 + rot), ('R', 30 + rot)):
        hd = hand_pos(a)
        sh, el = ((88, 190), (146, 236)) if side == 'L' else ((184, 188), (228, 228))
        plaid(im, band([sh, el], 24)); ellipse(im, el[0], el[1], 12, 10, 'red0')
        poly(im, band([el, hd], 18), 'brown4'); dither(im, band([el, hd], 18), 'brown3', 1)
        poly(im, band([el, ((el[0] + hd[0]) / 2, (el[1] + hd[1]) / 2)], 20), 'red1')
        dither(im, band([el, ((el[0] + hd[0]) / 2, (el[1] + hd[1]) / 2)], 20), 'red0')
        ellipse(im, hd[0], hd[1], 12, 9, 'brown4'); ellipse(im, hd[0] + 1, hd[1] + 3, 10, 5, 'brown3')
        for i in range(3): line(im, [(hd[0] - 8 + i * 6, hd[1] + 2), (hd[0] - 8 + i * 6, hd[1] + 7)], 'brown2')
    return im

# ---------------------------------------------------------------- dash lights
def dash_lights():
    im = new()
    for cx, cy, r in (SPEEDO, FUEL):
        ellipse(im, cx, cy, r, r, 'amber0'); dither(im, ell_pts(cx, cy, r, r), 'ink', 1)
        n = 9 if r > 10 else 5
        for i in range(n):
            a = 200 - 220 * i / (n - 1)
            line(im, [(cx + (r - 4) * math.cos(math.radians(a)), cy - (r - 4) * math.sin(math.radians(a))), (cx + (r - 1) * math.cos(math.radians(a)), cy - (r - 1) * math.sin(math.radians(a)))], 'amber1')
        a = 120 if r > 10 else 160
        line(im, [(cx, cy), (cx + (r - 2) * math.cos(math.radians(a)), cy - (r - 2) * math.sin(math.radians(a)))], 'amber2', 2)
        ellipse(im, cx, cy, 2, 2, 'ink')
    rect(im, RADIO_DISP, 'green0')
    for x in (333, 340, 347, 356): rect(im, (x, 220, x + 4, 224), 'green1')
    rect(im, (336, 221, 337, 223), 'green0'); rect(im, (343, 221, 344, 223), 'green0')
    return im

def lamp(name):
    im = new(); x0, y0, x1, y1 = LAMPS[name]
    c = {'engine': 'amber1', 'highbeam': 'blue', 'fuel': 'amber2'}[name]
    rect(im, (x0, y0, x1, y1), c); rect(im, (x0 + 2, y0 + 1, x1 - 2, y1 - 1), 'ink' if name != 'highbeam' else 'blue')
    if name == 'highbeam': rect(im, (x0 + 1, y0 + 2, x1 - 1, y1 - 2), 'ink'); rect(im, (x0 + 3, y0 + 1, x0 + 5, y1 - 1), 'blue')
    return im

def night_tint():
    im = new(); rect(im, (0, 0, W, H), 'ink', 150)
    dither(im, [(0, 252), (W, 252), (W, H), (0, H)], 'ink', 1, 200)
    for w in (WS, WL, WR): erase(im, w)
    halo = [(CLUSTER[0] - 8, CLUSTER[1] - 6), (CLUSTER[2] + 8, CLUSTER[1] - 6), (CLUSTER[2] + 8, CLUSTER[3] + 6), (CLUSTER[0] - 8, CLUSTER[3] + 6)]
    im.paste((0, 0, 0, 0), mask=ImageChops.multiply(mask_poly(halo), CHECK[0]))
    im.paste((0, 0, 0, 0), mask=ImageChops.multiply(mask_poly([(324, 214), (386, 214), (386, 231), (324, 231)]), CHECK[1]))
    erase(im, [(CLUSTER[0], CLUSTER[1]), (CLUSTER[2], CLUSTER[1]), (CLUSTER[2], CLUSTER[3]), (CLUSTER[0], CLUSTER[3])])
    rect(im, CLUSTER, 'ink', 90)
    for cx, cy, r in (SPEEDO, FUEL): erase(im, ell_pts(cx, cy, r, r))
    erase(im, [(RADIO_DISP[0], RADIO_DISP[1]), (RADIO_DISP[2], RADIO_DISP[1]), (RADIO_DISP[2], RADIO_DISP[3]), (RADIO_DISP[0], RADIO_DISP[3])])
    for b in LAMPS.values(): erase(im, [(b[0], b[1]), (b[2], b[1]), (b[2], b[3]), (b[0], b[3])])
    return im

def glovebox_open():
    im = new(); x0, y0, x1, y1 = GLOVE
    rect(im, (x0, y0, x1, y1), 'ink'); rect(im, (x0 + 2, y1 - 8, x1 - 2, y1), 'grey0')
    rect(im, (x0 + 10, y1 - 12, x0 + 34, y1 - 6), 'cream1'); rect(im, (x0 + 40, y1 - 10, x0 + 62, y1 - 5), 'grey3'); rect(im, (x0 + 58, y1 - 11, x0 + 64, y1 - 4), 'grey2')
    poly(im, [(x0 - 2, y1), (x1 + 2, y1), (x1 + 8, y1 + 42), (x0 - 8, y1 + 42)], 'grey1')
    poly(im, [(x0 - 2, y1), (x1 + 2, y1), (x1 + 3, y1 + 6), (x0 - 3, y1 + 6)], 'grey0')
    dither(im, [(x0 - 5, y1 + 20), (x1 + 5, y1 + 20), (x1 + 8, y1 + 42), (x0 - 8, y1 + 42)], 'grey2', 1)
    rect(im, (x0 + 34, y1 + 32, x0 + 46, y1 + 36), 'grey3')
    return im

# ---------------------------------------------------------------- glass damage
def win_center(w): return (sum(x for x, _ in w) / len(w), sum(y for _, y in w) / len(w))

def chips(w, seed, im=None):
    im = im or new(); rnd = random.Random(seed); cx, cy = win_center(w); sx = max(x for x, _ in w) - min(x for x, _ in w)
    for _ in range(3):
        x, y = cx + rnd.uniform(-0.3, 0.3) * sx, cy + rnd.uniform(-30, 30)
        for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2), (3, 2), (-3, -1)): line(im, [(x, y), (x + dx * rnd.randint(1, 2), y + dy * rnd.randint(1, 2))], 'glass', 1, 220)
        rect(im, (x, y, x + 1, y + 1), 'ink')
    clip(im, w); return im

def cracks(im, p, rnd, size, a=230):
    for k in range(8):
        a0 = k * 45 + rnd.uniform(-15, 15); L = size * rnd.uniform(0.5, 1.0); mid = L * rnd.uniform(0.3, 0.6); bend = rnd.uniform(-12, 12)
        m = (p[0] + mid * math.cos(math.radians(a0)), p[1] - mid * math.sin(math.radians(a0)))
        e = (p[0] + L * math.cos(math.radians(a0 + bend)), p[1] - L * math.sin(math.radians(a0 + bend)))
        line(im, [(x + 1, y + 1) for x, y in (p, m, e)], 'grey2', 1, 160); line(im, [p, m, e], 'glass', 1, a)
    for r in (size * 0.2, size * 0.45):
        ring = [(p[0] + r * rnd.uniform(0.7, 1.2) * math.cos(math.radians(t)), p[1] - r * rnd.uniform(0.7, 1.2) * math.sin(math.radians(t))) for t in range(0, 360, 30)]
        line(im, ring + ring[:1], 'glass', 1, 200)

def cracked(w, seed):
    im = new(); rnd = random.Random(seed); cx, cy = win_center(w); sx = max(x for x, _ in w) - min(x for x, _ in w)
    cracks(im, (cx + rnd.uniform(-0.2, 0.25) * sx, cy + rnd.uniform(-20, 20)), rnd, sx * 0.3)
    chips(w, seed + 1, im); clip(im, w); return im

def broken(w, seed):
    im = new(); rnd = random.Random(seed); cx, cy = win_center(w)
    rect(im, (0, 0, W, H), 'glass', 150); dither(im, [(0, 0), (W, 0), (W, H), (0, H)], 'glass', 1, 255)
    hole = [(cx + (x - cx) * rnd.uniform(0.55, 0.92), cy + (y - cy) * rnd.uniform(0.5, 0.9)) for x, y in sum(([(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t) for t in (0, 0.33, 0.66)] for a, b in zip(w, w[1:] + w[:1])), [])]
    for k in range(3): cracks(im, (cx + rnd.uniform(-0.4, 0.4) * (max(x for x, _ in w) - min(x for x, _ in w)), cy + rnd.uniform(-40, 40)), rnd, 60, 255)
    erase(im, hole); line(im, hole + hole[:1], 'ink', 1); line(im, [(x - 1, y - 1) for x, y in hole + hole[:1]], 'glass', 1)
    clip(im, w); return im

# ---------------------------------------------------------------- mods
def bar(im, a, b):
    poly(im, band([a, b], 6), 'ink'); poly(im, band([a, b], 4), 'steel0')
    (x0, y0), (x1, y1) = a, b; off = (-1, 0) if abs(x1 - x0) < abs(y1 - y0) else (0, -1)
    line(im, [(x0 + off[0], y0 + off[1]), (x1 + off[0], y1 + off[1])], 'steel1')

def mod_bars():
    im = new()
    for w, vx, hy in ((WS, (190, 320, 450), (85, 135)), (WL, (28, 56), (118,)), (WR, (583, 611), (118,))):
        xs = [x for x, _ in w]; ys = [y for _, y in w]
        for x in vx: bar(im, (x, min(ys) - 4), (x, max(ys) + 4))
        for y in hy: bar(im, (min(xs) - 4, y), (max(xs) + 4, y))
        for x in vx:
            for y in hy: ellipse(im, x, y, 4, 3, 'rust'); rect(im, (x - 1, y - 1, x + 1, y), 'steel1')
        edge = w + w[:1]
        for a, b in zip(edge, edge[1:]): bar(im, a, b)
        clip_m = mask_poly(w); r, g, b_, al = im.split()
    clip(im, [(0, 0), (W, 0), (W, H), (0, H)])
    m = ImageChops.add(ImageChops.add(mask_poly(WS), mask_poly(WL)), mask_poly(WR)); im.putalpha(ImageChops.multiply(im.split()[3], m))
    return im

def mod_plow():
    im = new()
    poly(im, [(62, 154), (170, 146), (470, 146), (586, 154), (586, 182), (62, 182)], 'rust')
    dither(im, [(62, 166), (586, 166), (586, 182), (62, 182)], 'brown1', 1)
    poly(im, [(62, 154), (170, 146), (470, 146), (586, 154), (586, 158), (470, 150), (170, 150), (62, 158)], 'steel0')
    line(im, [(62, 154), (170, 146), (470, 146), (586, 154)], 'steel1')
    for x in range(90, 580, 40): rect(im, (x, 160, x + 3, 163), 'ink'); rect(im, (x, 160, x + 1, 161), 'steel1')
    for x in (150, 488): rect(im, (x, 118, x + 10, 150), 'steel0'); rect(im, (x + 8, 118, x + 10, 150), 'ink'); rect(im, (x, 118, x + 2, 150), 'steel1')
    rect(im, (150, 118, 498, 124), 'steel0'); rect(im, (150, 123, 498, 124), 'ink')
    clip(im, WS); return im

# ---------------------------------------------------------------- road scene (preview only)
def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))
def scene(mode):
    im = Image.new('RGB', (W, H)); d = ImageDraw.Draw(im)
    sky, fog, ground, road = {
        'dusk': ((70, 60, 78), (150, 132, 126), (58, 62, 40), (78, 80, 84)),
        'night': ((8, 8, 12), (22, 22, 28), (14, 16, 10), (24, 25, 28)),
        'day': ((168, 176, 184), (206, 208, 204), (84, 92, 58), (112, 114, 118)),
    }[mode]
    HZ = 118
    for i in range(6): d.rectangle((0, i * HZ / 6, W, (i + 1) * HZ / 6), fill=lerp(sky, fog, i / 5))
    for i in range(10):
        t = i / 9; y0, y1 = HZ + (H - HZ) * (i / 10) ** 1.6, HZ + (H - HZ) * ((i + 1) / 10) ** 1.6
        d.rectangle((0, y0, W, y1), fill=lerp(fog, ground, t))
        d.polygon([(312 - 432 * (y0 - HZ) / (H - HZ), y0), (328 + 432 * (y0 - HZ) / (H - HZ), y0), (328 + 432 * (y1 - HZ) / (H - HZ), y1), (312 - 432 * (y1 - HZ) / (H - HZ), y1)], fill=lerp(fog, road, t))
    edge = lerp(fog, (200, 190, 150), 0.6) if mode != 'night' else (60, 58, 44)
    d.line((312, HZ, -120, H), fill=edge, width=2); d.line((328, HZ, 760, H), fill=edge, width=2)
    for i in range(12):
        s0, s1 = (i / 12) ** 2.2, (i / 12 + 0.04) ** 2.2
        d.polygon([(320 - 3 * s0, HZ + (H - HZ) * s0), (320 + 3 * s0, HZ + (H - HZ) * s0), (320 + 5 * s1, HZ + (H - HZ) * s1), (320 - 5 * s1, HZ + (H - HZ) * s1)], fill=lerp(fog, (170, 130, 40) if mode != 'night' else (70, 56, 20), s0 ** 0.5))
    for i in range(8, 0, -1):
        s = (i / 8) ** 2.2; bx, by = 312 - 470 * s, HZ + (H - HZ) * s; hgt = 20 + 200 * s; wdt = max(1, int(5 * s))
        c = lerp(fog, (28, 22, 16) if mode != 'night' else (10, 10, 8), s ** 0.5)
        d.rectangle((bx, by - hgt, bx + wdt, by), fill=c); d.rectangle((bx - 14 * s - 2, by - hgt + 6 * s, bx + 14 * s + wdt + 2, by - hgt + 6 * s + max(1, int(2 * s))), fill=c)
        if i < 8: d.line((bx + wdt / 2, by - hgt + 4, 312 - 470 * ((i + 1) / 8) ** 2.2, HZ + (H - HZ) * ((i + 1) / 8) ** 2.2 - 20 - 200 * ((i + 1) / 8) ** 2.2 + 6), fill=c)
    if mode == 'night':
        cone = Image.new('L', (W, H), 0); ImageDraw.Draw(cone).polygon([(300, 150), (345, 150), (720, 360), (-80, 360)], fill=255)
        lit = Image.eval(im, lambda v: min(255, int(v * 3.4 + 18)))
        im.paste(lit, mask=cone)
        fogglow = Image.new('L', (W, H), 0); ImageDraw.Draw(fogglow).polygon([(280, 100), (360, 100), (420, 150), (220, 150)], fill=255)
        im.paste(Image.eval(im, lambda v: min(255, int(v * 2 + 24))), mask=fogglow)
    return im.convert('RGBA')

# ---------------------------------------------------------------- build
def stack(*layers):
    out = layers[0].copy()
    for l in layers[1:]: out.alpha_composite(l)
    return out

def main():
    L = {
        'interior_frame': interior_frame(), 'driver': driver(), 'wheel': wheel(),
        'driver_left': driver(30), 'driver_right': driver(-30),
        'dash_lights': dash_lights(), 'lamp_fuel': lamp('fuel'), 'lamp_engine': lamp('engine'), 'lamp_highbeam': lamp('highbeam'),
        'night_tint': night_tint(), 'glovebox_open': glovebox_open(), 'mod_bars': mod_bars(), 'mod_plow': mod_plow(),
    }
    for name, w, seed in (('windscreen', WS, 1), ('left', WL, 2), ('right', WR, 3)):
        L[f'glass_{name}_chipped'] = chips(w, seed); L[f'glass_{name}_cracked'] = cracked(w, seed + 10); L[f'glass_{name}_broken'] = broken(w, seed + 20)
    for k, v in L.items(): v.save(f'{OUT}/{k}.png')

    previews = {
        'preview_dusk': stack(scene('dusk'), L['interior_frame'], L['dash_lights'], L['wheel'], L['driver']),
        'preview_night': stack(scene('night'), L['interior_frame'], L['dash_lights'], L['lamp_highbeam'], L['lamp_fuel'], L['wheel'], L['driver'], L['night_tint']),
        'preview_day_glovebox': stack(scene('day'), L['interior_frame'], L['glovebox_open'], L['dash_lights'], L['wheel'], L['driver']),
        'preview_mods': stack(scene('dusk'), L['mod_plow'], L['mod_bars'], L['interior_frame'], L['dash_lights'], L['lamp_engine'], L['wheel'], L['driver']),
        'preview_damage': stack(scene('day'), L['glass_windscreen_cracked'], L['glass_left_chipped'], L['glass_right_broken'], L['interior_frame'], L['dash_lights'], L['driver_left']),
    }
    for k, v in previews.items(): v.resize((1280, 720), Image.NEAREST).save(f'{OUT}/{k}.png')

    # self-check: sizes, see-through windows, palette, hard alpha on art layers
    cols = set()
    for k, v in L.items():
        assert v.size == (W, H), k
        for px in v.getdata():
            if px[3]: cols.add(px[:3])
    assert all(L['interior_frame'].getpixel(p)[3] == 0 for p in ((320, 110), (20, 120), (620, 120))), 'windows not transparent'
    assert cols <= set(PAL.values()), cols - set(PAL.values())
    print('ok: %d layers, %d colours used' % (len(L), len(cols)))

if __name__ == '__main__':
    main()
